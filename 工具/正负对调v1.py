user_input = input("请输入用逗号隔开的数组: ")
numbers = user_input.split(",")

result = []
for number in numbers:
    if number.startswith("-"):
        result.append(number[1:])
    else:
        result.append("-" + number)

output = ",".join(result)
print(output)