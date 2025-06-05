import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# 定义物理常数
G = 6.67430e-11  # 万有引力常数
M = 1.989e30     # 太阳质量 (kg)

def planet_motion(state, t):
    # state包含位置和速度: [x, y, z, vx, vy, vz]
    x, y, z, vx, vy, vz = state
    
    # 计算行星到太阳的距离
    r = np.sqrt(x**2 + y**2 + z**2)
    
    # 计算加速度分量
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    az = -G * M * z / r**3
    
    return [vx, vy, vz, ax, ay, az]

# 设置初始条件 (以地球为例)
x0 = 0.496e11    # 地球到太阳的平均距离
vz0 = 49.78e3    # 地球公转速度

initial_state = [x0, 0, 0,    # 初始位置
                0, vz0, 0]    # 初始速度

# 设置时间点 (一年的时间)
t = np.linspace(0, 365*24*3600, 1000)

# 求解微分方程
solution = odeint(planet_motion, initial_state, t)

# 提取位置数据
x = solution[:, 0]
y = solution[:, 1]
z = solution[:, 2]

# 创建动画
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# 绘制太阳
ax.scatter([0], [0], [0], color='yellow', s=100, label='Sun')

# 初始化行星轨迹
line, = ax.plot([], [], [], 'b-', label='Orbit')
point, = ax.plot([], [], [], 'bo', markersize=10, label='Planet')

# 设置坐标轴范围
limit = 1.5e11
ax.set_xlim([-limit, limit])
ax.set_ylim([-limit, limit])
ax.set_zlim([-limit, limit])

ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.legend()

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point

def animate(i):
    # 绘制轨迹
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
    
    # 绘制行星当前位置
    point.set_data([x[i]], [y[i]])
    point.set_3d_properties([z[i]])
    
    return line, point

# 创建动画
anim = animation.FuncAnimation(fig, animate, init_func=init,
                             frames=len(t), interval=20, 
                             blit=True)

plt.title('Planet Motion Around the Sun')
plt.show()
