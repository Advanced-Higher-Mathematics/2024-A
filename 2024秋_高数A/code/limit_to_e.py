import numpy as np
import matplotlib.pyplot as plt

n = range(1, 40)
y = (1+np.divide(1, n))**n  

# 创建图形，保持比例相等
plt.figure(figsize=(6, 6))

# 绘制y=x的对称轴
#plt.plot([-5, 5], [-2, 8], 'gray', linestyle='--', label='y = x')

# 绘制指数函数
plt.plot(n, y, '.', label=r'$y = (1+1/n)^n$', color='blue')

# 设置axis equal
# plt.axis('equal')

# 添加图例、标题和标签
#plt.legend()
#plt.title("Exponent and Logarithm Functions (Base e)")
plt.xlabel("n")
plt.ylabel("y")

# 设置图形的显示范围
plt.xlim([0, 40])
plt.ylim([1.8, 2.8])
#plt.plot(0, 1, 'o', markerfacecolor="white")
# 显示网格
plt.grid(True)

plt.savefig("media/img/limit_to_e.png")

# 显示图形
plt.show()


