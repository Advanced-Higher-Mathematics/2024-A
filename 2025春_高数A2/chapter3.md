---
title: 高等数学讲义(下)
author: 胡煜成
description: 首都师范大学2025春季学期高等数学A
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,讲义
vlook-chp-autonum: h1{{第 ### 节 }},h3{{### }}
vlook-query: vdl=on
vlook-query: ws=off
---


[回到主页面](index.html)

# 重积分

> [!tip]
> 在单变量积分中，我们通过定积分研究了一个变量在区间上的累积问题，例如曲线下的面积、物体的位移等。然而，现实世界中的许多问题涉及多个变量的相互作用，例如：三维空间中不均匀物体的质量（质量密度随位置变化），平面区域上的温度分布平均值等。这些问题要求我们将积分的概念从一维推广到高维空间。重积分（Multiple Integrals）正是解决这类问题的核心工具。本章将系统学习二重积分（Double Integrals）与三重积分（Triple Integrals）的定义、计算方法及其应用。 

## 二重积分

> [!tip]
> 跟单变量积分一样, 二重积分的本质仍然是“分割-近似-求和”的极限过程. 


### 二重积分的概念

> [!tip]
>
> ==回顾: 单变量积分==
> 我们要计算曲线 $ y = f(x) $在区间 $\left[ a, b\right]$下的面积，可以通过以下步骤实现：
> 将区间 $\left [a, b \right]$等分为 $ N $个子区间，每个子区间的宽度为 $\displaystyle  \Delta x = \frac{b-a}{N} $。通过分割得到 $ N $个窄矩形（小柱体），每个矩形的左端点或右端点记为 $ x_i $（例如 $ x_i = a + i\Delta x $）.每个窄矩形的面积可近似为底边长度 $ \Delta x $乘以高度 $ f(x_i) $，即第 $ i $个矩形的面积为 $ \Delta x \cdot f(x_i) $.将所有窄矩形的面积相加，得到总面积 $ S_N $的近似值：
> $$
> \displaystyle S_N = \sum_{i=1}^N \Delta x \cdot f(x_i)
> $$
> 当 $ N \to \infty $（即子区间宽度 $ \Delta x \to 0 $）时，近似值 $ S_N $趋近于精确面积 $ S $：
> $$
> \displaystyle S = \lim_{N \to \infty} S_N = \lim_{\Delta x \to 0} S_N
> $$
> 最终，面积 $ S $可表示为定积分：
> $$
> S = \int_{a}^{b} f(x) \, \mathrm{d}x
> $$


> [!important]
> 
> ==多变量积分==
> 
> [图略，待补充]
> 如图所示，对于定义在平面区域 $D$ 上的函数 $z = f(x,y)$，若要计算其对应的体积或物理量（如质量、电荷量等），其思想是单变量积分在二维空间的自然推广.首先将积分区域 $D$ 分割为 $N$ 个面积微元 $\Delta A$，每个微元可近似视为一个小矩形区域，并选取其代表点 $(x_i, y_i)$（例如取中心点或顶点坐标）.每个微元的体积可近似为底面积 $\Delta A$ 乘以高度 $f(x_i, y_i)$，即 $\Delta A \cdot f(x_i, y_i)$.将所有微元的贡献叠加，得到近似总体积：
> $$
> \displaystyle V_N = \sum_{i=1}^N \Delta A \cdot f(x_i, y_i)
> $$
> 当分割无限细化（即 $N \to \infty$，且每个微元面积 $\Delta A \to 0$）时，近似值趋于精确值：
> $$
> \displaystyle V = \lim_{N \to \infty} V_N = \lim_{\Delta A \to 0}V_N
> $$
> 这一极限过程即为二重积分的定义，可表示为：
> $$
> V = \iint_{D} f(x,y) \, \mathrm{d}A
> $$
> 其中 $D$ 是积分区域，$f(x,y)$ 为被积函数，$\mathrm{d}A$ 为面积元（直角坐标系中通常写作 $\mathrm{d}x\mathrm{d}y$）.
> 
> ==如何计算？==
> [图略，待补充]
> $$
> \displaystyle M=\sum_{i=1}^N \rho (x_i,y_i)\mathrm{d}A_i=\iint_D \rho(x,y)\mathrm{d}A
> $$

### 二重积分的计算

> [!note]
> 
> > **例1:已知$f(x,y)=1-x^2-y^2,D=\{(x,y)|0\leq x\leq 1,0\leq y\leq 1\}$,计算$\displaystyle \iint_D f(x,y) \mathrm{d}A$.**
> >
> > **解：**上式可展开为
> > $$
> \begin{aligned}
> \iint_D f(x,y) \mathrm{d}A &=\iint_Df(x,y)\mathrm{d}x\mathrm{d}y\\
> &=\int_0^1\int_0^1(1-x^2-y^2)\mathrm{d}x\mathrm{d}y\\
> &=\int_0^1\left[\int_0^1(1-x^2-y^2)\mathrm{d}x\right]\mathrm{d}y
> \end{aligned}
> > $$
> > Inner:
> > $$
> \int_0^1(1-x^2-y^2)\mathrm{d}x=\left[x-\frac{1}{3}x^3-y^2x\right]_0^1=\frac{2}{3}-y^2
> >$$
> > Outer:
> > $$
> \int_0^1\left(\frac{2}{3}-y^2\right)\mathrm{d}y=\left[\frac{2}{3}y-\frac{1}{3}y^3\right]_0^1=\frac{1}{3}
> > $$
> > 同理
> > $$
\begin{aligned}
\int_0^1\left[\int_0^1(1-x^2-y^2)\mathrm{d}x\right]\mathrm{d}y &= \int_0^1\left[\int_0^1(1-x^2-y^2)\mathrm{d}y\right]\mathrm{d}x \\
&=\int_0^1\left(\left[y-\frac{1}{3}y^3-x^2y\right]_0^1\right)\mathrm{d}x\\
&= \int_0^1\left(\frac{2}{3}-x^2\right)\mathrm{d}x \\
&= \left[\frac{2}{3}x-\frac{1}{3}x^3\right]_0^1 \\
&=\frac{1}{3}
\end{aligned}
> > $$
>
>
> > **例2：已知$f(x,y)=1-x^2-y^2,D=\{(x,y)|x^2+y^2\leq 1,x> 0,y > 0 \} $,计算$\displaystyle \iint_D f(x,y) \mathrm{d}A$.**
> >
> > **解：**由图
> > [图略，待补充]
> > $$
> \iint_D f(x,y) \mathrm{d}A=\int_0^1\left[\int_0^{\sqrt{1-x^2}}(1-x^2-y^2)\mathrm{d}y\right]\mathrm{d}x
> > $$
> > Inner:
> > $$
> \begin{aligned}
> \int_0^{\sqrt{1-x^2}}(1-x^2-y^2)\mathrm{d}y&=\left[y-x^2y-\frac{1}{3}y^3\right]_0^{\sqrt{1-x^2}} \\
> &= \sqrt{1-x^2}-x^2\sqrt{1-x^2}-\frac{1}{3}(1-x^2)^{\frac{3}{2}} \\
> &=\sqrt{1-x^2}\left(1-x^2-\frac{1}{3}(1-x^2)\right) \\
> &= \sqrt{1-x^2}\left(\frac{2}{3}-\frac{2}{3}x^2\right)\\
> &= \frac{2}{3}(1-x^2)^{\frac{3}{2}}
> \end{aligned}
> > $$
> > Outer:$\displaystyle \int_0^1\frac{2}{3}(1-x^2)^{\frac{3}{2}}\mathrm{d}x$
> > 令$x=\sin\theta,\mathrm{d}x=\cos\theta\mathrm{d}\theta$
> > $$
> \begin{aligned}
> \int_0^1\frac{2}{3}(1-x^2)^{\frac{3}{2}}\mathrm{d}x &= \int_0^{\frac{\pi}{2}}\frac{2}{3}\cos^4\theta\mathrm{d}\theta \\
> &=\frac{3}{2}\int_0^{\frac{\pi}{2}} \left( \frac{1+\cos2\theta}{2}\right)^2\mathrm{d}\theta \\
> &=\frac{3}{2}\int_0^{\frac{\pi}{2}}\left(\frac{1}{4}+\frac{1}{2}\cos2\theta + \frac{1}{4}\cos^22\theta\right)\mathrm{d}\theta \\
> &= \frac{3}{2}\left(\left[\frac{\theta}{4}\right]_0^{\frac{\pi}{2}}+\left[\frac{\sin2\theta}{4}\right]_0^{\frac{\pi}{2}}+\frac{1}{4}\int_0^{\frac{\pi}{2}}\left(\frac{1+\cos4\theta}{2}\right)^2\mathrm{d}\theta \right)\\
> &= \frac{3}{2}\left(\frac{\pi}{8}+\frac{\pi}{16}+\frac{1}{8}\cdot \frac{1}{4}\left[ \sin4\theta \right]_0^{\frac{\pi}{2}}\right) \\
> &= \frac{\pi}{8}
> \end{aligned}
> > $$

> [!note]
>
> - ==重积分可交换顺序？==
> 一般可以，注意上下限
>
> > **例1：计算$\displaystyle \iint_{D} xy \mathrm{d}x\mathrm{d}y$,其中积分区域 $ D $ 由直线 $ y = 1 $、$ x = 2 $ 及 $ y = x $ 围成.**
> > 
> > **解法一：**由图
> >  [图略，待补充]
> > $$
> \begin{aligned}
> \iint_{D} xy \mathrm{d}x\mathrm{d}y &= \int_{1}^{2} \left[ \int_{1}^{x} xy \mathrm{d}y \right]\mathrm{d}x \\
> &= \int_1^2\left(\left[\frac{1}{2}xy^2\right]_1^x\right)\mathrm{d}x \\
> &= \int_1^2\left(\frac{x^3}{2} - \frac{x}{2}\right)\mathrm{d}x \\
> &= \left[ \frac{x^4}{8} - \frac{x^2}{4} \right]_{1}^{2}\\
> &= 1+\frac{1}{8}\\
> &= \frac{9}{8}
> \end{aligned}
> > $$
> > 
> > **解法二：**由图
> >   [图略，待补充]
> > $$
> \begin{aligned}
> \iint_{D} xy \mathrm{d}x\mathrm{d}y &= \int_{1}^{2} \left[ \int_{y}^{2} xy \mathrm{d}x \right] \mathrm{d}y\\
> &=\int_{1}^{2}\left[\frac{1}{2}x^2y\right]_y^2\mathrm{d}y\\
> &= \int_{1}^{2}\left(2y - \frac{y^3}{2}\right)\mathrm{d}y\\
> &=\left[ y^2 - \frac{y^4}{8} \right]_{1}^{2}\\
> &= 2-\left(1-\frac{1}{8}\right)\\
> &=\frac{9}{8}
> \end{aligned}
> >$$
>
> > **例2：计算$\displaystyle \iint_{D} y\sqrt{1+x^2 - y^2} \mathrm{d}\sigma$,其中$ D $ 由直线 $ y = x $、$ x = -1 $ 及 $ y = 1 $ 围成的闭区域.**
> > 
> > **解法一：**由图
> > [图略，待补充]
> > $$
> \begin{aligned}
> \iint_{D} y\sqrt{1+x^2 - y^2} \mathrm{d}x\mathrm{d}y &= \int_{-1}^1\mathrm{d}x\int_x^1 y\sqrt{1+x^2 - y^2} \mathrm{d}y \\
> &= \int_{-1}^1 \left[\left[-\frac{1}{3}(1+x^2-y^2)^{\frac{3}{2}}\right]_x^1\right] \mathrm{d}x\\
> &=\int_{-1}^1\frac{1}{3}(1-|x|^3)\mathrm{d}x \\
> &= \frac{2}{3}\int_0^1(1-x^3)\mathrm{d}x \\
> &= \frac{1}{2}
> \end{aligned}
> > $$
> > **解法二：**由图
> > [图略，待补充]
> > $$
> \iint_{D} y\sqrt{1+x^2 - y^2} \mathrm{d}\sigma=\int_{-1}^1 y\left[\int_{-1}^y\sqrt{1+x^2 - y^2} \mathrm{d}x\right]\mathrm{d}y
> > $$

> [!note]
> 
> ==极坐标下的积分==
> 
> > **例：已知$f(x,y)=1-x^2-y^2,D= \{(x,y)|x^2+y^2\leq 1,x\geq 0,y\geq 0 \} $,计算$\displaystyle \iint_D f(x,y) \mathrm{d}A$.**
> > 
> >**解:**由图
> > [图略，待补充]
> > 由于
> > $$
> > \mathrm{d}A=\mathrm{d}x\mathrm{d}y=r\mathrm{d}\theta\mathrm{d}r
> > $$
> >$$
> > \begin{aligned}
> > \iint_D (1-x^2-y^2)\mathrm{d}x\mathrm{d}y &=\iint_D (1-x^2-y^2)r\mathrm{d}r\mathrm{d}\theta\\
&=\iint_D(1-r^2)r\mathrm{d}r\mathrm{d}\theta\\
&= \int_0^{\frac{\pi}{2}}\left[\int_0^1(1-r^2)r\mathrm{d}r\right]\mathrm{d}\theta \\
&= \frac{\pi}{2}\left[\frac{1}{2}r^2-\frac{1}{4}r^4\right]_0^1 \\
&= \frac{\pi}{8}
\end{aligned}
$$

### 重积分的应用

> [!important]
>
> ==质量==
>
> 对于分布在平面区域 $ D $上的物体（如薄片），若其密度函数为 $ \rho(x,y) $，则总质量可通过二重积分计算：
> $$
> M = \iint_D \rho(x,y) \, \mathrm{d}\sigma
> $$
> 其中 $ \mathrm{d}\sigma $表示面积元（即直角坐标系中的 $ \mathrm{d}x\mathrm{d}y $）.当密度均匀时（$ \rho $为常数），总质量退化为密度与面积的乘积 $ M = \rho \cdot A $，其中 $\displaystyle  A = \iint_D \mathrm{d}\sigma $为区域 $ D $的面积.
>
> ==质心==
>
> 质心是物体质量分布的加权平均位置.对于离散质点系，质心坐标 $ (\bar{x}, \bar{y}) $定义为：
> $$
> \displaystyle \bar{x} = \frac{\sum_{i=1}^n m_i x_i}{\sum_{i=1}^n m_i}, \quad \bar{y} = \frac{\sum_{i=1}^n m_i y_i}{\sum_{i=1}^n m_i}
> $$
> 将其推广到连续情形，则质心坐标通过二重积分表达。当密度函数为 $ \mu(x,y) $时：
> $$
> \displaystyle \bar{x} = \frac{\iint_D x \mu(x,y) \, \mathrm{d}\sigma}{\iint_D \mu(x,y) \, \mathrm{d}\sigma}, \quad \bar{y} = \frac{\iint_D y \mu(x,y) \, \mathrm{d}\sigma}{\iint_D \mu(x,y) \, \mathrm{d}\sigma}
> $$

>[!note]
>
> > **例1:如图所示，求$\displaystyle I=\iint_Dr^2(\rho,\theta)\rho \mathrm{d}\rho \mathrm{d}\theta$.**
> > 
> > [图略，待补充]
> > **解:**
> >  $$
> \begin{aligned}
> I&=\iint_Dr^2(\rho,\theta)\rho \mathrm{d}\rho \mathrm{d}\theta \\ 
> &= \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\int_0^{2\cos\theta}\rho^3\mathrm{d}\rho \mathrm{d}\theta \\ 
> &=\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\left[\frac{1}{4}\rho^4\right]_0^{2\cos\theta}\mathrm{d}\theta \\ 
> &=\int_0^{\frac{\pi}{2}}4\cos^4\theta \mathrm{d}\theta \\
> &=\frac{3}{2}\pi
> \end{aligned}
> >  $$
> 
> > **例2:如图所示，求$\displaystyle  I=\iint_Dr^2(\rho,\theta)\rho \mathrm{d}\rho \mathrm{d}\theta$.**
> > 
> > [图略，待补充]
> > **解法一：**
> > $$
> \begin{aligned}
> I&=\iint_Dr^2(\rho,\theta)\rho \mathrm{d}\rho \mathrm{d}\theta\\
> &= \int_{-\frac{\pi}{2}}^{\frac{\pi}{2}}\int_0^{2\cos\theta}(1+\rho^2-2\rho \cos\theta)\rho \mathrm{d}\rho \mathrm{d}\theta \\
> &=\frac{\pi}{2}
> \end{aligned}
> > $$
> > **解法二:**
> > $$
> I=\int_0^{2\pi}\int_0^1\rho^2\cdot \rho\mathrm{d}\rho \mathrm{d}\theta=\frac{\pi}{2}
> > $$


> [!warning]
> 
> ==转动惯量与质心的关系(不要求)==
> 
> 对于平面区域 $ D $上的质量分布，若密度函数为 $ \mu(x,y) $，则系统对某点 $ (x_0, y_0) $的转动惯量为：
> $$
> I(x_0, y_0) = \iint_D \mu(x,y) \left[ (x-x_0)^2 + (y-y_0)^2 \right] \mathrm{d}x\mathrm{d}y
> $$
> 此式可视为质量元 $ \mu(x,y)\mathrm{d}x\mathrm{d}y $到参考点距离平方的加权积分.特别地，当参考点为原点时，转动惯量简化为：
> $$
> I = \iint_D \mu(x,y) r^2(x,y) \mathrm{d}x\mathrm{d}y \quad (r^2 = x^2 + y^2)
> $$
> 
> **质心的极值特性**:  
> 质心具有重要物理性质：它是使系统转动惯量取极小值的位置.为证明这一点，对 $ I(x_0, y_0) $分别关于 $ x_0, y_0 $求偏导并令其为零：
> $$
> \frac{\partial I}{\partial x_0} = \iint_D 2\mu(x,y)(x_0 - x)\mathrm{d}x\mathrm{d}y = 0 \\
> \frac{\partial I}{\partial y_0} = \iint_D 2\mu(x,y)(y_0 - y)\mathrm{d}x\mathrm{d}y = 0
> $$
> 由此可得方程组：
> $$
> x_0 \iint_D \mu\mathrm{d}x\mathrm{d}y = \iint_D \mu x\mathrm{d}x\mathrm{d}y \\
> y_0 \iint_D \mu\mathrm{d}x\mathrm{d}y = \iint_D \mu y\mathrm{d}x\mathrm{d}y
> $$
> 最终解得质心坐标为：
> $$
> \displaystyle x_0 = \frac{\iint_D \mu x\mathrm{d}x\mathrm{d}y}{\iint_D \mu\mathrm{d}x\mathrm{d}y}, \quad 
> y_0 = \frac{\iint_D \mu y\mathrm{d}x\mathrm{d}y}{\iint_D \mu\mathrm{d}x\mathrm{d}y}
> $$
> 这与离散质点系的质心公式一致：
> $$
> \displaystyle \begin{cases}
> x_0 = \frac{\sum m_i x_i}{\sum m_i} & \text{（质量加权平均）} \\
> y_0 = \frac{\sum m_i y_i}{\sum m_i} & \text{（质量加权平均）}
> \end{cases}
> $$


> [!warning]
> 
> ==平行轴定理==
> 
> 平行轴定理揭示了物体绕不同轴转动惯量之间的关系：**绕任意轴的转动惯量等于绕质心轴的转动惯量加上总质量与该轴到质心距离平方的乘积**。其数学推导可通过二重积分展开：
> 
> 设质心坐标为 $ (x_c, y_c) $，绕点 $ (x_0, y_0) $ 的转动惯量为：
> $$
> \begin{aligned}
> I(x_0,y_0) &= \iint_D \mu \left[ (x-x_0)^2 + (y-y_0)^2 \right] \mathrm{d}x\mathrm{d}y \\
> &= \iint_D \mu \left[ (x-x_c + x_c - x_0)^2 + (y-y_c + y_c - y_0)^2 \right] \mathrm{d}x\mathrm{d}y 
> \end{aligned}
> $$
> 
> 展开平方项并重组积分：
> $$
> \begin{aligned}
> &= \underbrace{\iint_D \mu \left[ (x-x_c)^2 + (y-y_c)^2 \right] \mathrm{d}x\mathrm{d}y}_{I_c \ (\text{绕质心的转动惯量})} \\
> &\quad + \underbrace{\iint_D \mu \left[ (x_c - x_0)^2 + (y_c - y_0)^2 \right] \mathrm{d}x\mathrm{d}y}_{M r^2 \ (\text{总质量} \times \text{距离平方})} \\
> &\quad + 2(x_c - x_0)\underbrace{\iint_D \mu (x - x_c) \mathrm{d}x\mathrm{d}y}_{0 \ (\text{质心定义})} \\
> &\quad + 2(y_c - y_0)\underbrace{\iint_D \mu (y - y_c) \mathrm{d}x\mathrm{d}y}_{0 \ (\text{质心定义})}
> \end{aligned}
> $$
> 
> 关键消去项：根据质心坐标的定义 $ \displaystyle  x_c = \frac{1}{M}\iint_D \mu x \mathrm{d}x\mathrm{d}y $，交叉项中的积分 $ \displaystyle \iint_D \mu(x - x_c)\mathrm{d}x\mathrm{d}y $ 和 $\displaystyle  \iint_D \mu(y - y_c)\mathrm{d}x\mathrm{d}y $ 必然为零。最终得到简洁形式：
> $$
> I(x_0, y_0) = I_c + M r^2
> $$
> 其中 $ r = \sqrt{(x_c - x_0)^2 + (y_c - y_0)^2} $ 为两轴间距离，$ \displaystyle M = \iint_D \mu \mathrm{d}x\mathrm{d}y $ 为总质量.





>[!note]
>
> > **例3:求球体 $ x^2 + y^2 + z^2 \leq 4a^2 $ 被圆柱面 $ x^2 + y^2 = 2ax $ ($ a > 0 $) 截得的含在圆柱面内的立体体积.**
> > 
> > [图略，待补充]
> >  **解:**
> >  $$
> \begin{aligned}
> V&= 4 \iint_{D} \sqrt{4a^2 - x^2 - y^2}\mathrm{d}x\mathrm{d}y \\
> &=4\int_0^{\frac{\pi}{2}}\int_0^{2a\cos\theta}\sqrt{4a^2 - \rho^2 }\rho \mathrm{d}\rho \mathrm{d}\theta \\
> &=4\int_0^{\frac{\pi}{2}}\frac{8}{3}a^3(1-\sin^3\theta) \mathrm{d}\theta \\ 
> &= \frac{16}{3}a^3\pi-\frac{8}{3}\cdot\frac{8}{3}a^3 \\
> &= \frac{32}{3}a^3\left(\frac{\pi}{2}-\frac{2}{3}\right)
> \end{aligned}
> >  $$

> [!note]
> ==换元法==
> $$
(x,y) \to (u,v)
> $$
> 
> > **例1(椭圆面积):已知$\displaystyle  \frac{x^2}{a^2}+\frac{y^2}{b^2}=1$，求$\displaystyle  \iint_D\mathrm{d}x\mathrm{d}y$.**
> > 
> > **解法一:**
> > [图略，待补充]
> > $$
\begin{aligned}
\iint_D\mathrm{d}x\mathrm{d}y &= 4\int_0^a\int_0^{b\sqrt{1-\frac{x^2}{a^2}}}\mathrm{d}y\mathrm{d}x \\
&=4\int_0^ab\sqrt{1-\frac{x^2}{a^2}}\mathrm{d}y
\end{aligned}
> > $$
> > 令$y=a\sin\theta,\mathrm{d}y=a\cos\theta\mathrm{d}\theta$,则
> > $$
原式=4\int_0^{\frac{\pi}{2}}b\cos\theta a \cos\theta\mathrm{d}\theta=4ab\int_0^{\frac{\pi}{2}}\frac{1+\cos2\theta}{2}\mathrm{d}\theta=\pi ab
> > $$
> > **解法二**:
> > 令$x=au,y=bv,-1\leq u \leq 1,-1\leq v \leq 1,u^2+v^2=1$，则
> > $$
\mathrm{d}x=a\mathrm{d}u \\ \mathrm{d}y=b\mathrm{d}v \\ \mathrm{d}x\mathrm{d}y=a\mathrm{d}u  \cdot b\mathrm{d}v
> > $$
> > $$
\iint_D\mathrm{d}x\mathrm{d}y= \iint_Dab\mathrm{d}u\mathrm{d}v=\pi ab
> > $$



> [!important]
> 
> ==变量替换与雅可比行列式==
> 
> 考虑坐标变换 $ \begin{cases} u = u(x,y) \\ v = v(x,y) \end{cases} $，其全微分形式可表示为：
> $$
> \begin{cases} 
> \mathrm{d}u = \frac{\partial u}{\partial x}\mathrm{d}x + \frac{\partial u}{\partial y}\mathrm{d}y \\ 
> \mathrm{d}v = \frac{\partial v}{\partial x}\mathrm{d}x + \frac{\partial v}{\partial y}\mathrm{d}y 
> \end{cases}
> $$
> 该微分系统可写成矩阵形式：
> $$
> \begin{bmatrix}
> \mathrm{d}u \\
> \mathrm{d}v
> \end{bmatrix} = 
> \begin{bmatrix}
> \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
> \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
> \end{bmatrix}
> \begin{bmatrix}
> \mathrm{d}x \\
> \mathrm{d}y
> \end{bmatrix}
> $$
> [图略，待补充]
> $$
\mathrm{d}u\mathrm{d}v = J= \frac{\partial (u,v)}{\partial (x,y)}=
\begin{vmatrix}
\frac{\partial u}{\partial x}\mathrm{d}x & \frac{\partial u}{\partial y}\mathrm{d}y\\
\frac{\partial v}{\partial x}\mathrm{d}x & \frac{\partial v}{\partial y}\mathrm{d}y
\end{vmatrix}=\left|\frac{\partial u}{\partial x}\frac{\partial v}{\partial y}-\frac{\partial u}{\partial y}\frac{\partial v}{\partial x}\right|\mathrm{d}x\mathrm{d}y
> $$



>[!note]
>
> > **例2:已知$\begin{cases}u=3x-2y\\v=x+y\end{cases}$**
> > 
> > [图略，待补充]
> >  **解:**
> >  方法一：
> >  $$
|\mathbf{\omega_1}\times\mathbf{\omega_2}|=|\mathbf{\omega_1}|\cdot |\mathbf{\omega_2}|\cdot \sin\theta=
\begin{vmatrix}
3 & -2\\
1 & 1
\end{vmatrix}=5
> >  $$
> >  方法二：
> >  $$
J=
\begin{vmatrix}
\frac{\partial u}{\partial x} & \frac{\partial u}{\partial y}\\
\frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
\end{vmatrix}=
\begin{vmatrix}
3 & -2\\
1 & 1
\end{vmatrix}=5
> >  $$
> >  则
> >  $$
\mathrm{d}u\mathrm{d}v=\frac{\partial (u,v)}{\partial (x,y)}\mathrm{d}x\mathrm{d}y=5\mathrm{d}x\mathrm{d}y
> >  $$
> >  $$
\iint_D\mathrm{d}x\mathrm{d}y=\iint_D\frac{1}{5}\mathrm{d}u\mathrm{d}v
> >  $$


> [!important]
>
> ==雅可比行列式与坐标变换的深层关系==
>
> 在坐标变换 $ (x,y) \leftrightarrow (u,v) $ 中，雅可比行列式不仅描述面积元的缩放比例，更揭示了双向变换的对称性。由基本关系：
> $$
> \mathrm{d}u\mathrm{d}v=\left|J\right|\mathrm{d}x\mathrm{d}y=\left|\frac{\partial (u,v)}{\partial (x,y)}\right|\mathrm{d}x\mathrm{d}y
> $$
> 通过反函数定理，可得逆变换关系：
> $$
> \mathrm{d}x\mathrm{d}y=\left|\frac{\partial (x,y)}{\partial (u,v)}\right|\mathrm{d}u\mathrm{d}v
> $$
> 这建立了双向变换的精确对应：雅可比行列式互为倒数，即：
> $$
> \left| \frac{\partial (x,y)}{\partial (u,v)} \right| = \left| \frac{\partial (u,v)}{\partial (x,y)} \right|^{-1}
> $$
> **经典示例：极坐标变换**  
> 对极坐标变换 $ \begin{cases} x = \rho \cos\theta \\ y = \rho \sin\theta \end{cases} $，其雅可比矩阵为：
> $$
> J(\rho ,\theta)=\frac{\partial (x,y)}{\partial (\rho ,\theta)}=
> \begin{vmatrix}
> \frac{\partial x}{\partial \rho } & \frac{\partial x}{\partial \theta}\\
> \frac{\partial y}{\partial \rho } & \frac{\partial y}{\partial \theta}
> \end{vmatrix}=
> \begin{vmatrix}
> \cos\theta & -\rho \sin\theta\\
> \sin\theta & \rho \cos\theta
> \end{vmatrix} = \rho
> $$
> 因此面积元变换为：
>$$
> \mathrm{d}x\mathrm{d}y = \left|\rho\right| \mathrm{d}\rho\mathrm{d}\theta = \rho \mathrm{d}\rho\mathrm{d}\theta \quad
>$$
> **矩阵互逆性的几何诠释**  
> 变换矩阵的互逆性直接体现在坐标系转换中：
> $$
> \begin{bmatrix}
> \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
> \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
> \end{bmatrix}
> 与
> \begin{bmatrix}
> \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
> \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
> \end{bmatrix}
> $$
> 这两个雅可比矩阵的乘积为单位矩阵，其行列式乘积为1。例如当 $ J_{uv} = 5 $ 时，逆变换的行列式为 $\displaystyle  \frac{1}{5} $，此时：
> $$
> \mathrm{d}x\mathrm{d}y = \frac{1}{5} \mathrm{d}u\mathrm{d}v
> $$
> 这种精确的倒数关系确保了积分在不同坐标系下计算结果的一致性，是多重积分变量替换定理的核心数学基础。



>[!note]
>
> > **例:计算$\displaystyle  \int_{-\infty}^{+\infty}e^{-x^2}\mathrm{d}x$.**
> >
> >  **解:**
> >  令$\displaystyle  I=\int_{-\infty}^{+\infty}e^{-x^2}\mathrm{d}x$
> >  则
> >  $$
I^2=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}e^{-(x^2+y^2)}\mathrm{d}x\mathrm{d}y=\int_{-\infty}^{+\infty}e^{-y^2}\mathrm{d}y\int_{-\infty}^{+\infty}e^{-x^2}\mathrm{d}x
> >  $$
> >  令$x=r\cos\theta,y=r\sin\theta$，则
> >  $$
\begin{aligned}
I^2 &=\int_0^{2\pi}\int_0^{+\infty}e^{-r^2}r\mathrm{d}r\mathrm{d}\theta \\ 
&=\int_0^{2\pi}\mathrm{d}\theta\left(\frac{1}{2}\int_0^{+\infty}e^{-r^2}\mathrm{d}r^2 \right)\\
&=\frac{1}{2}\int_0^{2\pi}\left[(-e^{-r^2})\right]_0^{+\infty}\mathrm{d}\theta \\
&= \pi
\end{aligned}
> > $$
> >  故
> > $$
\int_{-\infty}^{+\infty}e^{-x^2}\mathrm{d}x = I=\sqrt{\pi}
> >  $$

## 三重积分

>[!note]
>
> > **例1:计算$\displaystyle  \iiint_{\Omega}x\mathrm{d}x\mathrm{d}y\mathrm{d}z$,其中 $\Omega$ 由平面 $x + 2y + z = 1$ 与三个坐标平面 ($x=0$, $y=0$, $z=0$) 围成.**
> > 
> > [图略，待补充]
> >  **解法一:**
> >  $$
\begin{aligned}
\iiint_{\Omega}x\mathrm{d}x\mathrm{d}y\mathrm{d}z 
&=\int_0^1\mathrm{d}z\int_0^{\frac{1}{2}(1-z)}\mathrm{d}y\int_0^{1-2y-z}x\mathrm{d}x \\
&=\int_0^1\mathrm{d}z\int_0^{\frac{1}{2}(1-z)}\frac{1}{2}(1-2y-z)^2\mathrm{d}y \\
&= \frac{1}{2} \int_{0}^{1} \left[ -\frac{(1 - 2y - z)^3}{6} \right]_{0}^{\frac{1}{2}(1 - z)} \mathrm{d}z \\
&= \frac{1}{12} \int_{0}^{1} (1 - z)^3 \, \mathrm{d}z \\
&= \frac{1}{12} \left[ -\frac{(1 - z)^4}{4} \right]_{0}^{1} \\
&= \frac{1}{48}.
\end{aligned}
> >  $$
> >  **解法二:**
> >  $$
\begin{aligned}
\iiint_{\Omega}x\mathrm{d}x\mathrm{d}y\mathrm{d}z
&=\int_0^1\mathrm{d}x\int_0^{\frac{1}{2}(1-x)}\mathrm{d}y\int_0^{1-x-2y} x \mathrm{d}z \\
&=\int_0^1x\mathrm{d}x\int_0^{\frac{1}{2}(1-x)}(1-x-2y)\mathrm{d}y \\ 
&=\int_0^1\frac{1}{4}x(1-x)^2\mathrm{d}x \\
&= \frac{1}{48}
\end{aligned} 
> >  $$
> 
> > **例2:利用柱面坐标计算三重积分 $\displaystyle  \iiint_{\Omega} z \mathrm{d}x\mathrm{d}y\mathrm{d}z$,其中$\Omega$ 是由曲面 $z = x^2 + y^2$ 与平面 $z = 4$ 围成的闭区域.**
> > 
> > [图略，待补充]
> >  **解:**令
> > $$
\begin{cases}
x=\rho \cos\theta \\
y=\rho \sin\theta \\
z=z
\end{cases}
> >  $$
> >  则
> >  $$
\mathrm{d}V=\mathrm{d}x\mathrm{d}y\mathrm{d}z=\rho\mathrm{d}\rho\mathrm{d}\theta\mathrm{d}z
> >  $$
> >  $$
\begin{aligned}
\iiint_{\Omega} z \mathrm{d}x\mathrm{d}y\mathrm{d}z
&=\iiint_{\Omega} z \rho\mathrm{d}\rho\mathrm{d}\theta\mathrm{d}z \\ 
&=\int_0^4\mathrm{d}z\int_0^{2\pi}\mathrm{d}\theta\int_0^{\sqrt{z}} z \rho \mathrm{d}\rho \\
&=\int_0^4\mathrm{d}z\int_0^{2\pi}\frac{1}{2}z^2\mathrm{d}\theta \\
&=\int_0^4 z^2\pi \mathrm{d}z \\
&=\frac{1}{3}\pi \left[z^3\right]_0^4 \\
&=\frac{64}{3}\pi
\end{aligned}
> >  $$




[回到主页面](index.html)