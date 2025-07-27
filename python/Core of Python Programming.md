## **Topics**
- Indexing and slicing {start, stop, step}
- Input handling {2 methods}
- Operations
- Indentation
- If else
- Errors (Exceptions)
- Error handling
- Loops

## Indexing
- On lists, we have seen about index numbers


```python
languages = ["Python", "swift", "C++"]
```

		"python"      "Swift"      "C++"
Index      0           1         2

- Negative Indexing

		"python"      "Swift"      "C++"
Index      0           1         2
negative   -3         -2         -1

**Note: The list index always starts with 0. Hence, the first element of a list is present at index 0, not 1.**

```python
languages = ["Python", "swift", "C++"]

print(languages[-3]) #Python
print(languages[-1]) #C++

```

- Calling texts by indexes also works for strings & tuples

## Slicing

- Slicing is indexing syntax that extracts a portion from a list. If a is a list, then a[m : n] returns the portion of a:
	- Starting with position m
	- Up to but not including n
	- Negative indexing can also be used
- Python uses default step as 1, sometimes no need to tell/put it
- Also default stopping index is the final , still no need to tell for this kinda purpose
- Syntax:
		 - Mylist[start:stop:step]

```python
name = "Abebe beso bela"

print(name[10::])

# bela


stud = "hello students"

print(stud[:-9:])
# hello

country = ["eth","chi","ame","jap"]

print(country[-1:0:-2])

# ['jap', 'chi']

country = ["eth","chi","ame","jap"]

print(country[::-1])

# ['jap', 'ame', 'chi', 'eth']

country = ["eth","chi","ame","jap"]

print(country[::-2])

#['jap', 'chi']

```

## User input handling

- ON python there are 2 types of inputs
	- By input function
	- By Arguments
