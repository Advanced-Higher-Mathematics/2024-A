---
title: 高等数学讲义(上)
author: 胡煜成
description: 首都师范大学2024秋季学期高等数学A
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,讲义
vlook-chp-autonum: h1{{第 ### 节 }},h3{{### }}
vlook-query: vdl=on
vlook-query: ws=off
---

[回到主页面](index.html)


# 微分方程

[待补充]



> [!warning]
>
> ==李普希茨条件（Lipschitz Condition）==
>
> > ==定义==
> >
> > 一个函数 $f: \mathbb{R} \to \mathbb{R}$ 满足**李普希茨条件**，如果存在一个常数 $L \geq 0$，使得对于所有的 $x_1, x_2 \in \mathbb{R}$，都有：
> > $$
> > |f(x_1) - f(x_2)| \leq L |x_1 - x_2|
> > $$
> > 在这种情况下，我们称 $f$ 是一个 **李普希茨连续**（Lipschitz continuous）的函数，$L$ 被称为**李普希茨常数**。
>
> > ==结论==
> >
> > 一个函数 $f: \mathbb{R} \to \mathbb{R}$ 满足**李普希茨条件**，如果存在一个常数 $L \geq 0$，使得对于所有的 $x_1, x_2 \in \mathbb{R}$，都有：
> > $$
> > |f(x_1) - f(x_2)| \leq L |x_1 - x_2|
> > $$
> > 在这种情况下，我们称 $f$ 是一个 **李普希茨连续**（Lipschitz continuous）的函数，$L$ 被称为**李普希茨常数**。
>
> > ==意义==
> >
> > 李普希茨条件限制了函数在其定义域内的变化速度，保证了函数不会在任意小的区域内有过大的变化。如果一个函数是李普希茨连续的，那么它也是连续的，但反过来不一定成立。即，所有李普希茨连续函数都是连续函数，但并不是所有连续函数都是李普希茨连续的。
>
> > ==示例==
> >
> > 1. **线性函数**：$f(x) = kx + b$，其中 $k$ 是常数。这个函数是李普希茨连续的，李普希茨常数为 $|k|$。
> > 2. **绝对值函数**：$f(x) = |x|$ 是李普希茨连续的，李普希茨常数为 $1$。
> > 3. **非李普希茨函数**：例如，$f(x) = x^2$ 在整个实数集上不是李普希茨连续的，因为在无穷大处，函数的增长速度无限制。


>多项式展开：
>$$ f(x) = a_0 + a_1x + a_2x^2 + \cdots + a_nx^n + \cdots$$
>
>离散点近似：
>$$ f(x) \sim \begin{bmatrix} 
f(0) \\ 
f(0.25) \\ 
f(0.5) \\ 
f(0.75) \\ 
f(1) 
\end{bmatrix}  $$


>矩阵形式展开
>
>将函数表示为系数方程组：
>$$
\begin{cases}
f(0)   = a_0 + a_1 \cdot 0 + a_2 \cdot 0^2 + a_3 \cdot 0^3 + a_4 \cdot 0^4 \\
f(0.25)= a_0 + a_1 \cdot \frac{1}{4} + a_2 \cdot \left(\frac{1}{4}\right)^2 + a_3 \cdot \left(\frac{1}{4}\right)^3 + a_4 \cdot \left(\frac{1}{4}\right)^4 \\
f(0.5) = a_0 + a_1 \cdot \frac{1}{2} + a_2 \cdot \left(\frac{1}{2}\right)^2 + a_3 \cdot \left(\frac{1}{2}\right)^3 + a_4 \cdot \left(\frac{1}{2}\right)^4 \\
f(0.75)= a_0 + a_1 \cdot \frac{3}{4} + a_2 \cdot \left(\frac{3}{4}\right)^2 + a_3 \cdot \left(\frac{3}{4}\right)^3 + a_4 \cdot \left(\frac{3}{4}\right)^4 \\
f(1)   = a_0 + a_1 \cdot 1 + a_2 \cdot 1^2 + a_3 \cdot 1^3 + a_4 \cdot 1^4
\end{cases}
>$$
>
>简写为矩阵形式：
>$$
>\begin{bmatrix} 
f(0) \\ 
f(0.25) \\ 
f(0.5) \\ 
f(0.75) \\ 
f(1) 
\end{bmatrix}=a_0
\begin{bmatrix} 
1 \\ 
1 \\ 
1 \\ 
1 \\
1 
\end{bmatrix}    
+a_1\begin{bmatrix} 
0 \\ 
\frac{1}{4} \\ 
\frac{1}{2} \\ 
\frac{3}{4} \\
1 
\end{bmatrix} 
+a_2\begin{bmatrix} 
0 \\ 
\frac{1}{16} \\ 
\frac{1}{4} \\ 
\frac{9}{16} \\
1 
\end{bmatrix} 
+a_3\begin{bmatrix} 
0 \\ 
\frac{1}{64} \\ 
\frac{1}{8} \\ 
\frac{27}{64} \\
1 
\end{bmatrix} 
+a_4\begin{bmatrix} 
0 \\ 
\left(\frac{1}{4}\right)^4 \\ 
\left(\frac{1}{2}\right)^4 \\ 
\left(\frac{3}{4}\right)^4 \\
1 
\end{bmatrix}
>$$
>
>$$
=\begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
1 & \frac{1}{4} & \frac{1}{16} & \frac{1}{64} & \frac{1}{256} \\
1 & \frac{1}{2} & \frac{1}{4} & \frac{1}{8} & \frac{1}{16} \\
1 & \frac{3}{4} & \frac{9}{16} & \frac{27}{64} & \frac{81}{256} \\
1 & 1 & 1 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
a_0 \\
a_1 \\
a_2 \\
a_3 \\
a_4
\end{bmatrix}
>$$

>[!tip]
>
> 1. $a_0,a_1,...,a_4$ 不好算
> 2. 性质也不好.

>$$
>\begin{bmatrix}
1 \\
0 \\
0 \\
0 \\
0
\end{bmatrix}
\begin{bmatrix}
0 \\
1 \\
0 \\
0 \\
0
\end{bmatrix}
\begin{bmatrix}
0 \\
0 \\
1 \\
0 \\
0
\end{bmatrix}
\begin{bmatrix}
0 \\
0 \\
0 \\
1 \\
0
\end{bmatrix}
\begin{bmatrix}
0 \\
0 \\
0 \\
0 \\
1
\end{bmatrix}
$$

> [!tip]
> 1. ${a}$好算.
> 2. 不连续.

> 傅里叶级数 
>**积分公式**： 
>$$
\int_0^1 \sin(2\pi x) \, dx = 0= \int_0^1 \cos(2\pi x) \, dx 
>$$
>$$
\int_0^1 \sin(2\pi n x) \sin(2\pi m x) \, dx = 0 \quad (n \neq m)
>$$
>$$
\int_0^1 \cos(2\pi n x) \cos(2\pi m x) \, dx = \frac{1}{2} \int_0^1 \left[\cos(2\pi (n+m)x) + \cos(2\pi (n-m)x)\right] \, dx = 0
>$$
>$$
\int_0^1 dx = 1, \quad \int_0^1 \sin^2(2\pi n x) \, dx =  \int_0^1 \frac{1- \cos((2\pi)2 n x) }{2}dx =\frac{1}{2}
>$$

>**傅里叶级数展开式**： 
>$$
f(x) = \frac{a_0 }{2}+ \sum_{k=1}^{\infty} \left[ a_k \cos(\frac{2\pi k x}{T}) + b_n \sin(\frac{2\pi k x}{T}) \right]
>$$
这块笔记有问题！！！
>$$
a_k = \frac{2}{T}\int_0^T f(x) \cos(\frac{2\pi k x}{T}) \, dx, \quad b_k =  \frac{2}{T}\int_0^T f(x) \sin(\frac{2\pi k x}{T}) \, dx
>$$
>适用于周期函数（周期为 T）。

---

### 复数形式
>
>**欧拉公式**： 
>$$
e^{ix} = \cos x + i \sin x, \quad e^{-ix} = \cos x - i \sin x
>$$
>  
>$$
\cos x = \frac{1}{2} (e^{ix} + e^{-ix}), \quad \sin x = \frac{1}{2i} (e^{ix} - e^{-ix})
>$$



>周期为 $ 2l $。 
>
>函数 $ f(x) $ 的展开式： 
>
>$$
>f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(\frac{n\pi x}{l}) + b_n \sin(\frac{n\pi x}{l}) \right]
>$$
>
>**系数表达式**： 
>
>$$
>a_n =\frac{1}{l} \int_{-l}^{l} f(x) \cos(\frac{n\pi x}{l}) \, dx, \quad b_n = \frac{1}{l}\int_{-l}^{l} f(x) \sin(\frac{n\pi x}{l}) \, dx
>$$
>

> [!warning]
> ==欧拉公式==
   >$$ e^z = 1 + z + \frac{z^2}{2!} + \cdots + \frac{z^n}{n!}+ \cdots\quad (|z|<\infty ) $$
>$z= x + iy$
>
   >$ e^{iy} = 1 + iy - \frac{y^2}{2!} + \cdots+ \frac{y^n}{n!} +\cdots $
   >
   >$$\quad = (1-\frac{y^2}{2!}+\frac{y^4}{4!}- \cdots)+(i\frac{y^3}{3!}-i\frac{y^5}{5!}+\cdots)$$
   >$ \quad= \cos y + i \sin y $
>
   >$$ e^{xi} = \cos x + i \sin x $$
> 
>特例. $ e^{i}  = -1+ 0 $
>   $$ e^{i\pi} + 1 = 0 \quad \text{（最美公式）} $$


>**复数形式结果**： 
>$$
>\begin{aligned}
>f(x) & = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ \frac{a_n}{2}(e^{i\frac{n\pi x}{l}}+e^{-i\frac{n\pi x}{l}} ) - \frac{b_ni}{2} (e^{i\frac{n\pi x}{l}}-e^{-i\frac{n\pi x}{l}} )  \right] \\
>&= \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ \frac{a_n-b_ni}{2} e^{i\frac{n\pi x}{l}} + \frac{a_n+b_ni}{2} e^{-i\frac{n\pi x}{l}} \right]
>\end{aligned}
>$$



