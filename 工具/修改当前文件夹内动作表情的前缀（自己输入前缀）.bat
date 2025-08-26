@echo off
setlocal enabledelayedexpansion

:: 提示用户输入要添加的字段
set /p prefix="Enter the prefix to add to the filenames: "

:: 遍历当前目录下的所有 .mtn 和 .json 文件
for %%f in (*.mtn *.json) do (
    :: 获取文件的完整路径
    set "filePath=%%f"
    :: 获取文件名（不包括扩展名）
    set "fileName=%%~nf"
    :: 获取文件扩展名
    set "fileExt=%%~xf"
    :: 构建新的文件名
    set "newFileName=!prefix!!fileName!!fileExt!"
    :: 清除临时变量
    set "tempFileName="
    :: 重命名文件
    echo Renaming "%%f" to "!newFileName!"
    ren "%%f" "!newFileName!"
)

echo Done
pause