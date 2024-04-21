# **Exercises for Math Model D: Geometrical Calculation**
### 四則演算 に関する演習問題です。

## ExMM_D_00: arithmetics
２つの整数 $A$ と $B$ を考えます。  
四則演算（加算，減算，乗算，除算）の結果を計算し, 表示して下さい。

### Input lines: paste lines after starting program
A B

[Case a]
``` python
20 -40 
```
[Case b]
``` python
-80 40
```
[Case c]
``` python
-80 -160
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_D_00a_arithmetics](../ExMathModel_D_Arithmetics/D_00/ExMM_D_00a_arithmetics.py)
>    :  +, - , *, /; 手順通りの逐次計算
> 
> b. [ExMM_D_00b_arithmetics](../ExMathModel_D_Arithmetics/D_00/ExMM_D_00b_arithmetics.py)
>    :  +, - , *, /, function; ４つの関数を用いた計算
> 
> c. [ExMM_D_00c_arithmetics](../ExMathModel_D_Arithmetics/D_00/ExMM_D_00c_arithmetics.py)
>    :  +, - , *, /, function; １つの関数を用いた計算 
> 
> a. [ExMM_D_00d_arithmetics](../ExMathModel_D_Arithmetics/D_00/ExMM_D_00d_arithmetics.py)
>    :  +, - , *, /, class; クラスを用いた計算
> 

</details>


## ExMM_D_01: divisors
正の整数 $N$ を考えます。  
$N$ の約数を昇順で表示して下さい。

### Input lines: paste lines after starting program
N

[Case a]
``` python
360 
```
[Case b]
``` python
1
```
[Case c]
``` python
113
```
[Case d]
``` python
40320
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_D_01a_divisors](../ExMathModel_D_Arithmetics/D_01/ExMM_D_01a_divisors.py)
>    :  %, list; 手順通りの逐次計算
> 
> b. [ExMM_D_01b_divisors](../ExMathModel_D_Arithmetics/D_01/ExMM_D_01b_divisors.py)
>    :  %, list; よりコンパクトな逐次計算，リストのソート
> 
> c. [ExMM_D_01c_divisors](../ExMathModel_D_Arithmetics/D_01/ExMM_D_01c_divisors.py)
>    :  %, function; 関数を用いたリストの計算 

</details>


## ExMM_D_02: prime factors
正の整数 $N$ を考えます。  
$N$ の素因数を昇順で表示して下さい。

### Input lines: paste lines after starting program
N

[Case a]
``` python
60 
```
[Case b]
``` python
1
```
[Case c]
``` python
720
```
[Case d]
``` python
1212750
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_D_02a_prime_factors](../ExMathModel_D_Arithmetics/D_02/ExMM_D_02a_prime_factors.py)
>    :  %, list, while-loop; 手順通りの逐次計算
> 
> b. [ExMM_D_02b_prime_factors](../ExMathModel_D_Arithmetics/D_02/ExMM_D_02b_prime_factors.py)
>    :  %, list, while-loop, function; 関数を用いたリストの計算

</details>


## ExMM_D_03: gcd_lcm
正の整数 $A, B$ を考えます。  
$A$ と $B$ の最大公約数（gcd）と最小公約数（lcm）を計算して表示しなさい。

### Input lines: paste lines after starting program
A B

[Case a]
``` python
12 18 
```
[Case b]
``` python
36 12
```
[Case c]
``` python
25 36
```
[Case d]
``` python
1 12
```

<details>
<summary>Sample programs: Click here !</summary>

> a. [ExMM_D_03a_gcd_lcm](../ExMathModel_D_Arithmetics/D_03/ExMM_D_03a_gcd_lcm.py)
>    :  %, for-loop; 手順通りの逐次計算
> 
> b. [ExMM_D_03b_gcd_lcm](../ExMathModel_D_Arithmetics/D_03/ExMM_D_03b_gcd_lcm.py)
>    :  %, while-loop, mutual division method; 互除法による計算
> 
> c. [ExMM_D_03c_gcd_lcm](../ExMathModel_D_Arithmetics/D_03/ExMM_D_03c_gcd_lcm.py)
>    :  %, while-loop, mutual division method; 関数を用いた互除法による計算
> 
> d. [ExMM_D_03d_gcd_lcm](../ExMathModel_D_Arithmetics/D_03/ExMM_D_03d_gcd_lcm.py)
>    :  gcd(), lcm(); 標準ライブラリ `math' の関数を用いた計算

</details>


## ExMM_D_04: multiples
２つの整数 $A$ と$B$ を考えます。  
次に示す４種類の $B$ の倍数を計算して, 表示して下さい。  
「$B$ の倍数のうち，$A$ 以下で最大のもの 」  
「$B$ の倍数のうち，$A$ より小さい最大のもの 」  
「$B$ の倍数のうち，$A$ 以上で最小のもの 」  
「$B$ の倍数のうち，$A$ より大きく最小のもの 」

### Input lines: paste lines after starting program
A B

[Case a]
``` python
15 5 
```
[Case b]
``` python
16 5
```
[Case c]
``` python
14 5
```

<details>
<summary>Sample programs: click here !</summary>

> a. [ExMM_D_04a_multiples](../ExMathModel_D_Arithmetics/D_04/ExMM_D_04a_multiples.py)
>    %, //: 商と剰余を用いて，定義に従って倍数を計算
> 
> b. [ExMM_D_04b_multiples](../ExMathModel_D_Arithmetics/D_04/ExMM_D_04b_multiples.py)
>    //: if文を用いずに，４種類の倍数を計算
> 
> c. [ExMM_D_04c_multiples](../ExMathModel_D_Arithmetics/D_04/ExMM_D_04c_multiples.py)
>    //: function; ４種類の倍数を計算する関数を用いた計算
> 
> d. [ExMM_D_04d_multiples](../ExMathModel_D_Arithmetics/D_04/ExMM_D_04d_multiples.py)
>    //: class; 変数と関数を内蔵するクラスを用いた計算

</details> 