>[!note]
>
> >**例1:给定隐函数方程：$F(x, y, z) = 0 $,（也可以成 $z = z(x, y)$） 求以下两个偏导数：$ \displaystyle\frac{\partial z}{\partial x} $,$ \displaystyle\frac{\partial z}{\partial y} $.**
> >
> >**解:**
> > 对$x$求偏导： $ \displaystyle\frac{\partial F}{\partial x} + \displaystyle\frac{\partial F}{\partial z} \displaystyle\frac{\partial z}{\partial x} = 0 $
> > 对$y$求偏导： $ \displaystyle\frac{\partial F}{\partial y} + \displaystyle\frac{\partial F}{\partial z} \displaystyle\frac{\partial z}{\partial y} = 0 $
> > 最终公式: $ \displaystyle\frac{\partial z}{\partial x} = -\displaystyle\frac{\displaystyle\frac{\partial F}{\partial x}}{\displaystyle\frac{\partial F}{\partial z}} $ , $ \displaystyle\frac{\partial z}{\partial y} = -\displaystyle\frac{\displaystyle\frac{\partial F}{\partial y}}{\displaystyle\frac{\partial F}{\partial z}} $
>
> >**例2:给定隐函数方程：$ x^2 + y^2 + z^2 - 4z = 0 $,求 $ \displaystyle\frac{\partial^2 z}{\partial x^2}$.**
> >
> >**解:**一阶偏导数计算：$ \displaystyle\frac{\partial z}{\partial x} = -\displaystyle\frac{x}{z-2} $
> >二阶偏导数推导：
> >对一阶导结果再次求导： $ \displaystyle\frac{\partial^2 z}{\partial x^2} = \displaystyle\frac{d}{dx}\left( -\displaystyle\frac{x}{z-2} \right) $
> >应用商的导数法则：$ = -\displaystyle\frac{(1)(z-2) - x\displaystyle\frac{\partial z}{\partial x}}{(z-2)^2} $
> >代入$\displaystyle\frac{\partial z}{\partial x}$ 得$-\displaystyle\frac{(z-2) - x\left(-\displaystyle\frac{x}{z-2}\right)}{(z-2)^2} $ $ = \displaystyle\frac{2 - z - \displaystyle\frac{x^2}{z-2}}{(z-2)^2} $
>
>
> >**例3:给定两个隐函数方程：
> >$ 
> >\begin{cases}
> >P = F(x, y, u, v) = 0 \\
> >q = Q(x, y, u, v) = 0 
> >\end{cases}
> >$  需要求解的偏导数矩阵：$ 
> >\begin{pmatrix}
> >\displaystyle\frac{\partial u}{\partial x} & \displaystyle\frac{\partial u}{\partial y} \\
> >\displaystyle\frac{\partial v}{\partial x} & \displaystyle\frac{\partial v}{\partial y}
> >\end{pmatrix}
> >$**
> >
> >**解:**
> >对每个方程求全微分： $ 
> >\begin{cases}
> >dF = F_x dx + F_y dy + F_u du + F_v dv = 0 \\
> >dG = G_x dx + G_y dy + G_u du + G_v dv = 0 
> >\end{cases}
> >$
> >整理成矩阵形式：
> >$ 
> >\begin{pmatrix}
> >F_u & F_v \\
> >G_u & G_v 
> >\end{pmatrix}
> >\begin{pmatrix}
> >\displaystyle\frac{\partial u}{\partial x} \\
> >\displaystyle\frac{\partial v}{\partial x}
> >\end{pmatrix}
> >= -
> >\begin{pmatrix}
> >F_x \\
> >G_x 
> >\end{pmatrix}
> >$
> >解得：
> >$
> >\begin{pmatrix}
> >\displaystyle\frac{\partial u}{\partial x} \\
> >\displaystyle\frac{\partial v}{\partial x}
> >\end{pmatrix}
> >= -
> >\begin{pmatrix}
> >F_u & F_v \\
> >G_u & G_v 
> >\end{pmatrix}^{-1}
> >\begin{pmatrix}
> >F_x \\
> >G_x 
> >\end{pmatrix}
> >$
>
>
> >**例4：$
> > \begin{cases}
> > xu - yv = 0 \\
> > yu + xv = 1
> > \end{cases}
> > $ 求对函数 $u(x,y)$ 和 $v(x,y)$ 的偏导数$ u_x,u_y,v_x,v_y$.**
> > 
> > **解：**
> > 第一个方程对$x$求导：$ u + x\displaystyle\frac{\partial u}{\partial x} - y\displaystyle\frac{\partial v}{\partial x} = 0 $
> >  第二个方程对$x$求导：$y\displaystyle\frac{\partial u}{\partial x} + v + x\displaystyle\frac{\partial v}{\partial x} = 0 $
> > 整理成方程组：$
> > \begin{cases}
> > xu_x - yv_x = -u \\
> > yu_x + xv_x = -v
> > \end{cases}
> > $
> >从第一式解出： $ u_x = \displaystyle\frac{yv_x - u}{x} $
> > 代入第二式：$ y\left(\displaystyle\frac{yv_x - u}{x}\right) + v + xv_x = 0 $
> > 化简得：$ (x^2 + y^2)v_x = yu - xv $
> >最终解：$ v_x = \displaystyle\frac{yu - xv}{x^2 + y^2} $
>
>
> >**例5:给定约束方程组：
> > $ F = x - \rho\cos\theta = 0 $,
> > $ G = y - \rho\sin\theta = 0 $.**
> >
> >[此题有问题，请检阅]
> >**解:** 约束函数的雅可比矩阵（对变量 $x, y, \rho, \theta$ 求偏导）为：
> >$J =
> >\begin{bmatrix}
> >\displaystyle\frac{\partial F}{\partial x} & \displaystyle\frac{\partial F}{\partial y} & \displaystyle\frac{\partial F}{\partial \rho} & \displaystyle\frac{\partial F}{\partial \theta} \\
> >\displaystyle\frac{\partial G}{\partial x} & \displaystyle\frac{\partial G}{\partial y} & \displaystyle\frac{\partial G}{\partial \rho} & \displaystyle\frac{\partial G}{\partial \theta}
> >\end{bmatrix}=
> >\begin{bmatrix}
> >1 & 0 & -\cos\theta & \rho \sin\theta \\
> >0 & 1 & -\sin\theta & -\rho \cos\theta
> >\end{bmatrix}$
>
>
> >**例6:设 $u = f(x,y)$ 的所有二阶偏导数连续,将下列表达式转换为极坐标形式： 
> > (1) $\left( \dfrac{\partial u}{\partial x} \right)^2 + \left( \dfrac{\partial u}{\partial y} \right)^2$ 
> > (2) $\dfrac{\partial^2 u}{\partial x^2} + \dfrac{\partial^2 u}{\partial y^2}$.**
> >
> >**解:**  
> > 由极坐标关系 $\rho = \sqrt{x^2+y^2}$, $\theta = \arctan(y/x)$,通过链式法则：
> > $$ \displaystyle\frac{\partial u}{\partial x} = \displaystyle\frac{\partial u}{\partial \rho}\cos\theta - \displaystyle\frac{\partial u}{\partial \theta}\displaystyle\frac{\sin\theta}{\rho} $$
> > $$ \displaystyle\frac{\partial u}{\partial y} = \displaystyle\frac{\partial u}{\partial \rho}\sin\theta + \displaystyle\frac{\partial u}{\partial \theta}\displaystyle\frac{\cos\theta}{\rho} $$
> > $$ \left(\displaystyle\frac{\partial u}{\partial x}\right)^2 + \left(\displaystyle\frac{\partial u}{\partial y}\right)^2 = \left(\displaystyle\frac{\partial u}{\partial \rho}\right)^2 + \displaystyle\frac{1}{\rho^2}\left(\displaystyle\frac{\partial u}{\partial \theta}\right)^2 $$
> > $\displaystyle\frac{\partial^2 u}{\partial x^2}$展开：
> > $$ \begin{aligned}
> > \displaystyle\frac{\partial^2 u}{\partial x^2} &= \displaystyle\frac{\partial^2 u}{\partial \rho^2}\cos^2\theta - \displaystyle\frac{\partial^2 u}{\partial \rho \partial \theta}\sin 2\theta + \displaystyle\frac{\partial^2 u}{\partial \theta^2}\displaystyle\frac{\sin^2\theta}{\rho^2} \\
> > &\quad + \displaystyle\frac{\partial u}{\partial \theta}\displaystyle\frac{\sin 2\theta}{\rho^2} + \displaystyle\frac{\partial u}{\partial \rho}\displaystyle\frac{\sin^2\theta}{\rho}
> > \end{aligned} $$
> > $\displaystyle\frac{\partial^2 u}{\partial y^2}$展开：
> > $$ \begin{aligned}
> > \displaystyle\frac{\partial^2 u}{\partial y^2} &= \displaystyle\frac{\partial^2 u}{\partial \rho^2}\sin^2\theta + \displaystyle\frac{\partial^2 u}{\partial \rho \partial \theta}\sin 2\theta + \displaystyle\frac{\partial^2 u}{\partial \theta^2}\displaystyle\frac{\cos^2\theta}{\rho^2} \\
> > &\quad - \displaystyle\frac{\partial u}{\partial \theta}\displaystyle\frac{\sin 2\theta}{\rho^2} + \displaystyle\frac{\partial u}{\partial \rho}\displaystyle\frac{\cos^2\theta}{\rho}
> > \end{aligned} $$
> > 两式相加后化简得极坐标下的拉普拉斯算子：
> > $$ \displaystyle\frac{\partial^2 u}{\partial x^2} + \displaystyle\frac{\partial^2 u}{\partial y^2} = { \displaystyle\frac{\partial^2 u}{\partial \rho^2} + \displaystyle\frac{1}{\rho}\displaystyle\frac{\partial u}{\partial \rho} + \displaystyle\frac{1}{\rho^2}\displaystyle\frac{\partial^2 u}{\partial \theta^2} } $$
> >或等价表示为：
> > $$ { \displaystyle\frac{1}{\rho}\displaystyle\frac{\partial}{\partial \rho}\left(\rho \displaystyle\frac{\partial u}{\partial \rho}\right) + \displaystyle\frac{1}{\rho^2}\displaystyle\frac{\partial^2 u}{\partial \theta^2} } $$


[回到主页面](index.html)