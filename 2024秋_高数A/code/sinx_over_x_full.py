import numpy as np
import matplotlib.pyplot as plt

# 创建x的范围
x = np.linspace(-15, 15, 1000)
y = np.sin(x)/x  

# 创建图形，保持比例相等
plt.figure(figsize=(6, 6))

# 绘制y=x的对称轴
#plt.plot([-5, 5], [-2, 8], 'gray', linestyle='--', label='y = x')

# 绘制指数函数
plt.plot(x, y, label=r'$y = \sin(x)/x$', color='blue')

# 设置axis equal
# plt.axis('equal')

# 添加图例、标题和标签
#plt.legend()
#plt.title("Exponent and Logarithm Functions (Base e)")
plt.xlabel("x")
plt.ylabel("y")

# 设置图形的显示范围
plt.xlim([-15, 15])
plt.ylim([-1, 2])
plt.plot(0, 1, 'o', markerfacecolor="white")
# 显示网格
plt.grid(True)

plt.savefig("media/img/sinx_over_x_full.png")

# 显示图形
plt.show()


