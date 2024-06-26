# **Exercises for Math Model D: Geometrical Calculation**
#### 幾何学計算 に関する演習問題です。

### ExMM_D_00: geom_arithmetics
２つの整数 $A& と$B$ を考えます。
$A$ と$B$ が空白で区切られて，１行で与えられます。

四則演算（加算，減算，乗算，除算）の結果を計算します。 
これらを表示して下さい。

### Input lines
#### 注: プログラム実行後に, 張り付けて下さい。

``` python
A B

[Case a]
20 10 

[Case b]
40 -20

[Case c]
-80 40

```

>Sample programs
>
> a. [ExMM_D_00a_geom_arithmetics](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_00a_geom_arithmetics.py)
>    //  +, - , *, /
> 
> b. [ExMM_D_00b_geom_arithmetics](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_00b_geom_arithmetics.py)
>    //  +, - , *, /, function
> 
> c. [ExMM_D_00c_geom_arithmetics](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_00c_geom_arithmetics.py)
>    //  +, - , *, /, function
> 
> d. [ExMM_D_00d_geom_arithmetics](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_00d_geom_arithmetics.py)
>    //  +, - , *, /, class
> 


### ExMM_D_01: geom_mltiples
２つの整数 $A& と$B$ を考えます。
$A$ と$B$ が空白で区切られて，１行で与えられます。

次に示す４つの $B$ の倍数を計算します。
「$B$ の倍数のうち，$A$ 以下で最大のもの 」，「$B$ の倍数のうち，$A$ より小さい最大のもの 」，
「$B$ の倍数のうち，$A$ 以上で最小のもの 」，「$B$ の倍数のうち，$A$ より大きく最小のもの 」
これらを表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
A B

[Case a]
15 5 

[Case b]
16 5

[Case c]
14 5

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_D_01a_geom_multiples](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_01a_geom_multiples.py)
>    %, //
> 
> b. [ExMM_D_01b_geom_multiples](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_01b_geom_multiples.py)
>    //
> 
> c. [ExMM_D_01c_geom_multiples](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_01c_geom_multiples.py)
>    //, function
> 
> d. [ExMM_D_01d_geom_multiples](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_01d_geom_multiples.py)
>    //, class
> 


### ExMM_D_04: geom_point
平面座標における座標点 $A(X, Y)$ を考えます。
整数 $X$ と$Y$ が空白で区切られて，１行で与えられます。

原点から座標点 $A$ までの距離と，原点から見た座標点の方位角を計算します。
これらを表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
X Y

[Case a]
3 4 

[Case b]
-3 -4

[Case c]
-3 -4

[Case d]
3 -4

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_D_04a_geom_point](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_04a_geom_point.py)
>    sqrt(), atan2()
> 


### ExMM_D_05: geom_point_list
平面座標における $N$ 個の座標点 $A_1(X_1, Y_1) ... A_N(X_N, Y_N)$ を考えます。
整数 $X$ と$Y$ が空白で区切られて，１行で与えられます。

座標点の個数 $N$ が最初の行で，座標値 $(X, Y)$ が空白で区切られ，後続の行で与えられます。
原点からそれぞれの座標点 $A$ までの距離と，原点から見た座標点の方位角を計算します。
これらを表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
X1 Y1
X2 Y2
...
XN YN

[Case a]
4
3 4 
-3 -4
-3 -4
3 -4

[Case b]
5
8 3
2 -5
-4 7
0 6
1 -9

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_D_05a_geom_point_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_D_Geometrical%20Calculation/ExMM_D_05a_geom_point_list.py)
>    sqrt(), atan2()
> 



