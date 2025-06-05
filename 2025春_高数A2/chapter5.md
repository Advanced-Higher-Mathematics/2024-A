---
title: 高等数学讲义(下)
author: 胡煜成
description: 首都师范大学2025秋季学期高等数学A
"og:description": 浏览器版和手机版
"og:image": https://vlook-doc.pages.dev/pic/vlook-og.png
keywords:
- 高等数学,微积分,讲义
vlook-chp-autonum: h1{{第 ### 节 }},h3{{### }}
vlook-query: vdl=on
vlook-query: ws=off
---

[回到主页面](index.html)


# 无穷级数

> [!tip]
> 本章的内容主要包括**常数项级数的收敛性**和**函数的级数展开**. 对**常数项级数**的研究可以追溯到古人对极限过程的早期理解. 而**函数项级数**则是分析学中一项极其重要的工具, 函数项级数蕴含了深层次的数学思想, 即用简单的无穷多项的和来表示一个复杂的对象.


## 常数项级数的概念和性质


> [!note]
>
> ==常数项级数的直观例子==
> 
>---
> > **例:一尺之杠, 日取其半**
> >
> > **解:**每次拿在手里的长度为
> > $$
> \begin{aligned}
> & S_1=\frac{1}{2} \\
> & S_2=\frac{1}{2}+\frac{1}{4}=\frac{3}{4} \\
> & S_3=\frac{1}{2}+\frac{1}{4}+\frac{1}{8}=\frac{7}{8} \\
> & \cdots \\
> & S_n=\frac{1}{2}+\frac{1}{4}+\cdots+\frac{1}{2^n}=\frac{\frac{1}{2}\left(1-\left(\frac{1}{2}\right)^n\right)}{1-\frac{1}{2}}=1-\frac{1}{2^2} \\
> & \lim _{n \rightarrow \infty} S_n=1
> \end{aligned}
> > $$
>
>
> > ==例2：割圆法与圆面积==
> 




> [!important]
> 
> ==级数的定义==
> 
> $ \displaystyle a_n=\frac{1}{2^n}, ~ S_n=\sum_{i}^{\ n} a_n \quad n \rightarrow \infty$ ，称为$a_n$的无穷级数，简称级数.
>
> ==级数收敛==
> 
>如果 $\left\{S_n\right\}$ 有极限$S$，记作 $\displaystyle\lim _{n \rightarrow \infty} S_n=S$ ，则称级数收敛于$S$.

>[!note]
>
> >**例1: 计算等比数列$S_n=\sum_{i=2}^{\ n} a q^i, a \neq 0$**
> >
> >**解:** 如果 $q \ne 1$，那么部分和  
> >$$
>S_n = a + aq + aq^2 + \cdots + aq^{n-1} = \frac{a - aq^n}{1 - q} = \frac{a}{1 - q} - \frac{aq^n}{1 - q}
> >$$
> >当 $|q| < 1$ 时，由于 $\displaystyle \lim _{n \rightarrow \infty} q^n = 0$，从而  $ \displaystyle\lim _{n \rightarrow \infty} S_n = \frac{a}{1 - q}$，因此该级数收敛，其和为$\frac{a}{1 - q}$.
> >当 $|q| > 1$ 时，由于 $ \displaystyle\lim _{n \rightarrow \infty} q^n = \infty$，从而 $ \displaystyle\lim _{n \rightarrow \infty} S_n = \infty$，这时级数发散.
> >如果 $|q| = 1$，那么当 $q = 1$ 时，$S_n = na \to \infty$，因此级数 发散；
> >当 $q = -1$ 时，级数成为 $a - a + a - a + \cdots$, 显然，$S_n$ 随着 $n$ 为奇数或偶数而等于 $a$ 或 $0$，从而 $S_n$ 的极限不存在，这时级数也发散.
> >
> >综合上述结果，我们得到：如果等比级数的公比的绝对值 $|q| < 1$，那么级数收敛；如果 $|q| \ge 1$，那么级数发散.
>
>
> >**例2:证明$\displaystyle S_n=\sum_{i=1}^{\ n} i$, 发散**
> >
> >**证:** 这级数的部分和为  
> >$$
>S_n = 1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}.
> >$$
> >显然，$\displaystyle\lim _{n \rightarrow \infty} S_n = \infty$，因此所给级数是发散的。
>
>
> >**例3:判断无穷级数$\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)}+\cdots$的收敛性.**
>  >
> >**解:** 级数的部分和
>  >$$
>\begin{aligned}
>\quad S_n &=\frac{1}{1 \cdot 2}+\frac{1}{2 \cdot 3}+\cdots+\frac{1}{n(n+1)}+\cdots \\
>& =\frac{1}{1}-\frac{1}{2}+\frac{1}{2}-\frac{1}{3}+\cdots+\frac{1}{n}-\frac{1}{n+1} \\
>& =1-\frac{1}{n+1} \rightarrow 1 \quad(n \rightarrow \infty) 
>\end{aligned}
> >$$
> >故级数收敛. 
> >

