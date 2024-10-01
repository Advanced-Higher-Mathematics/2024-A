import turtle
import time

# 设置屏幕
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Clock")
screen.tracer(0)  # 关闭自动刷新，手动刷新以提高性能

# 创建画笔对象
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# 画钟表圆形和刻度
def draw_clock(pen):
    # 画钟表圆形
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()
    pen.circle(250)

    # 画刻度
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(220)
        pen.pendown()
        pen.fd(30)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

# 画针的函数
def draw_hand(angle, length, pen, color, pensize):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.rt(angle)
    pen.pendown()
    pen.pensize(pensize)
    pen.pencolor(color)
    pen.fd(length)

# 获取时间并转换成角度
def get_time_angles():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # 将时间转换为角度
    hour_angle = (hours + minutes / 60) * 30  # 每小时30度
    minute_angle = (minutes + seconds / 60) * 6  # 每分钟6度
    second_angle = seconds * 6  # 每秒钟6度

    return hour_angle, minute_angle, second_angle

# 主程序循环
def run_clock():
    while True:
        pen.clear()

        # 画固定的钟表背景
        draw_clock(pen)

        # 获取当前时间的角度
        hour_angle, minute_angle, second_angle = get_time_angles()

        # 画时针、分针和秒针
        draw_hand(hour_angle, 100, pen, "black", 8)   # 时针
        draw_hand(minute_angle, 150, pen, "blue", 4)  # 分针
        draw_hand(second_angle, 180, pen, "red", 2)   # 秒针

        # 更新屏幕
        screen.update()

        # 每秒更新一次
        time.sleep(1)

# 运行时钟
run_clock()

# 保持窗口打开
screen.mainloop()
