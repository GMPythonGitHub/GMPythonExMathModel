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
>    : sqrt(); 入力値のリストへの格納，for-loop を用いた逐次計算 
>
> b. [ExMM_E_01b_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01b_point_list.py)
>    : sqrt(), list comprehension; 入力値のリスト内包標記による格納と，逐次計算
>
> c. [ExMM_E_01c_point_list](../ExMathModel_E_Geometry/E_01/ExMM_E_01c_point_list.py)
>    : sqrt(), list, list comprehension, list; 座標点間の距離のリストへの格納ろ，リストのソート計算

</details> 


## ExMM_E_02: vector_xxyy
平面座標におけるベクトル $V(X, Y)$ を考えます。  
ベクトル $V$ の成分 $X, Y$ からベクトルの大きさ $r$ と方位角 $\theta$ を計算し，表示して下さい。

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
[Case c]
``` python
-3 -4
```
[Case d]
``` python
4 -3
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_02a_vector_xxyy](../ExMathModel_E_Geometry/E_02/ExMM_E_02a_vector_xxyy.py)
>    : sqrt(), atan2(); 手順通りの計算 
>
> b. [ExMM_E_02b_vector_xxyy](../ExMathModel_E_Geometry/E_02/ExMM_E_02b_vector_xxyy.py)
>    : sqrt(), atan2(), function; ２つの関数を用いた計算 
>
> c. [ExMM_E_02c_vector_xxyy](../ExMathModel_E_Geometry/E_02/ExMM_E_02c_vector_xxyy.py)
>    : sqrt(), atan2(), function; １つの関数を用いた計算 
>
> d. [ExMM_E_02d_vector_xxyy](../ExMathModel_E_Geometry/E_02/ExMM_E_02d_vector_xxyy.py)
>    : sqrt(), atan2(), function; クラスを用いた計算 

</details> 


## ExMM_E_03: vector_rrth
平面座標におけるベクトル $V(X, Y)$ を考えます。  
ベクトル $V$ の大きさ $r$ と方位角 $\theta$ からベクトルの成分 $X, Y$ を計算し，表示して下さい。

### Input lines: paste lines after starting program
R T  

[Case a]
``` python
4 30 
```
[Case b]
``` python
4 150
```
[Case c]
``` python
12 -120
```
[Case d]
``` python
12 -45
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_03a_vector_xxyy](../ExMathModel_E_Geometry/E_03/ExMM_E_03a_vector_rrth.py)
>    : sqrt(), atan2(); 手順通りの計算 
>
> b. [ExMM_E_03b_vector_xxyy](../ExMathModel_E_Geometry/E_03/ExMM_E_03b_vector_rrth.py)
>    : sqrt(), atan2(), function; ２つの関数を用いた計算 
>
> c. [ExMM_E_03c_vector_xxyy](../ExMathModel_E_Geometry/E_03/ExMM_E_03c_vector_rrth.py)
>    : sqrt(), atan2(), function; １つの関数を用いた計算 
>
> d. [ExMM_E_03d_vector_xxyy](../ExMathModel_E_Geometry/E_03/ExMM_E_03d_vector_rrth.py)
>    : sqrt(), atan2(), function; クラスを用いた計算，ExMM_E_03d_vector_xxyy.py のクラスを拡張・修正

</details> 


## ExMM_E_04: vector_product
平面座標における２つのベクトル $A(A_x, A_y)$ と $B(B_x, B_y)$ を考えます。  
ベクトル $A$ と $B$ のドット積（$A \dot B$ 内積）とクロス積（$A \cross B$ 外積）を計算し，表示して下さい。

### Input lines: paste lines after starting program
Ax Ay 
Bx By

[Case a]
``` python
3 4 
3 4 
```
[Case b]
``` python
3 4
-4 3
```
[Case c]
``` python
3 4
4 -3
```
[Case d]
``` python
3 4
-3 -4
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_04a_vector_product](../ExMathModel_E_Geometry/E_04/ExMM_E_04a_vector_product.py)
>    : ; 手順通りの計算 
>
> b. [ExMM_E_04b_vector_product](../ExMathModel_E_Geometry/E_04/ExMM_E_04b_vector_product.py)
>    : function; ２つの関数を用いた計算 
>
> c. [ExMM_E_04c_vector_product](../ExMathModel_E_Geometry/E_04/ExMM_E_04c_vector_product.py)
>    : tuple, function; ベクトルをtupleとして表示，１つの関数を用いた計算 
>
> d. [ExMM_E_04d_vector_product](../ExMathModel_E_Geometry/E_04/ExMM_E_04d_vector_product.py)
>    : tuple, class; ベクトルをtupleとして表示，クラスを用いた計算
>
> e. [ExMM_E_04e_vector_product](../ExMathModel_E_Geometry/E_04/ExMM_E_04e_vector_product.py)
>    : tuple, class; ベクトルをtupleとして表示，クラスを用いた計算，ExMM_E_03d_vector_xxyy.py のクラスを拡張・修正

</details> 