>[!warning]
> - 通过计算判断级数收敛——有时可行，有时不可行
> - 可以用别的办法（不计算）来判断收敛

> [!important] 
> 
>
>==性质1==
>
>$ \displaystyle \sum_{n=1}^{\infty } u_n=s . \quad \displaystyle \sum_{n=1}^{\infty } k u_n=k s.$
>
>==性质2==
>
>已知$\displaystyle \sum_{n=1}^{\infty } u_n=s, \displaystyle \sum_{n=1}^{\infty } v_n=δ$,有$\displaystyle \sum_{n=1}^{\infty }\left(u_n+v_n\right)=s+δ.$
>
>==性质3==
>
>改变级数有限项不影响收敛性.
>
>==性质4== 
>
>级数$ \displaystyle \sum_{n=1}^{\infty } u_n$收敛 ，那么对这项级数的项任意加括号后所成的级数仍收敛，且和不变.
>
>==性质5== 
>
>级数$ \displaystyle \sum_{n=1}^{\infty } u_n$收敛 $\displaystyle \Longrightarrow \lim _{n \rightarrow \infty} u_n \Rightarrow 0$.

>[!warning]
> - 由性质5，若级数的一般项不趋于零，那么该级数一定发散.比如，级数
>$$
> \frac{1}{2}-\frac{2}{3}+\frac{3}{4}-\cdots+(-1)^{n-1} \frac{n}{n+1}+\cdots
>$$
>他的一般项不趋于零，因此该级数发散;
> -  级数的一般项趋于零不是级数收敛的充分条件，即$\displaystyle\lim _{n \rightarrow \infty} a_n=0 \nRightarrow \text { 级数收敛. }$.比如，调和级数
>$$
>1+\frac{1}{2}+\frac{1}{3}+\cdots+\frac{1}{n}+\cdots
>$$
>他的一般项趋于零，但是他是发散的.
>


## 常数项级数的审敛法
>[!tip]
>
> 直接计算部分和很多时候并不可行, 如果我们只关心级数收敛与否, 可以使用一些判别法来判断级数的收敛性, 这些判别法也称为**审敛法**.

### 正项级数

>> [!important]
>
>==定理1==
>
>正项级数 $\displaystyle \sum_{n=1}^{\infty} u_n$ 收敛的充要条件是 $S_n$ 有界.
>
>注: 本质上这个定理就是我们上册学过的**单调有界有极限**.
>
>==定理2(比较审敛法)==
>
>设$\sum u_n$ 和 $\sum v_n$ 都是正项级数，且$u_n \leqslant v_n$.
>则，若$\sum  v_n$收敛，则$ \Rightarrow \sum  u_n$收敛;若$\sum u_n $发散，则 $ \Rightarrow \sum v_n $ 发散. 
>
>注：上述结论与前 $N$ 项无关.

>[!note]
>
> >**例2:证明级数$\sum \frac{1}{\sqrt{n(n+1)}}$发散.**
> >
> > **证:**
> >因$\frac{1}{n+1}<\frac{1}{\sqrt{n(n+1)}}<\frac{1}{\sqrt{n n}}$，由比较审敛法，所给级数发散.


> [!important]
> 
>==定理3（比较审敛法的极限形式）==
>设 $\displaystyle \sum\limits_{n=1}^{\infty} u_n$ 和 $\displaystyle \sum\limits_{n=1}^{\infty} v_n$ 都是正项级数，
>
>1. 如果 $\displaystyle\lim\limits_{n \to \infty} \frac{u_n}{v_n} = l\ (0\le l < +\infty)$，且级数 $\displaystyle\sum\limits_{n=1}^{\infty} v_n$ 收敛，那么级数 $\displaystyle\sum\limits_{n=1}^{\infty} u_n$ 收敛；
>
>2. 如果 $\displaystyle\lim\limits_{n \to \infty} \frac{u_n}{v_n} = l > 0$ 或 $\displaystyle\lim\limits_{n \to \infty} \frac{u_n}{v_n} = +\infty$，且级数 $\displaystyle\sum\limits_{n=1}^{\infty} v_n$ 发散，那么级数 $\displaystyle\sum\limits_{n=1}^{\infty} u_n$ 发散。


