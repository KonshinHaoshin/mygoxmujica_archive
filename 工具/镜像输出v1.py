def mirror_arrays():
    input_str = input("请输入多个浮点数组，每组之间用逗号隔开：")
    input_arrays = input_str.split(',')

    merged_array = []
    for arr in input_arrays:
        arr = arr.split(',')
        arr = [float(num) for num in arr if num.strip() != '']
        merged_array.extend(arr)  # 将每个数组添加到合并数组中

    mirrored_array = merged_array[::-1]  # 将合并数组按镜像顺序翻转

    output_str = ','.join(str(num) for num in mirrored_array)  # 将数组元素转换为字符串，并用逗号隔开
    print(output_str)  # 输出元素字符串

mirror_arrays()