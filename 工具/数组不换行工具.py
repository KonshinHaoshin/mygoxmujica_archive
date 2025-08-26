def transform_array(target_array):
    transformed_array = []

    for line in target_array:
        line = line.strip()
        if line:
            elements = line.split(',')
            transformed_array.extend(elements)

    return transformed_array

def format_output(target_array):
    return ','.join(target_array)

def write_to_txt(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# 获取用户输入
target_array = []
print("请输入带有换行符的目标数组，输入空行结束：")
while True:
    line = input()
    if line == "":
        break
    target_array.append(line)

# 转换数组
transformed_array = transform_array(target_array)

# 格式化输出
output = format_output(transformed_array)
print("转换后的数组：", output)

# 将结果写入文本文件
filename = input("请输入要保存的文件名（不包含扩展名）：") + ".txt"
write_to_txt(filename, output)
print("结果已保存至", filename)