>[!note]
>
> >**例3．判定级数$\displaystyle \sum_{n=1}^{\infty} \sin \frac{1}{n}$敛散性**
> >
> >**解:**
> >$\lim\limits_{n \to \infty} \frac{\sin \frac{1}{n}}{\frac{1}{n}}=1 > 0$，而级数$\displaystyle \sum_{n=1}^{\infty} \frac{1}{n}$发散，故$\quad \sum \sin \frac{1}{n} $发散.

>[!important]
>
>==定理4(比值审敛法，达朗贝尔判别法)（非常重要！）==
>
>设$\displaystyle\sum\limits_{n=1}^{\infty} u_n$为正项级数，如果$\quad \lim _{n \rightarrow 0} \frac{u_{n+1}}{u_n}=ρ$
>那么当$ρ<1$时，级数收敛. $ ρ>1$时，级数发散. $ ρ=1$时,级数不确定收敛还是发散.

>[!note]
>
> >**例4．判断$\quad 1+\frac{1}{1}+\frac{1}{1· 2}+\frac{1}{1·2·3}+\cdots+\frac{1}{(n-1)!}+\dots$敛散性.**
> >$$
>\lim _{n \rightarrow \infty} \frac{u_{n+1}}{u_n}=\lim _{n \rightarrow \infty} \frac{(n-1)!}{n!}=\lim _{n \rightarrow \infty} \frac{1}{n}=0 \quad
> >$$
> >因此该级数收敛.
> >
>
> >**例5．判断$\quad \frac{1}{10}+\frac{1·2}{10^2}+\frac{1·2·3}{10^3}+\cdots+\frac{n!}{10^n}$敛散性.**
> >
> >$$
\lim _{n \rightarrow \infty} \frac{u_{n+1}}{u_n}=\lim _{n \rightarrow \infty} \frac{(n+1)}{10}=\infty
> >$$
> >因此该级数发散.


### 交错级数
>[!important]
> 
> ==交错级数的定义==
> 交错级数是正项和负项交替出现的级数，形式满足$a_1-a_2+a_3-a_4+...+(-1)^{n+1}a_n+...$，其中$an＞0$.

>[!important]
>
>==定理7（莱布尼茨定理）==
>
>对$\sum_{n=1}^{\infty}(-1)^{n-1} u_n$, 若 $ u_n \geqslant u_{n+1} . \quad \lim _{n \rightarrow \infty} u_n=0$,则级数收敛.

>[!note]
>
> >**例:判断$1-\frac{1}{2}+\frac{1}{3}-\frac{1}{4}+\cdots+(-1)^{n-1} \frac{1}{n}+\cdots$**
> >$$
u_n=\frac{1}{n}, \quad u_n>u_{n+1} \quad \lim _{n+1} u_n=0
> >$$
> >因此由定理7，该级数收敛.


### 绝收数与条件收敛
>[!important]
>==绝对收敛==
> $\displaystyle \sum_{n=1}^{\infty}\left|u_n\right|$ 收敛
>
>==条件收敛==
>  $\displaystyle \sum_{n=1}^{\infty} u_n$ 收敛

>[!warning]
> 绝对收敛 $\Rightarrow $条件收敛 


>[!note]
>
> >**例9.判断级数$\quad \sum \frac{\sin n \alpha}{n^2}$收敛性.**
>  >
>  > **解:**
> >
> >因$\sum\left|\frac{\sin \alpha}{n^2}\right| \leqslant \sum \frac{1}{n^2}$, 故收敛.



## 幂级数
>[!tip]
> 由常数数列构成的级数称为**常数项级数**, 由无穷多个函数的和构成的无穷级数称为**函数项级数**. **幂级数**是函数项级数中最简单也最直观的例子.



### 幂级数

>[!important]
>
>==幂级数==
>
>各项都是常数乘幂函数的函数项级数，它的形式是:
>$$
>\displaystyle \sum_{n=1}^{\infty} a_n x^n = a_0 + a_1x + a_2x^2 + \cdots + a_nx^n + \cdots
>$$
>其中常数a_0,a_1,a_2,…,a_n,…叫做幂级数的系数.


