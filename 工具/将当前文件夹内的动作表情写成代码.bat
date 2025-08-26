@echo off
setlocal enabledelayedexpansion

REM 创建或清空data.txt文件
echo [] > data.txt

REM 遍历当前目录下的所有.mtn文件
for %%f in (*.mtn) do (
    REM 将文件名添加到data.txt中
    echo,"%%~nf":[{"file":"live2d/chara/xxxx/%%~nf.mtn"}],>> data.txt
)

REM 在.mtn和.exp.json文件输出之间添加三行空行
echo. >> data.txt
echo. >> data.txt
echo. >> data.txt

REM 遍历当前目录下的所有.exp.json文件
for %%f in (*.exp.json) do (
    REM 将文件名添加到data.txt中
    echo,{"name":"%%~nf","file":"live2d/chara/xxxx/%%~nf.exp.json"}, >> data.txt
)

echo 数据已写入到data.txt

setlocal enabledelayedexpansion

REM 获取当前文件夹的名称
for %%i in ("%cd%") do set foldername=%%~nxi

REM 替换文本文件中的字符串
for %%f in (*.txt) do (
    echo Processing file: %%f
    powershell -command "(Get-Content '%%f') -replace 'xxxx', '!foldername!' | Set-Content '%%f'"
)

echo Replacement completed.
pause