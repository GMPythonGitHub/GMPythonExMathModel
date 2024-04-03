# **Exercises for Math Model A: input and output**
#### 数値や文字列データの入出力に関する演習問題です。

### ExMM_A_00: integer，float, and string
整数Aと実数B，文字列Cがそれぞれ１行ごとに与えられます。これらを関数`input()`を用いて入力し，さらに変数に変換します。 
それらを`print()`を用いて１行毎に表示して下さい。

```
--- list of input lines ---
[Case a]  copy the following sentences to 'execution window'
12345
123.45
abcde

[Case b]  copy the following sentences to 'execution window'
1234500000
0.00012345
abc de
```
柱: プログラムを実行後に，入力リストを実行ウィンドウに張り付けます。

>解答例：
>- [ExMM_A_00a_integer_float_string](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_00a_integer_float_string.py)
>  - input(), int(), float(), print()
>- [ExMM_A_00b_integer_float_string](https://github.com/GMPythonGitHub/GMPythonExMathModel/blob/main/ExMathModel_A_Input_and_Output/ExMM_A_00b_integer_float_string.py)
>  - f-string 

### ExMM_A_01: integers
６個の整数 (A
<sub>1</sub>, A
<sub>2</sub>...，A
<sub>6</sub>) が空白`' '`で区切られて１行で与えられます。これらを読み取り，整数型変数に変換します。 
それらをカンマと空白`, `で区切り，１行で表示して下さい。

```
--- list of input lines ---
[Case a]
4 5 3 0 2 1 

[Case b]
100 130 110 140 150 120
```

>解答例：
>- [ExMM_A_01_integers](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_01_integers.py)
>  - input(), int(), float(), print()
>- [ExMM_A_01a_integers](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_01a_integers.py)
>  - map(), f-string 

### ExMM_A_02: integer_list_a
N個の整数を考えます。
整数の個数Nが最初の行で，続いての整数 (A
<sub>1</sub>, A
<sub>2</sub>...，A
<sub>N</sub>) が空白`' '`で区切られて１行で与えられます。これらを読み取り，整数型の`list`に変換します。 
そのすべての要素をカンマと空白`, `で区切り，１行で表示して下さい。

```
--- list of input lines ---
[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
6
100 130 110 140 150 120

```

>解答例：
>- [ExMM_A_02_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_02_integer_list_a.py)
>  - split(), list()
>- [ExMM_A_02a_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_02a_integer_list_a.py)
>  - input().split(), append() 
>- [ExMM_A_02b_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_02b_integer_list_a.py)
>  - map(), *list


## ExMM_A_03: integer_list_b
N個の整数を考えます。
整数の個数Nが最初の行で，続いての整数 (A
<sub>1</sub>, A
<sub>2</sub>...，A
<sub>N</sub>) がN行で与えられます。これらを読み取り，整数型の`list`に変換します。 
そのすべての要素をカンマと空白`, `で区切り，１行で表示して下さい。

```
--- list of input lines ---
[Case a]
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

[Case b]
6
100 
130 
110 
140 
150 
120

```

>解答例：
>- [ExMM_A_03_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_03_integer_list_b.py)
>  - ---
>- [ExMM_A_03a_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_03a_integer_list_b.py)
>  - list comprehension, append() 
>- [ExMM_A_032_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_for_Math_Model_A_Input_and_Output/ExMM_A_03b_integer_list_b.py)
>  - list comprehension, *list



