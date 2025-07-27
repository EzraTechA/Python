# Topic Outcomes

- What is Programming language

- History of Python

- Why Python is used in hacking

- How to install Python

- What is IDE and code editor

- Creating Python script file

- Outputs and comments

- Variables and Datatypes

##  What is Programming language ?

- It is language which helps to communicate with computers {they are not able to understand human languages}

- We have a lots of languages (English, Amharic ) as same as computers have many languages too
	- Assembly, C,C++, Java, Python, Perl, GO, Python ,JavaScript

- Prog lang. Helps us to write **programs** using those languages

## What is Program ?

- It is an **algorithm** expressed in a prog lang

- An **algorithm** is a **detailed sequence of actions** to perform to accomplish some task.  Named after an Iran mathematician, Al-Khwarizmi

- Technically, an algorithm must reach a result after a finite number of steps

- With those steps Programs Do a specific task correctly

### Algorithm Example

- To ask someone, his/her name, we will do the following steps:

	1. We walk to the person
	2. Greetings
	3. Wait for answer back
	4. "What is your name?"

- There will be a lot of kinds of algorithms to a specific task


## Evolution of I/O (Input / Output)

- Early in the history of computing, programs were submitted on **punch cards with all the data** they required & executed together with other programs that used the same libraries. Output was to a **line printer**

- Later dev't  introduced **interactive processing** which allowed the user to **provide data  while the program was running**. This normally takes place in a Question & Answer format.

## Generation Of Computers

1. First Generation: Vaccum Tubes =>punch cards

2. Second Generation: Transistors => Programming started here with Assembly

3. Third Gen: Integrated Circuits => BASIC, COBOL, Pascal, Fortran, C, C++, Perl and Ada

4. Fourth Gen: Microprocessors => Python, SQL, Matlab

5. Fifth Gen: AI (Artificial Intelligence)


- They could only solve one program at a time. It would take days or even weeks to set up a new program on First Gen

### Transistors

- Small electronic Device that changed the world
### Micro Controller

- More like CPU

## Types of Programming Languages

- Computers Understand binary (0/1), humans don''t understand this.

- So based on the closeness of the language to humans we classify it into 3

- The more they become to low to the machine they are faster

- The more they become like human lang they are slower


## 1. LOW LEVEL prog lang

- These Lang are more like machines but with lots of effort people can understand them. They are close to the hardware of the computer

- Ex: Assembly


### 2. High Level Prog lang

- They are more close to humans lang.
- Ex: Python, Java, C++, JS


### 3. Medium level prog lang

- A lang which is some how closer to machines as well as human lang.

- Lang between both Low and high level .

- Ex: C-lang

## How do high level languages work


- As we saw earlier have said that computers know only **binaries**, and if we code with high level lang how do computers understand us ?
	1. Compilers: are tools which help to convert the hole code to bytecode then computer will execute it.
		Ex. C,C++,Java,...
	2. Interpreter: can directly execute the code by reading the source code line by line
		Ex. Python	
## Use of Programming lang
- Android app development
- Web development
- Machine learning
- AI
- Game development
- Big data tech
- Desktop software development
- Hacking tool development
- ...

## What is Python Programming ?

- Python is a high level & interpreted lang. => very easy to learn

- It is very simplified lang any one can write with it, also can read it

## History of Python

- It was developed by **Guido Van Rossum** in the late eighties and early nineties at the National Research Institute for Math & Computer science in the Netherlands.

- It is Derived from many other languages, including ABC ,Modula-3, C, C++, Algol-68, SmallTalk, and Unix shell and other scripting lang

- It is now maintained by a core development team at the institute, although Guido van Rossum still a vital role in directing it's progress.

### Use of python

- Data visualization
- ""  analysis
- ML
- AI
- Back-end web development (with frameworks like Django, Flask)
- Game development
- Hacking script writing

## IDE & Code Editors

- **IDE(Integrated Development Environment)**: is a software that helps to write & run a specific prog lang.
	- Ex. PythonIDE
- **Code Editors**: are software those can help to write any kind of prog lang. and also by adding some compiling/ interpreting feature they can run programs/ scripts 
	- Ex. sublime, Vscode

## Outputs and comments
- On python, to display output we use keyword 'print'
	- syntax: print(object='', sep='', end='')

```python
print("Python is powerful")

print("Python is powerful",2000, end=".")

print("Python is powerful",2000, sep="/")

print("Programming is fun \n")
```

\n: newline
\t: tab space


## Comments

- Comments won't execute

```python
# using input() to take user input 

num = input("Enter a number: ")

print("You entered:",num )
print("Data Type of num:",type(num) )
```

## Python Keywords

- Keywords are predefined, reserved word used in Python prog that have special meaning to the compiler.

Python keywords List
-------------------------------
-----------------
await      else      import      pass      False 

raise      in        except	     break	   None

return	   is	     finally	 class	   True

try	       lambda	  for	     continue	 and	

while      nonlocal   from       def         as
 
assert     del        global      not       with

async      elif       if          or       yield


## Variables

- They are a value container/holders

- They store data

- We give some value to some word

		Ex. number = 10 from this code the value of number is 10
		
- The process of giving value to word is called **Variable Declaration**

- The word that holds the data is called **Identifier**

```python

nummber = 10

print(number)

# Output: 10

print("Abebe are",number,"Years old")

# Output: Abebe are ,10, Years old


```

- We can print the variable with {variableName} on print keyword

- Syntax: print(f"our text{variable}")


```python

age = 13

print(f"abebe is {abe} years old")

# Output: abebe is 13 years old
```

**Remember!**
On naming the identifier
	a. Don't use space b/n words use _
	b. Don't use numbers as identifier


```python

my name = 13

print(f"abebe is {abe} years old")

# Output: Syntax Error
```



## Data Types

Data Types         Classes                    Description

Numeric           int, float, complex         holds numeric values
 
String             str                        holds sequence of characters

Sequence           list, tuple, range         holds collection of items

Mapping            dict                       holds data in key-value pair form

Boolean             bool                      holds either True or False

Set                 set, frozeenset           holds collection of unique items


### A. Numeric Data Type

- int(integer) - holds signed integers of non-limited length
- float - holds floating decimal points and it's accurate up to 15 decimal places
- complex - holds complex numbers
- We can identify the type of variable with keyword 'type()' 

```python

num = 5

print(num, "is of type", type(num))

num1 = 5.3

print(num1, "is of type", type(num1))

num2 = 5+2j

print(num2, "is of type", type(num2))

```


### B. String Data type

- String represented by either single or double quotes.

		Ex. var="" or var=''

```python
name = "Abel"

pring(name)

name1 = 'Alemu'

print(name1)
```


### C. Sequence Data

 
1). **Lists**

a. **List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ]. For example,  languages = ["Swift", "Java", "Python"]**

b. **To access items from a list, we use the index number (0, 1, 2 ...). For example, languages[0]**

c. **We can add/modify objects to the list, languages.append(“Amharic”)**


2) **Tuple**

- Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.
    
- we use the parentheses () to store items of a tuple. For example, product = ('Xbox', 499.99)
    
- Similar to lists, we use the index number to access tuple items in Python
    
### D.  **Dictionary data**

- **Python dictionary is an unordered collection of items. It stores elements in key/value pairs.**

- user1 = {'username':’nathan26,’password’:’p@$$word’}
    

- username and password = key
    
- nathan26 & p@$$word = value
    
- **We use keys to retrieve the respective value. But not the other way around. For example,**





	