>[!note]
>
> >**例1:求幂级数$1 + x + x^2 + \cdots + x^n + \cdots = \frac{1 - x^n}{1 - x}$的收敛半径与收敛域.**
> >
> >**解:**因为
> >$$
>\rho=\lim _{n\rightarrow\infty}\left|\frac{a_{n+1}}{a_{n}}\right|=\lim _{n\rightarrow\infty}\frac{\frac{1}{n+1}}{\frac{1}{n}}=1,
> >$$
> >所以收敛半径$ R=\frac{1}{\rho}=1. $
> >当 $x = -1$ 时,级数成为
> >$$
>  -1-\frac{1}{2}-\frac{1}{3}-\cdots-\frac{1}{n}-\cdots 
> >$$
> >此级数发散（为调和级数的负数形式）
> >当 $x = 1$ 时,级数成为交错级数
> >$$
> \displaystyle \sum_{n=1}^{\infty} (-1)^{n}\frac{1}{n}
> >$$
> >此级数收敛.
> >综上所述，
> >* $|x| < 1$:收敛
> >* $|x| > 1$:发散
> >* $x = 1$:发散
> >* $x = -1$:发散
>
> >**例2:求幂级数$1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots + \frac{x^n}{n!} + \cdots = e^x$的收敛域.**
> >
> >**解:** 因为
> >$$
> \rho = \lim_{n\rightarrow\infty} \left| \frac{a_{n+1}}{a_n} \right| 
= \lim_{n\rightarrow\infty} \frac{\frac{1}{(n+1)!}}{\frac{1}{n!}} 
= \lim_{n\rightarrow\infty} \frac{1}{n+1} 
= 0
> >$$
> >所以收敛半径是$ R = \frac{1}{\rho} = +\infty $,
> >故收敛域为：$ (-\infty, +\infty) $.


>[!important]
>
>==定理1（阿贝尔(Abel)定理）==
>
>如果级数$\displaystyle \sum_{n=1}^{\infty} a_n x^n$ 当$x=R(R\neq 0)$时收敛，那么
>* 适合不等式
 >$|x| < R $ 的一切 x 使得幂级数绝对收敛.
 >
>反之，如果级数$\displaystyle \sum_{n=1}^{\infty} a_n x^n$ 当 $x=R(R\neq 0)$时发散，那么 
>* 适合不等式 $|x| > R$的一切 x 使得幂级数发散.
>
>注意:$x = R, -R$待定.
>
>
>
>==收敛半径==
>
>正数$R$
>
>
>==收敛区域==
>
>收敛区间$(-R, R)$以及$[-R, R]$, $(-R, R]$, $(-R, R)$. 
>
>
>==定理2==
>
>如果
>$$
\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \ell,
>$$
>其中 $a_n,a_{n+1}$ 为幂级数相邻两项的系数，$\ell$为常数，则幂级数的收敛半径为
>$$
R = 
\begin{cases}
\frac{1}{\ell}, & \ell \ne 0 \\
\infty, & \ell = 0 \\
0, & \ell = +\infty.
\end{cases}
>$$


>[!note]
>
> >**例1:求幂级数$x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots + (-1)^n \frac{x^n}{n} + \cdots$的收敛半径与收敛域.**
> >
> >**解:**因为
> >$$
>\ell = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \frac{\frac{1}{n+1}}{\frac{1}{n}} = 1
>\Rightarrow R = 1
> >$$
> >所以收敛半径$R=1$.
> >* $x = -1 \Rightarrow -1 + \frac{1}{2} - \cdots$:发散.
> >* $x = 1 \Rightarrow 1 - \frac{1}{2} + \frac{1}{3} - \cdots$:收敛.
> >故收敛区间:$(-1, 1]$.
>
>
> >**例2:求幂级数的收敛域.**
> >$$
>1 + x + \frac{x}{2!}  + \cdots + \frac{1}{n!}x^n + \cdots
> >$$
> >**解:**
> >$$
>\ell = \lim_{n \to \infty} \frac{1}{n+1} = 0
>\Rightarrow R = \infty \Rightarrow (-\infty, \infty)
> >$$
>
>
> >**例3:求幂级数 $\displaystyle\sum_{n=1}^\infty {n!}{x^n}$ 的收敛半径（规定 $0! = 1$）**
> >
> >**解:**
> >$$
>\rho = \lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \frac{(n+1)!}{n!} = \lim_{n\to\infty} \frac{n+1}{1} =+\infty
> >$$
> >故收敛半径 $R = 0$，级数在 $x=0$ 收敛.
>
>
> >**例5:求幂级数 $\displaystyle\sum_{n=1}^\infty \frac{(x-1)^n}{2^n \cdot n}$ 的收敛域.**
> >
> >**解:**
> >令 $t = x - 1$，级数变为 $\displaystyle\sum_{n=1}^\infty \frac{t^n}{2^n n}$
> >因为
> >$$
>\rho = \lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \frac{2^n n }{2^{n+1}(n+1)} = \frac{1}{2}
> >$$
>>故收敛半径 $R = 2$.
>>收敛区间为$ | t | <2$，即$ -1 < x < 3 $.
>>- 当  $x = -1$,级数变为 $\displaystyle\sum_{n=1}^\infty \frac{(-1)^n}{n}$（收敛）
>>- 当  $x = 3$）,级数变为 $\displaystyle\sum_{n=1}^\infty\frac{1}{n}$（发散）
>>因此原级数的收敛域是$[-1, 3)$


