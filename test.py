# print("Welcome to GTST")
# # print("abebe")
# # abebe = ["python","swift","java"]
# # print(abebe[-1])

# # name = ("hello", 32,23)

# # print(name[1])

# # # 32

# # fname="Abebe"
# # print(fname[2])
# # # e
# # name = "Abebe beso bela"
# # print(name[10::])

# # stud = "hello students"
# # print(stud[:-9:])

# # country = ["eth","chi","ame","jap"]
# # print(country[::-1])

# # # ['jap', 'chi']

# # country = ["eth","chi","ame","jap"]
# # print(country[::-2])

# #['jap', 'chi']


# # name = input("What is your name ? \n name: ")
# # print(f"Hello {name}!")
# #What is your name ?
#  #name: abebe
#  #Hello abebe!

# # number1 = input("Enter Number: ")
# # print(type(number1))

# # number2 = int(input("Enter Number: "))
# # print(type(number2))
# # # Enter Number: 12
# # # <class 'int'>
# # number3 = float(input("Enter Number: "))
# # print(type(number3))
# # # Enter Number: 12
# # # <class 'float'>
# # number4 = eval(input("Enter Number: "))
# # print(type(number4))
# # Enter Number: 12
# # <class 'int'>
# # import sys
# # name = sys.argv[1]
# # print(f"hello {name}!")

# # firstname = sys.argv[1]
# # lastname = sys.argv[2]
# # print(f"Hello {firstname}!, your father name is:{lastname}")
# # users = ['Nathan',2313,'Geez','pass231','Abebe','092313133','Miki',"pl3s34D0n'tH4ckM3"]
# # UN = users[::2]
# # PS = users[1::2]
# # print("The usernames are: ",UN)
# # print("The Passwords are: ", PS)
# # user = {"abebe":"123", "kebede":"pass123", "abel":"dsi1"}
# # nameInput =input("Your name: ")
# # print(f"your password is {user[nameInput]}")
# # a = 8

# # b = 7

# # print(a+b)
# # # 15
# # print(a-b)
# # # 1
# # print(a*b)
# # # 56
# # print(a/b)
# # # 1.1428571428571428
# # print(a**b)
# # # 2097152
# # print(a%b)
# # # 1

# # d = 10
# # b = 5
# # # d += b
# # # d -= b
# # # d *= b
# # # d /= b
# # # d %= b
# # d **= b

# # print(d)

# # f = 32
# # v = 76

# # print(f == v) # False
# # print(f != v) # True
# # print(f < v) # True
# # print(f > v) # False
# # print(f >= v)  # False
# # print(f <= v)  # True

# # print(bin(33)) # 0b100001

# # print(~3)
# # print(10 | 7)
# # print(10 ^ 7)

# # print(10 << 2)

# # number = 10 
# # if number > 0:
# #     print("Number is greater than 0")
# # marks = 98

# # if marks >= 75:
# #     print("Passed with Distinction")
# # else:
# #     print("Failed keep trying")

# # score = 80
# # if score > 90:
# #     print("Grade A")
# # elif score > 75:
# #     print("Grade B")
# # elif score > 65:
# #     print("Grade C")
# # else:
# #     print("Grade D")    
# age = 20


# # if age >= 18:
# #     if age > 0:
# #         print("Access granted")

# # userInput = int(input("Enter a number: "))
# # if userInput == "":
# #     print("nothing inserted!")
# # else:
# #     try:
# #         if userInput % 2 == 0:
# #              print("Even number")
# #         else:
# #              print("Odd number")    
# #     except ValueError:
# #            print("Please enter a valid number")

# # try:
# #     num = int(input("Enter a number: "))
# #     result = 100 / num
# #     print(f"The result is: {result}")
# # except ZeroDivisionError:
# #     print("You cannot divide by zero!")
# # except ValueError:
# #     print("Please enter a valid number!")    

# # languages = ["Python", "Java", "C++", "JavaScript"  ]
# # for lang in languages:
# #     print(lang)

# # allusers = {'Nathan': '2313',
# #     'Geez': 'pass231',
# #     'Abebe': '092313133',
# #     'Miki': "pl3s34D0n'tH4ckM3"}

# # attempts = 0
# # max_attempts = 5

# # while attemps < max_attempts:
# #     username = input("Enter your username ")
# #     password = input("Enter your password ")

# #     if alluser in allusers:
# #         if allusers[alluser] == password:
# #             print("Welcome to GTST")
# #             break
# #         else:
# #             print("Incorrect Login!")
# #      else:
# #         print("Incorrect Login!")
# #     attempts += 1
# #     if attempts == max_attempts:
# #         print("Sorry you are limited")
# # another method
# user = {'Nathan': '2313',
#     'Geez': 'pass231',
#     'Abebe': '092313133',
#     'Miki': "pl3s34D0n'tH4ckM3"}

# for i in range(5):
#     username = input("Enter Username: ")
#     password = input("Enter password: ")

#     if username in user and password == str(user[username]):
#         print("Welcome to Our company!")
#         break
#     else:
#         print("Incorrect Login!")
# else:
#     print("Soory you are limited")

# def student():
#     print("learn")
#     print("ask")
#     print("do exercise")
    

# def teacher():
#     print("teach")
#     print("answer ")
#     print("prepare exercise")
    
# student()
# teacher()
    
# def add(x, y):
#     return x + y
# result = add(3 ,4)
# print("The sum is ", result)        

# def greet_user():
#     fname = input("Enter your name")
#     lname = input("Enter father your name")
#     return fname + " " + lname
# fullname = greet_user()
# print("hello",fullname )    

# def power(num1, num2):
#     return num1 ** num2
# result = pow(4,2)    
# print(result)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)    
result = factorial(5)
print("Factorial of 5 is: ", result)        


