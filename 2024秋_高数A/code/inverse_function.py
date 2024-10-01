import numpy as np
import matplotlib.pyplot as plt

# 创建x的范围
x = np.linspace(0.00001, 5, 400)
y = np.linspace(-5, 5, 400)

# 指数函数和对数函数
exp_y = np.exp(y)  # 指数函数
log_x = np.log(x)  # 对数函数

# 创建图形，保持比例相等
plt.figure(figsize=(6, 6))

# 绘制y=x的对称轴
plt.plot([-4, 4], [-4, 4], 'gray', linestyle='--', label='y = x')

# 绘制指数函数
plt.plot(y, exp_y, label=r'$y = e^x$', color='blue')

# 绘制对数函数
plt.plot(x, log_x, label=r'$y = \ln(x)$', color='green')

# 设置axis equal
plt.axis('equal')

# 添加图例、标题和标签
plt.legend()
plt.title("Exponent and Logarithm Functions (Base e)")
plt.xlabel("x")
plt.ylabel("y")

# 设置图形的显示范围
plt.xlim([-4, 4])
plt.ylim([-4, 4])

# 显示网格
plt.grid(True)

plt.savefig("inverse_function.png")

# 显示图形
plt.show()


