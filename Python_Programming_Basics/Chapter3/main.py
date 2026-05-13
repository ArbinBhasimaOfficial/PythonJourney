# # hello function
# def hello():
#     print('howdy!')
#     print('howdy!!')
#     print('moshi moshi!')

# hello()
# hello()
# hello()

# hello function 2
# def hello(name):
#     print('konichiwa ' + name)

# hello('Zion')
# hello('Arbin')

# spam = print('Hello')
# None == spam


# local variables cannnot be used in global scope

# def spam():
#     eggs = 34337

# spam()
# print(eggs)
# Traceback (most recent call last):
#   File "D:\ArbinBhasimaOfficial\PythonJourney\Python_Programming_Basics\chapter3\main.py", line 28, in <module>
#     print(eggs)
#           ^^^^
# NameError: name 'eggs' is not defined

# local scopes cannot use variables in other local scopes

# def spam():
#     eggs = 99
#     bacon()

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# this program does nothing

# Global variables can be read from a local Scope

# def spam():
#     print(eggs)

# eggs = 42
# spam()
# print(eggs)