1. By input function
	- Syntax: var = input("Text you like to display)
	- Will accept input and stores on variable
```python
name = input("What is your name ? \n name: ")
print(f"Hello {name}!")
#What is your name ?
 #name: abebe
 #Hello abebe!

```

- We can change the input type to int()
, float() ,eval(), str()
- By default the input type is string
```python
number1 = input("Enter Number: ")
print(type(number1))

# Enter Number: 12
# <class 'str'>  

number2 = int(input("Enter Number: "))
print(type(number2))

# Enter Number: 12
# <class 'int'>

number3 = float(input("Enter Number: "))
print(type(number3))

# Enter Number: 12
# <class 'float'>

number4 = eval(input("Enter Number: "))
print(type(number4))

# Enter Number: 12
# <class 'int'>

```

2. Arguments
	- This help us to get the input from the command line
	- Shell: python abebe.py arg1 arg2 arg3
	- Syntax: 
```python
import sys
name = sys.argv[1]
print(f"hello {name}!")
# to execute this code we should to use ->  python test.py Abebe Alemu

# we can do more inputs
firstname = sys.argv[1]
lastname = sys.argv[2]
print(f"Hello {firstname}!, your father name is:{lastname}")
# to execute this code we should to use ->  python test.py Abebe Alemu

```

- We can create a variables until n times

## Exercise

```python
users = ['Nathan',2313,'Geez','pass231','Abebe','092313133','Miki',"pl3s34D0n'tH4ckM3"]

UN = users[::2]

PS = users[1::2]

print("The usernames are: ",UN)

print("The Passwords are: ", PS)

user = {"abebe":"123", "kebede":"pass123", "abel":"dsi1"}

nameInput =input("Your name: ")

print(f"your password is {user[nameInput]}")
```
## Operators
- They are special symbols that perform operations on variable and values, For example  print(5 + 6)  #11
- There are lots of operators type on python:

	1. Arithmetic Operators
	2. Assignment Operators
	3. Comparison Operators
	4. Logical Operators
	5. Bitwise Operators
	6. Special Operator
## 1. **Arithmetic Operators**

- They are simply math Operators
- Inputs have to be in int, eval, float only
- It includes:
	- Addition         +
	- Subtraction      -
	- Multiplication   * 
	- Division         /
	- Modulo            %
	- Power            **

 
```python
a = 8

b = 7

print(a+b)
# 15
print(a-b)
# 1
print(a*b)
# 56
print(a/b)
# 1.1428571428571428
print(a**b)
# 2097152
print(a%b)
# 1
```

## 2. **Assignment Operators**

- They are used to assign Values to variables.
- We put the arithmetic operators first ,then equal sign
- It includes:
	- Assignment Operators =           
	- Addition Assignment  +=
	- Subtraction Assignment  -=
	- Multiplication Assignment  * =
	- Division Assignment  /=
	- Remainder Assignment  %=
	- Exponent Assignment  ** =

```python
d = 10
b = 5
d += b
print(d) # 15
d -= b
print(d) # 5
d *= b
print(d) # 50
d /= b
print(d) # 2.0
d %= b 
print(d) # 0
d **= b
print(d) # 100000
```

## 3. **Comparison Operators**

- Used to compare  variables and return boolean result
- Boolean means either **True** or **False**
- It includes:
	- Is equal to                  ==
	- Not equal to                 !=
	- Greater than                  >
	- Less than                     <
	- Greater than  or equal to    >=
	- Less than  or equal to       <=

```python
f = 32

v = 76
print(f == v) # False

print(f != v) # True

print(f < v) # True

print(f > v) # False

print(f >= v)  # False

print(f <= v)  # True
```

## 4. **Logical Operators**

- They are used to check if an expression is **True** or **False**
- They use Truth table to compare
- It includes:
	- and        Logical AND: True if both operands are true
	- or         Logical OR: True if at least one of the operands is true
	- not        Logical NOT: True if the operand is false and vice-versa
### Truth Table for and (&&)

- Only **True** and **True** is **True**

A        B        A and B

True     True     True
True     False    False
False    True     False
False    False    False

### Truth Table for or (||)

- Only **False** and **False** is **False**

A        B        A and B

True     True     True
True     False    True
False    True     True
False    False    False

### Truth Table for or (||)

- It is just opposite

A        not A
True     False
False    True

## 5. **Bitwise Operators**

- On our computer everything have a binary value. (also called bit)
- On python there is a keyword called bin(Your decimal) this helps to show you the binary value of Your decimal
- **True** have a value of **1**
- **False** have a value of **0**
- **Bitwise Operators used to do math (Logical operations) o the binary value of the expression.**
- They are 
	- Compliment(Not)(~)
	- And(&)
	- Or(|)
	- Xor(^)
	- Left Shift(<<)
	- Right Shift(>>)
- **It is must in Cryptography.**

```python
print(bin(33)) # 0b100001
```

### Compliment(NOT) (~)

- It changes the number to binary, flips each bit, then converts it back to decimal
- It add will add 1 to the number and then makes it negative

~12  =>   -(12+1)   = -13
~4   =>   -5 
```python

print(~3) # -4

```

### And (&)

- We can add 0 before the binary of any number if it is not 4 digit binary 
- bin(7) -> 111, but we can do 0111 too
10&7

10 -> 1010
	  &&&&
7 ->  0111	
__________
	AND   0010    == 2 
```python

print(10&7) #2

```

### OR

- Same as And but the logic operator will be changed.

10 & 7

10 -> 1010
	  ||||
7 ->  0111	
____
OR    1111      == 15

```python

print(10 | 7) # 15
 ```

### XOR (^)

- It is like And, Or but the difference is the logic here is
	- If there are same = 0     1 ^ 1 = 0, 0 ^ 0 = 0
	- If they are different = 1   1 ^ 0, 0 ^ 1 = 1

10 & 7
10 -> 1010
	  ^^^^
7 ->  0111

---- 

XOR    1101    == 13

```python

print(10 ^ 7)  # 13

```

### Left Shift

- Every Numbers have .0 at the end => 1.0, 32.0

10 << 2 - shifting 2 bits to the left 

10 -> 1010.==00==00
      101000.00
  --------------
<<    101000   == 40   


```python
print(10 << 2) # 40
```

### Right Shift (>>)

- It is the opposite of Left Shift

10 >> 2 -  shifting 2 bits to the right

10 ->  10==10==.0000
       10.100000
-----------------
 >>  10        == 2

## Indentations

- Are just a White Space which python uses for some of it's function. 

**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdzgxTbL150fTGh9_iT7KUrBznVuk3o58PWwpFrPLdo4PV7lZTsuNx2Tfgzqc5g2g-HU8EyTqpS1oI77b3K6NhcZLVDTeZvN91PyNiDP1W-x7txBn-mJFauXJhfSygs1HJ1KQzXjHds2kRhiFQzJ55LknABvza2=s2048?key=i39BOw0JvvqB6u0vuqPFIg)**

## If-Else Conditions

- In programming, an **if statement** runs code only when a condition is true. 
- For example, we can assign grades based on mars:
	- Above 90  ->  Grade A
	- Above 75 → Grade B
    - Above 65 → Grade C
 - Python supports three forms:
	 - if
	 - if ... else
	 - if ... elif ... else

### If statement

- 