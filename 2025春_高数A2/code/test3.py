import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# 定义泰勒展开函数
def taylor_expansion(x, n, a=2):
    # e^x 在 x=a 处的泰勒展开
    return sum(((x - a)**k / factorial(k)) * np.exp(a) for k in range(n+1))

# 定义x的取值范围
x = np.linspace(0, 4, 400)

# 函数的实际值 e^x
y_exact = np.exp(x)

# 绘制不同阶数的泰勒展开
plt.figure(figsize=(10, 6))

# 1阶到6阶的泰勒展开
for n in range(1, 7):
    y_taylor = taylor_expansion(x, n)
    plt.plot(x, y_taylor, label=f'Taylor expansion (n={n})')

# 绘制 e^x 的实际函数图像
plt.plot(x, y_exact, label="Exact $e^x$", color="black", linestyle="--")

# 添加图例和标签
plt.title("$e^x$ and its Taylor expansions at $x=2$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.axvline(x=2, color="gray", linestyle=":")  # 标记x=2处
plt.legend()
plt.grid(True)

# 显示图像
plt.show()
