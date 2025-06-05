import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 定义Lotka-Volterra方程组
def lotka_volterra(state, t, alpha, beta, delta, gamma):
    prey, predator = state
    # prey的变化率: dx/dt = αx - βxy
    dprey_dt = alpha * prey - beta * prey * predator
    # predator的变化率: dy/dt = δxy - γy
    dpredator_dt = delta * prey * predator - gamma * predator
    return [dprey_dt, dpredator_dt]

# 设置参数
alpha = 1.0  # prey的自然增长率
beta = 0.5   # prey被捕食的率
delta = 0.5  # predator的出生率
gamma = 2.0  # predator的死亡率

# 设置初始条件
x0 = 2.0  # prey的初始数量
y0 = 1.0  # predator的初始数量
state0 = [x0, y0]

# 设置时间点
t = np.linspace(0, 30, 1000)

# 求解微分方程
solution = odeint(lotka_volterra, state0, t, args=(alpha, beta, delta, gamma))
prey_values = solution[:, 0]
predator_values = solution[:, 1]

# 绘制时间序列图
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, prey_values, 'b-', label='Prey (x)')
plt.plot(t, predator_values, 'r-', label='Predator (y)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Time Series')
plt.grid(True)
plt.legend()

# 绘制相图
plt.subplot(1, 2, 2)
plt.plot(prey_values, predator_values, 'g-')
plt.xlabel('Prey Population (x)')
plt.ylabel('Predator Population (y)')
plt.title('Phase Portrait')
plt.grid(True)

plt.tight_layout()
plt.show()
