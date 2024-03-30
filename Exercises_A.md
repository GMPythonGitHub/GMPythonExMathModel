# **Exercises A: input and output**
### 数値や文字列データの入出力に関する演習問題です。

## Ex_A_00: integer，float, and string
整数Aと実数B，文字列Cがそれぞれ１行ごとに与えられます。これらを関数`input()`を用いて入力し，さらに変数に変換します。 
それらを`print()`を用いて１行毎に出力して下さい。

```
--- list of input lines ---
[Case a]
12345
123.45
abcde

[Case b]
1234500000
0.00012345
abc de
```
３行をターミナルウィンドウに張り付けることによって入力します。

>解答例：
>- [Ex_A_00_integer_float_string](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_00_integer_float_string.py)
>  - input(), int(), float(), print()
>- [Ex_A_00a_integer_float_string](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_00a_integer_float_string.py)
>  - f-string 


## Ex_A_01: integers
６個の整数 (A
<sub>1</sub>, A
<sub>2</sub>...，A
<sub>6</sub>) が空白`' '`で区切られて１行で与えられます。これらを読み取り，整数型変数に変換します。 
それらをカンマと空白`, `で区切り，１行で出力して下さい。

```
--- list of input lines ---
[Case a]
4 5 3 0 2 1 

[Case b]
100 130 110 140 150 120
```

>解答例：
>- [Ex_A_01_Integers](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_01_Integers.py)
>  - input(), int(), float(), print()
>- [Ex_A_01a_Integers](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_01a_Integers.py)
>  - map(), f-string 

## Ex_A_02: integer_list_a
N個の整数を考えます。
整数の個数Nが最初の行で，続いての整数 (A
<sub>1</sub>, A
<sub>2</sub>...，A
<sub>N</sub>) が空白`' '`で区切られてN行で与えられます。これらを読み取り，整数型の`list`に変換します。 
それらをカンマと空白`, `で区切り，１行で出力して下さい。

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
>- [Ex_A_01_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_02_integer_list_a.py)
>  - split(), list()
>- [Ex_A_01a_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_02a_integer_list_a.py)
>  - input().split(), append() 
>- [Ex_A_01b_integer_list_a](https://github.com/GMPythonGitHub/GMPython_Exercises_for_Math_Model/blob/main/Exercises_A_Input_and_Output/Ex_A_02b_integer_list_b.py)
>  - map(), *list



