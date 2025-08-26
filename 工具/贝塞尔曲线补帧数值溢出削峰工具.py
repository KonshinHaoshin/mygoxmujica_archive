def modify_array(min_value, max_value, target_array):
    modified_array = []

    for num in target_array:
        try:
            num = float(num)
            if num < min_value:
                modified_array.append(min_value)
            elif num > max_value:
                modified_array.append(max_value)
            else:
                modified_array.append(num)
        except ValueError:
            modified_array.append(num)

    return modified_array

def format_output(target_array):
    return ','.join(map(str, target_array))

def write_to_txt(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# 获取用户输入
min_value = float(input("请输入最小值："))
max_value = float(input("请输入最大值："))
target_array = input("请输入目标数组（用逗号分隔）：").split(',')

# 修改数组
modified_array = modify_array(min_value, max_value, target_array)

# 输出结果
output = format_output(modified_array)
print("修改后的数组：", output)

# 将结果写入文本文件
filename = input("请输入要保存的文件名（不包含扩展名）：") + ".txt"
write_to_txt(filename, output)
print("结果已保存至", filename)