## 幂级数展开

>[!important]
>==常用展开式==
>1. 指数函数:
   >$$
   > e^x = 1 + x + \frac{x^2}{2!} + \cdots+\frac{x^n}{n!}+\cdots \quad (-\infty < x < \infty) 
   > $$
>2. 正弦函数:
   >$$
   >\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots+(-1)^n \frac{x^{2n+1}}{(2n+1)!}+\cdots \quad (-\infty < x < \infty) 
   >$$
>3. 几何级数:
   >$$
   >  \frac{1}{1+x} = \sum_{n=0}^\infty (-1)^n x^n \quad (-1 < x < 1) 
   > $$
>4. 对数函数:
   >$$
   > \ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n \quad (-1 < x \leq 1) 
   > $$
>5. 余弦函数:
   >$$
   > \cos x = \sum_{n=1}^\infty \frac{(-1)^{n}}{2n!} x^(2n) \quad (-\infty < x < \infty) 
   > $$

## 幂级数展开例题
> [!note]
> 
> > **例3:将函数 $f(x) = (1 - x) \ln(1 + x)$ 展开成 $x$ 的幂级数.**
> > 
> > **解**:已知 $\ln(1+x)$ 的幂级数展开:
> >$$
>\ln(1+x) = \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n \quad (-1 < x \leq 1)
> >$$
> >因此:
> >$$
>\begin{aligned}
>f(x) &= (1-x) \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n \\
>&= \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n - \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^{n+1} \\
>&= \sum_{n=1}^\infty \frac{(-1)^{n-1}}{n} x^n - \sum_{n=2}^\infty \frac{(-1)^{n}}{n-1} x^n \\
>&= x + \sum_{n=2}^\infty  \frac{(-1)^{n-1}(2n-1)}{n(n-1)}   x^n
>\end{aligned} \quad
> >$$
> 
>
> > **例4: 将函数 $\sin x$ 展开成 $(x - \frac{\pi}{4})$ 的幂级数.**
> >
> > **解**:
> >$$
>\sin x = \sin\left( \frac{\pi}{4} + \left(x - \frac{\pi}{4}\right) \right) 
= \sin\frac{\pi}{4} \cos\left(x - \frac{\pi}{4}\right) + \cos\frac{\pi}{4} \sin\left(x - \frac{\pi}{4}\right)
> >$$
>
>
> > **例5:将函数 $f(x) = \frac{1}{x^2 + 4x + 3}$ 展开成 $(x-1)$ 的幂级数.**
> > 
> > **解**:
> >$$
>f(x) = \frac{1}{(x+1)(x+3)} = \frac{1}{2(1+x)} - \frac{1}{2(3+x)}
> >$$
> >
> >变形为 $(x-1)$ 形式:
> >$$
>\frac{1}{2(1+x)} = \frac{1}{4\left(1 + \frac{x-1}{2}\right)}, \quad \frac{1}{2(3+x)} = \frac{1}{8\left(1 + \frac{x-1}{4}\right)}
> >$$
> >
> >利用几何级数展开:
> >$$
>\begin{aligned}
>\frac{1}{4\left(1 + \frac{x-1}{2}\right)} &= \frac{1}{4} \sum_{n=0}^\infty \frac{(-1)^n}{2^n} (x-1)^n \quad (-1 < x < 3) \\
>\frac{1}{8\left(1 + \frac{x-1}{4}\right)} &= \frac{1}{8} \sum_{n=0}^\infty \frac{(-1)^n}{4^n} (x-1)^n \quad (-3 < x < 5)
\end{aligned}
> >$$
> >
> >所以
> >$$
>f(x) = \sum_{n=0}^\infty (-1)^n \left( \frac{1}{2^{n+2}} - \frac{1}{2^{2n+3}} \right) (x-1)^n \quad (-1 < x < 3)
> >$$



