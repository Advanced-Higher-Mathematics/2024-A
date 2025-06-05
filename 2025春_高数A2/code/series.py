import numpy as np
import matplotlib.pyplot as plt

# 定义原函数
def f(x):
    return 1 / (1 + x)

# 定义幂级数部分和
def s_n(x, n):
    total = 0
    for k in range(n + 1):
        total += (-1)**k * x**k
    return total

# 创建x值数组（避开奇点x=-1）
x = np.linspace(-5, 5, 1000)
x = x[~np.isclose(x, -1, atol=0.01)]  # 移除x=-1附近的点

# 计算原函数值（在x≠-1处定义）
y_f = np.where(np.abs(x + 1) > 0.01, f(x), np.nan)

# 不同阶数的部分和
N_values = [0, 1, 2, 3, 5, 10, 20, 50]

# 创建图形
plt.figure(figsize=(12, 8))

# 绘制原函数
plt.plot(x, y_f, label='原函数: $f(x) = \\frac{1}{1+x}$', 
         linewidth=3, color='black')

# 绘制不同阶数的部分和
colors = plt.cm.viridis(np.linspace(0, 1, len(N_values)))
for i, N in enumerate(N_values):
    y_s = s_n(x, N)
    plt.plot(x, y_s, linestyle='--', linewidth=1.5, 
             alpha=0.8, color=colors[i],
             label=f'部分和 $N={N}$')

# 标记关键点和区域
plt.axvline(x=-1, color='red', linestyle='-', alpha=0.3, label='奇点 $x=-1$')
plt.axvline(x=1, color='green', linestyle='-', alpha=0.3)
plt.axvline(x=-1, color='red', linestyle='', marker='x', markersize=8)
plt.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
plt.fill_between([-1, 1], -20, 20, color='green', alpha=0.05, 
                 label='收敛区域 $|x|<1$')

# 设置图形属性
plt.title('$\\frac{1}{1+x}$ 的幂级数逼近 ($x \in [-5, 5]$)', fontsize=16)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.2)

# 设置坐标轴范围
plt.ylim(-10, 10)
plt.xlim(-5, 5)

# 添加收敛区域标记
plt.text(0, -8, '收敛区域 $|x|<1$', ha='center', fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.8))
plt.text(3, -8, '发散区域', ha='center', fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.8))
plt.text(-3, -8, '发散区域', ha='center', fontsize=12, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()