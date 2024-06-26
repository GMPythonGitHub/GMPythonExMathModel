# **Exercises for Math Model A: Input and Output**
#### 数値や文字列データの入出力に関する演習問題です。

### ExMM_A_00: integer_float_string
整数 $A$ と実数 $B$，文字列 $C$ が１行ごとに与えられます。

`input()`を用いて読み取り，さらに変数に変換します。 
`print()`を用いて３変数を１行ごとに表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
A
B
C

[Case a]  Copy the following sentences to 'execution window'
12345
123.45
abcde

[Case b]  Copy the following sentences to 'execution window'
1234500000
0.00012345
abc de

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_00a_integer_float_string](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_00a_integer_float_string.py)
>    //  input(), int(), float(), print()
> 
> b. [ExMM_A_00b_integer_float_string](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_00b_integer_float_string.py)
>    // f-string 


### ExMM_A_01: integers
６個の整数 $A_1, A_2, ...，A_6$ が空白で区切られ，１行で与えられます。

読み取り，整数型変数に変換します。 
カンマと空白`, `で区切り，１行で表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
A1 A2 A3 A4 A5 A6

[Case a]  Copy the following sentences to 'execution window' !
4 5 3 0 2 1 

[Case b]  Copy the following sentences to 'execution window' !
100 130 110 140 150 120

```
注: プログラム実行後に張り付けて下さい。

</details>

>Sample programs
>
> a. [ExMM_A_01a_integers](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_01a_integers.py)
>    //  input(), split()
> 
> b. [ExMM_A_01b_integers](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_01b_integers.py)
>    //  input().split() 


### ExMM_A_02: integer_list_a
N個の整数を考えます。
整数の個数 $N$ が最初の行で，整数 $(A_1，A_2, ... A_N)$ が空白で区切られて次の行で与えられます。

読み取り，整数型の`list`に変換します。 
すべての要素をカンマと空白`, `で区切り，１行で表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
A1 A2 ... AN

[Case a]  Copy the following sentences to 'execution window' !
10
8 4 9 5 3 6 0 2 7 1 

[Case b]  Copy the following sentences to 'execution window' !
6
100 130 110 140 150 120

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_02a_integer_list_a](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_02a_integer_list_a.py)
>    //  split(), list()
> 
> b. [ExMM_A_02b_integer_list_a](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_02b_integer_list_a.py)
>    //  input().split(), append() 
> 
> b. [ExMM_A_02c_integer_list_a](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_02c_integer_list_c.py)
>    //  map(), *list 


### ExMM_A_03: integer_list_b
N個の整数を考えます。
整数の個数 $N$ が最初の行で，整数 $(A_1，A_2, ... A_N)$ が空白で区切られて続く $N$ 行で与えられます。

読み取り，整数型の`list`に変換します。 
すべての要素をカンマと空白`, `で区切り，１行で表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
A1
A2
...
AN

[Case a]  Copy the following sentences to 'execution window' !
10
8
4
9
5
3
6
0
2
7
1 

[Case b]  Copy the following sentences to 'execution window' !
6
100
130
110
140
150
120

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_03a_integer_list_b](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_03a_integer_list_b.py)
>    //  
> 
> b. [ExMM_A_03b_integer_list_b](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_03b_integer_list_b.py)
>    //  list comprehension, append() 
> 
> b. [ExMM_A_03c_integer_list_b](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_03c_integer_list_b.py)
>    //  list comprehension, *list 


### ExMM_A_04: string list
N個の文字列を考えます。
文字列の個数 $N$ が最初の行で，文字列 $(S_1，S_2, ... S_N)$ が空白で区切られて続く $N$ 行で与えられます。

読み取り，文字列型の`list`に変換します。 
すべての要素をカンマと空白`, `で区切り，１行で表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
N
S1
S2
...
SN

[Case a]  Copy the following sentences to 'execution window' !
10
alpha
bravo
charlie
delta
echo
foxtrot
golf
hotel
india
juliet

[Case b]  Copy the following sentences to 'execution window' !
6
abc
acb
bac
bca
cab
cba

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_04a_string_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_04a_string_list.py)
>    //  
> 
> b. [ExMM_A_04b_string_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_04b_string_list.py)
>    //  list comprehension, append() 
> 
> b. [ExMM_A_04c_string_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_04c_string_list.py)
>    //  list comprehension, *list 


### ExMM_A_05: character list
１この文字列 %S% が与えられます。

読み取り，文字に分解して`list`に変換します。 
すべての要素をカンマと空白`, `で区切り，１行で表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
S

[Case a]  Copy the following sentences to 'execution window' !
abcdefghij

[Case b]  Copy the following sentences to 'execution window' !
012345

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_05a_character_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_05a_character_list.py)
>    //  list()
> 
> b. [ExMM_A_05b_character_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_05b_character_list.py)
>    //  list(), *list
> 
> b. [ExMM_A_05c_character_list](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_05c_character_list.py)
>    //  list(), join() 


### ExMM_A_06: integer matrix
$H$ 行，$W$ 列の整数型マトリックス $A$ を考えます。
$H$ と$W$ が１行で，すべての整数要素が空白区切りで $H$ 行で与えられます。

読み取り，２次元`list`に変換します。 
すべての要素をカンマと空白`, `で区切り，$H$ 行で表示して下さい。
さらに，与えられたマトリックスの転置行列を作成し，同様に表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
H W
A11 A12 ... A1W
A21 A22 ... A2W
...
AH1 AH2 ... AHW

[Case a]  Copy the following sentences to 'execution window' !
6 6
0 1 2 3 4 5
5 0 1 2 3 4
4 5 0 1 2 3
3 4 5 0 1 2
2 3 4 5 0 1
1 2 3 4 5 0 

[Case b]  Copy the following sentences to 'execution window' !
6 3
0 1 2
1 2 0
2 0 1
0 1 2
1 2 0
2 0 1

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_06a_integer_matrix](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_06a_integer_matrix.py)
>    //  2-D list, list comprehension
> 
> b. [ExMM_A_06b_integer_matrix](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_06b_integer_matrix.py)
>    //  2-D list, list comprehension
> 
> b. [ExMM_A_06c_integer_matrix](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_06c_integer_matrix.py)
>    //  2-D list, list comprehension, *list 


### ExMM_A_07: character matrix
$H$ 行，$W$ 列の文字型マトリックス $S$ を考えます。
$H$ と$W$ が１行で，すべての文字要素が空白区切りで $H$ 行で与えられます。

読み取り，２次元`list`に変換します。 
すべての要素をカンマと空白`, `で区切り，$H$ 行で表示して下さい。
さらに，与えられたマトリックスの転置行列を作成し，同様に表示して下さい。

<details>
<summary>Input lines: Click here !</summary>

``` python
H W
S11 S12 ... S1W
S21 S22 ... S2W
...
SH1 SH2 ... SHW

[Case a]  Copy the following sentences to 'execution window' !
6 6
######
#.xx.#
#x..x#
#.xx.#
#x..x#
######

[Case b]  Copy the following sentences to 'execution window' !
6 3
###
#.#
#x#
#x#
#.#
###

```
注: プログラム実行後に張り付けて下さい。

</details>


>Sample programs
>
> a. [ExMM_A_07a_character_matrix](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_07a_character_matrix.py)
>    //  2-D list, list comprehension
> 
> b. [ExMM_A_07b_character_matrix](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_07b_character_matrix.py)
>    //  2-D list, list comprehension, *list
> 
> b. [ExMM_A_07c_character_matrix](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_07c_character_matrix.py)
>    //  2-D list, list comprehension, join() 




