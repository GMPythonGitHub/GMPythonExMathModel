# **Exercises for Math Model E: Geometrical Calculation**
### 幾何学計算 に関する演習問題です。

## ExMM_E_00: point
平面座標における２つの座標点 $A(A_x,A_y), B(B_x, B_y)$ を考えます。  
座標点 $A, B$ の間の距離を計算して表示して下さい。

### Input lines: paste lines after starting program
Ax Ay
Bx By

[Case a]
``` python
0 0
4 3 
``` 
[Case b]
```python
4 3
7 7
```
[Case c]
```python
7 7
3 4
```
[Case d]
```python
3 4
0 0
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_00a_point](../ExMathModel_E_Geometry/E_00/ExMM_E_00a_point.py)
>    : sqrt(); 手順通りの計算
>
> b. [ExMM_E_00b_point](../ExMathModel_E_Geometry/E_00/ExMM_E_00b_point.py)
>    : sqrt(), function; 関数を用いた計算

</details>


## ExMM_E_01: point_list
平面座標における $N$ 個の座標点 $A_1(X_1, Y_1), ..., A_N(X_N, Y_N)$ を考えます。  
それらの座標点の間の距離を計算し，距離の最大値と最小値および平均値を計算し，表示して下さい。

### Input lines: paste lines after starting program
N  
X1 Y1  
X2 Y2  
...  ...  
XN YN

[Case a]
``` python
4
5 4 
-4 3
-3 -4
4 -5
```
[Case b]
``` python
5
4 3
2 -5
-8 7
0 6
1 -9
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_01a_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01a_point_list.py)
>    : sqrt(); for-loop を用いた逐次計算 
>
> b. [ExMM_E_01b_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01b_point_list.py)
>    : sqrt(), list comprehension; リストへの入力値の格納と，逐次計算
>
> c. [ExMM_E_01c_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01c_point_list.py)
>    : sqrt(), list, list comprehension, function; リストへの入力値の格納と，関数を用いた逐次計算

</details> 


## ExMM_E_02: vector
平面座標におけるベクトル $A(X, Y)$ を考えます。  
ベクトル $V$ のに関して，原点からの距離と，原点から見た方位角を計算し，表示して下さい。

### Input lines: paste lines after starting program
X Y  

[Case a]
``` python
3 4 
```
[Case b]
``` python
-4 3
```
[Case b]
``` python
-4 3
```
[Case b]
``` python
-4 3
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_01a_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01a_point_list.py)
>    : sqrt(), atan2(); for-loop を用いた逐次計算 
>
> a. [ExMM_E_01b_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01b_point_list.py)
>    : sqrt(), atan2(), list, list comprehension; リストへの入力値の格納と逐次計算
>
> a. [ExMM_E_01c_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01c_point_list.py)
>    : sqrt(), atan2(), list, list comprehension, function; リストへの入力値の格納と関数を用いた逐次計算
>
> a. [ExMM_E_01d_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01d_point_list.py)
>    : sqrt(), atan2(), list, list comprehension, class; 「クラスのリスト」への入力値の格納と逐次計算

</details> 



