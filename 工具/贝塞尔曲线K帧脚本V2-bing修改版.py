import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
# 导入Tkinter模块
from tkinter import *

# 创建一个Tk对象，代表一个窗口
window = Tk()
# 设置窗口的标题
window.title("Bezier Curve")
# 设置窗口的大小
window.geometry("400x300")

# 定义一个函数，用来获取用户输入的坐标轴范围
def get_range():
    # 获取x轴最小值和最大值
    global x_min, x_max
    x_min, x_max = map(float, x_range.get().split(':'))
    # 获取y轴最小值和最大值
    global y_min, y_max
    y_min, y_max = map(float, y_range.get().split(':'))

# 定义一个函数，用来获取用户输入的坐标点
def get_points():
    # 获取x轴和y轴对应参数
    global x_values, y_values
    x_values, y_values = [], []
    for point in points.get().split(','):
        if ':' not in point:
            continue
        x, y = map(float, point.split(':'))
        x_values.append(x)
        y_values.append(y)
    # 检查坐标点数量是否足够
    if len(x_values) < 2 or len(y_values) < 2:
        # 在输出框中显示错误信息
        output.insert(END, "错误：坐标点数量不足\n")
        return

# 定义一个函数，用来绘制贝塞尔样条曲线
def draw_curve():
    # 调用之前定义的函数，获取用户输入的数据
    get_range()
    get_points()
    # 创建坐标系
    fig, ax = plt.subplots()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('gray')
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('gray')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.yaxis.tick_left()
    ax.xaxis.tick_bottom()
    # 绘制贝塞尔样条曲线
    t = np.linspace(0, 1, 100)
    spl = make_interp_spline(x_values, y_values)
    smooth_x = np.linspace(min(x_values), max(x_values), 100)
    smooth_y = spl(smooth_x)
    ax.plot(smooth_x, smooth_y, 'b-', label='Bezier Curve')
    ax.scatter(x_values, y_values, color='red', label='Control Points')
    ax.legend()
    # 保存贝塞尔曲线到txt文件
    with open('bezier_curve.txt', 'w') as f:
        f.write("x,y\n")
        for i in range(len(smooth_x)):
            f.write(f"{smooth_x[i]:.3f},{smooth_y[i]:.3f}\n")
    # 在输出框中显示成功信息
    output.insert(END, "贝塞尔曲线已保存到txt文件\n")
    # 输出x轴上所有整数对应的y轴值
    x_integers = np.arange(np.ceil(x_min), np.floor(x_max) + 1)
    y_integer_values = spl(x_integers)
    y_integer_values = [f"{value:.3f}" for value in y_integer_values]
    output.insert(END, "x轴上所有整数对应的y轴值：\n")
    output.insert(END, ",".join(y_integer_values) + "\n")
    # 显示坐标系和曲线
    plt.show()

# 在窗口中添加一个标签，用来显示提示信息
label1 = Label(window, text="请输入x轴最小值和最大值（用冒号分隔）：")
# 将标签放置在第一行第一列
label1.grid(row=0, column=0)
# 在窗口中添加一个文本框，用来输入x轴范围
x_range = Entry(window)
# 将文本框放置在第一行第二列
x_range.grid(row=0, column=1)

# 在窗口中添加一个标签，用来显示提示信息
label2 = Label(window, text="请输入y轴最小值和最大值（用冒号分隔）：")
# 将标签放置在第二行第一列
label2.grid(row=1, column=0)
# 在窗口中添加一个文本框，用来输入y轴范围
y_range = Entry(window)
# 将文本框放置在第二行第二列
y_range.grid(row=1, column=1)

# 在窗口中添加一个标签，用来显示提示信息
label3 = Label(window, text="请输入x轴和y轴对应参数（用逗号分隔）：")
# 将标签放置在第三行第一列
label3.grid(row=2, column=0)
# 在窗口中添加一个文本框，用来输入坐标点
points = Entry(window)
# 将文本框放置在第三行第二列
points.grid(row=2, column=1)

# 在窗口中添加一个按钮，用来执行绘制曲线的命令
button = Button(window, text="绘制曲线", command=draw_curve)
# 将按钮放置在第四行第一列
button.grid(row=3, column=0)

# 在窗口中添加一个文本框，用来显示输出信息
output = Text(window, width=30, height=10)
# 将文本框放置在第四行第二列
output.grid(row=3, column=1)

# 启动窗口的主循环
window.mainloop()

'''
使用方法示例：
请输入x轴最小值和最大值（用冒号分隔）：0:30
请输入y轴最小值和最大值（用冒号分隔）：-1:1
请输入x轴和y轴对应参数（用逗号分隔）：0:0.22,4:0.41,15:0.31,30:0.22
'''