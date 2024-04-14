# **Exercises for Math Model B: List Structures**
#### リスト構造 list, tuple, set に関する演習問題です。

### ExMM_B_00: list_tuple_set
長さ$N$ の数列 $A = (A_1，A_2, ... A_N)$ を考えます。
$N$ が最初の行で，数列 $A$ の要素が空白で区切られ，続く１行で与えられます。

読み取り，数列を `list`, `tuple` と `set` に変換します。 
これらを `f-string` を用いて表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
A1, A2, ... AN

[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
10
5 2 0 4 3 5 1 0 5 2

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_B_00a_list_tuple_set](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_00a_list_tuple_set.py)
>    //  input(), int(), float(), print()
> 
> b. [ExMM_B_00b_list_tuple_set](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_00b_list_tuple_set.py)
>    // f-string 


### ExMM_B_01: list_len_sum
数列 $A = (A_1，A_2, ...)$ を考えます。
数列 $A$ の要素が空白で区切られ，１行で与えられます。

読み取り，数列の項数と総和，最大値，最小値を求めます。 
これらを `f-string` を用いて表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
A1, A2, ...

[Case a]
8 4 9 5 3 6 0 2 7 1 

[Case b]
5 2 0 4 3 5 1 0 5 2

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_B_01a_list_len_sum](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_01a_list_len_sum.py)
>    // f-string
> 
> b. [ExMM_B_01b_list_len_sum](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_01b_list_len_sum.py)
>    // len(), sum(), max(), min() 


### ExMM_B_02: list_exchange
数列$A = (A_1，A_2, ...)$ を考えます。
数列の項数 $N$ が最初の行で，数列 $A$ の要素が空白で区切られ，次の１行で与えられます。

読み取り，奇数番目の項と次の項の入れ替えを繰返します。 
そのようにしてできる数列を表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
A1, A2, ..., AN

[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_B_02a_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_02a_list_exchange.py)
>    // append()
> 
> b. [ExMM_B_02b_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_02b_list_exchange.py)
>    // slicing 


### ExMM_B_03: list_reverse
数列$A = (A_1，A_2, ...)$ を考えます。
数列の項数 $N$ が最初の行で，数列 $A$ の要素が空白で区切られ，次の１行で与えられます。

読み取り，数列の順番を反転させます。 
反転した数列を表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
A1, A2, ..., AN

[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_B_03a_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_03a_list_reverse.py)
>    // append()
> 
> b. [ExMM_B_03b_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_03b_list_reverse.py)
>    // 
> 
> c. [ExMM_B_03c_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_03c_list_reverse.py)
>    // list comprehension
> 
> d. [ExMM_B_03d_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_03d_list_reverse.py)
>    // slicing
> 
> e. [ExMM_B_03e_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_03e_list_reverse.py)
>    // list.reverse()
> 
> f. [ExMM_B_03f_list_exchange](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_B_List%20Structures/ExMM_B_03f_list_reverse.py)
>    // reversed()
> 


