# Expression
from time import clock_settime


print("Arbin" +  " Bhasima") ##string exprssion

print('Hello Bro') #string single expression

print(2+2) #int expression

print(157) #int single expression


# math operators
print(5 ** 3) # exponent
print(157 % 5) # Modulus/remainder
print(160 // 10) #Integer division/floored quotient
print(120 / 10) #Devision
print(52 * 23) #Multiplication
print(123 - 122) #Subtraction
print(2+2) #Addition

# Precedence
print(2+3*6)
print((2+3)*6)
print((5-1)*((7+1)/(3-1)))

# syntax errors
# 5 + 
# 2 +- 1 not error
# 3 +* 2
# print (2 +- 1)
# print(2 +* 2)
  # File "D:\ArbinBhasimaOfficial\PythonJourney\Python_Programming_Basics\Chapter1\main.py", line 31
  #  print(2 +* 2)
  #            ^
  # SyntaxError: invalid syntax
# print(5+)
  # File "D:\ArbinBhasimaOfficial\PythonJourney\Python_Programming_Basics\Chapter1\main.py", line 36
  #   print(5+)
  #            ^
  # SyntaxError: invalid syntax


# Data types
# populors data types...
print("Arbin") # string
print(223) #int
print(23.52) #float

# String concatenation
print("bob" + "lol")
# String replication
print("bob" * 5)

# errors
# print("bob" * "lol")
# print("bob" + 1)


# string values in variables

first_name = "arbin"
last_name = "bhasima"
age = 23
print("Hi" + " I am " + first_name + " " + last_name + ". I am " + str(age) + " years old. " )

# str(age) -> age int converted to string

spam = 42
spam1 = "spiderman"
spam2 = " is hero."
print(spam + 23)
print(spam1 * 2)
print(spam1 + spam2)

health_bar = 100 # initialized
attack_damage = 23.345
new_health_bar = float(health_bar - attack_damage)
print(new_health_bar)
health_bar = new_health_bar #overwriting
print(health_bar)


# Varible Naming Conventions

# Correct Naming Conventions
# moviename
# movie_name
# movie1
# and more

# Incorrect Naming Conventions
# 1moviename
# movie name
# movie$asdad