## 傅里叶级数（Fourier Series）不考

>[!warning]
>这里和傅里叶级数有什么关系？
>多项式展开:
>$$ f(x) = a_0 + a_1x + a_2x^2 + \cdots + a_nx^n + \cdots$$
>
>离散点近似:
>$$
>f(x) \sim \begin{bmatrix} 
f(0) \\ 
f(0.25) \\ 
f(0.5) \\ 
f(0.75) \\ 
f(1) 
\end{bmatrix}
>$$
>矩阵形式展开
>
>将函数表示为系数方程组:
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
>简写为矩阵形式:
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

>[!warning]
>
> 1. $a_0,a_1,...,a_4$ 不好算
> 2. 性质也不好.

>[!warning]
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
>$$

> [!warning]
>
> 1. ${a}$好算.
> 2. 不连续.

>[!important]
>
> ==积分公式==
> $$
>\int_0^1 \sin(2\pi x) \, dx = 0= \int_0^1 \cos(2\pi x) \, dx 
>$$
>$$
>\int_0^1 \sin(2\pi n x) \sin(2\pi m x) \, dx = 0 \quad (n \neq m)
>$$
>$$
>\int_0^1 \cos(2\pi n x) \cos(2\pi m x) \, dx = \frac{1}{2} \int_0^1 \left[\cos(2\pi (n+m)x) + \cos(2\pi (n-m)x)\right] \, dx = 0
>$$
>$$
>\int_0^1 dx = 1, \quad \int_0^1 \sin^2(2\pi n x) \, dx =  \int_0^1 \frac{1- \cos((2\pi)2 n x) }{2}dx =\frac{1}{2}
>$$
>
>==傅里叶级数展开式==
> $$
>f(x) = \frac{a_0 }{2}+ \sum_{k=1}^{\infty} \left[ a_k \cos(\frac{2\pi k x}{T}) + b_n \sin(\frac{2\pi k x}{T}) \right]
$$
>$$
a_k = \frac{2}{T}\int_0^T f(x) \cos(\frac{2\pi k x}{T}) \, dx, 
>$$
>$$
b_k =  \frac{2}{T}\int_0^T f(x) \sin(\frac{2\pi k x}{T}) \, dx
>$$
>适用于周期函数（周期为 T）.

---

### 复数形式
>[!important]
>
> ==欧拉公式==
>
>$$
e^{ix} = \cos x + i \sin x, \quad e^{-ix} = \cos x - i \sin x
>$$
>  
>$$
\cos x = \frac{1}{2} (e^{ix} + e^{-ix}), \quad \sin x = \frac{1}{2i} (e^{ix} - e^{-ix})
>$$
>
>==周期为 $ 2l $傅里叶级数展开式== 
>
>$$
>f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(\frac{n\pi x}{l}) + b_n \sin(\frac{n\pi x}{l}) \right]
>$$
>
>==系数表达式==
>$$
>a_n =\frac{1}{l} \int_{-l}^{l} f(x) \cos(\frac{n\pi x}{l}) \, dx, \quad b_n = \frac{1}{l}\int_{-l}^{l} f(x) \sin(\frac{n\pi x}{l}) \, dx
>$$
>
>==复数形式结果==
>$$
>\begin{aligned}
>f(x) & = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ \frac{a_n}{2}(e^{i\frac{n\pi x}{l}}+e^{-i\frac{n\pi x}{l}} ) - \frac{b_ni}{2} (e^{i\frac{n\pi x}{l}}-e^{-i\frac{n\pi x}{l}} )  \right] \\
>&= \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ \frac{a_n-b_ni}{2} e^{i\frac{n\pi x}{l}} + \frac{a_n+b_ni}{2} e^{-i\frac{n\pi x}{l}} \right]
>\end{aligned}
>$$


[回到主页面](index.html)