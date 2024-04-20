# **Exercises for Math Model E: Geometrical Calculation**
### 幾何学計算 に関する演習問題です。

## ExMM_E_00: geom_point
平面座標における座標点 $A(X, Y)$ を考えます。  
原点から座標点 $A$ までの距離と，原点から見た座標点の方位角を計算して，表示して下さい。

### Input lines: paste lines after starting program
X Y

[Case a]
``` python
3 4
``` 
[Case b]
```python
-3 -4
```
[Case c]
```python
-3 -4
```
[Case d]
```python
3 -4
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_00a_point](../ExMathModel_E_Geometry/E_00_point/ExMM_E_00a_point.py)
>    : sqrt(), atan2(); 手順通りの計算
>
> b. [ExMM_E_00b_point](../ExMathModel_E_Geometry/E_00_point/ExMM_E_00b_point.py)
>    : sqrt(), atan2(), function; 関数を用いた計算
> 
> c. [ExMM_E_00c_point](../ExMathModel_E_Geometry/E_00_point/ExMM_E_00c_point.py)
>    : sqrt(), atan2(), class; クラスを用いた計算


</details>


## ExMM_E_01: geom_point_list
平面座標における $N$ 個の座標点 $A_1(X_1, Y_1) ... A_N(X_N, Y_N)$ を考えます。  
原点からそれら座標点 $A_{1, ..., N}$ までの距離と，原点から見た座標点の方位角を計算し，表示して下さい。

### Input lines: paste lines after starting program
N  
X1 Y1  
X2 Y2  
...  ...  
XN YN

[Case a]
``` python
4
3 4 
-3 -4
-3 -4
3 -4
```
[Case b]
``` python
5
8 3
2 -5
-4 7
0 6
1 -9
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_E_01a_point_list](../ExMathModel_E_Geometry/E_01_point_list/ExMM_E_01a_point_list.py)
>    : sqrt(), atan2(): for-loop を用いた逐次計算 
>
> a. [ExMM_E_01b_point_list](../ExMathModel_E_Geometry/E_01_point_list/ExMM_E_01b_point_list.py)
>    : sqrt(), atan2(), list, list comprehension: リストへの入力値の格納と逐次計算
>
> a. [ExMM_E_01c_point_list](../ExMathModel_E_Geometry/E_01_point_list/ExMM_E_01c_point_list.py)
>    : sqrt(), atan2(), list, list comprehension, function: リストへの入力値の格納と関数を用いた逐次計算
>
> a. [ExMM_E_01d_point_list](../ExMathModel_E_Geometry/E_01_point_list/ExMM_E_01d_point_list.py)
>    : sqrt(), atan2(), list, list comprehension, class: クラスのリストへの入力値の格納と逐次計算
>

</details> 



