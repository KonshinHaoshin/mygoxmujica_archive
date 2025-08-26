
// 该脚本用于批量修改 .mtn 文件中的 PARAM_IMPORT 参数，可以指定新的数字，也可以移除 PARAM_IMPORT 参数。
// 脚本使用方法：
// 1. 打开命令行（Win + R -> cmd -> 回车）
// 2. 切换到脚本所在目录（cd 文件路径）
// 3. 运行脚本（node mtnPARAM_IMPORT参数批量修改脚本.js 文件夹路径 新的数字（可选））
// 4. 脚本运行完成后，会在命令行输出处理的文件数量。
// 5. 脚本会自动递归遍历文件夹及其子文件夹，并处理 .mtn 文件。
// 6. 有新数字时，脚本会自动在文件末尾添加 PARAM_IMPORT 参数，如果文件中已经存在 PARAM_IMPORT 参数，则会更新其值。
// 7. 没有新数字时，脚本会自动移除 PARAM_IMPORT 参数，如果文件中不存在 PARAM_IMPORT 参数，则不会有任何操作。





const fs = require('fs');
const path = require('path');

// 获取用户输入
const folderPath = process.argv[2]; // 第一个参数为文件夹路径
const newNumber = process.argv[3]; // 第二个参数为新的数字

if (!folderPath) {
    console.error('请提供文件夹路径作为输入参数.');
    process.exit(1);
}

let cnt = 0;

// 遍历文件夹及其子文件夹的函数
function traverseDirectory(dir) {
    try {
        const files = fs.readdirSync(dir); // 使用同步读取文件夹

        files.forEach(file => {
            const filePath = path.join(dir, file);
            const stats = fs.statSync(filePath); // 使用同步获取文件状态

            if (stats.isDirectory()) {
                // 如果是文件夹，递归调用
                traverseDirectory(filePath);
            } else if (path.extname(file) === '.mtn') {
                // 如果是 .mtn 文件，处理文件
                processMtnFile(filePath);
                cnt++;
                console.log(`已处理 ${cnt} 个文件.`);
            }
        });
    } catch (err) {
        console.error(`无法读取文件夹: ${dir}`, err);
    }
}

// 处理 .mtn 文件的函数
function processMtnFile(filePath) {
    try {
        const data = fs.readFileSync(filePath, 'utf8'); // 使用同步读取文件

        const regex = /PARAM_IMPORT=\d+/;
        if (newNumber) {
            // 如果提供了新的数字，则替换 PARAM_IMPORT 后面的数字
            if (regex.test(data)) {
                const newData = data.replace(regex, `PARAM_IMPORT=${newNumber}`);
                fs.writeFileSync(filePath, newData, 'utf8'); // 使用同步写入文件
                console.log(`已更新文件: ${filePath}`);
            } else {
                // 如果不存在，则在文件末尾添加 PARAM_IMPORT=
                const newData = data + `\nPARAM_IMPORT=${newNumber}\n`;
                fs.writeFileSync(filePath, newData, 'utf8'); // 使用同步写入文件
                console.log(`已添加 PARAM_IMPORT 至文件: ${filePath}`);
            }
        } else {
            // 如果没有提供新的数字，则移除 PARAM_IMPORT
            const newData = data.replace(/PARAM_IMPORT=\d+\n?/g, ''); // 移除 PARAM_IMPORT 行
            fs.writeFileSync(filePath, newData, 'utf8'); // 使用同步写入文件
            console.log(`已移除 PARAM_IMPORT 至文件: ${filePath}`);
        }
    } catch (err) {
        console.error(`无法处理文件: ${filePath}`, err);
    }
}

// 开始遍历指定的文件夹
traverseDirectory(folderPath);
console.log(`共处理 ${cnt} 个文件.`);
