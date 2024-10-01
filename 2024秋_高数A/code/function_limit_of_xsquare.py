import numpy as np
import matplotlib.pyplot as plt

# 创建x的范围
x = np.linspace(-5, 5, 400)
y = np.linspace(-2, 8, 400)

# 指数函数和对数函数
xsquare = x*x + 1  # 指数函数

# 创建图形，保持比例相等
plt.figure(figsize=(6, 6))

# 绘制y=x的对称轴
#plt.plot([-5, 5], [-2, 8], 'gray', linestyle='--', label='y = x')

# 绘制指数函数
plt.plot(x, xsquare, label=r'$y = x^2$', color='blue')

# 设置axis equal
# plt.axis('equal')

# 添加图例、标题和标签
#plt.legend()
#plt.title("Exponent and Logarithm Functions (Base e)")
plt.xlabel("x")
plt.ylabel("y")

# 设置图形的显示范围
plt.xlim([-5, 5])
plt.ylim([-2, 8])

# 显示网格
plt.grid(True)

plt.savefig("media/img/function_limit_of_xsquare.png")

# 显示图形
plt.show()


