# boolean data type

# spam = True
# print(spam) #True

# error
# spam1 = true
# print(spam1)
# Traceback (most recent call last):
#   File "D:\ArbinBhasimaOfficial\PythonJourney\Python_Programming_Basics\Chapter2\main.py", line 7, in <module>
#     spam1 = true
#             ^^^^
# NameError: name 'true' is not defined. Did you mean: 'True'?

# True = 2 + 2
#   File "<python-input-1>", line 1
#     True = 2 + 2
#     ^^^^
# SyntaxError: cannot assign to True

# Comparison Operators

# spam1 = 2
# spam2 = 2
# spam3 = 4
# name = 'loki'
# name1 = 'thor'
# name2 = 'thor'
# print(bool(spam1 == spam2)) #True
# print(bool(spam3 == spam2)) #False
# print(bool(spam1 != spam2)) #False
# print(bool(spam3 != spam2)) #True
# print(bool(name1 == name2)) #True


# spam = 42
# trash = 123
# eggCount = 231
# print(bool(spam <= trash)) # True
# print(bool(spam >= trash)) # False
# print(bool(eggCount<=100)) # False
# print(bool(eggCount>=100)) # True

# flow control statement
# if statement
# name = 'Zion'
# age = 23
# if name == 'arbin':
#     print('Konichiwa, aniki.')
# # elif statements
# elif age < 23:
#     print('Anatawa arbin janai desu ne. Dare!.....')
# # elif age > 2000:
# #     print('Aniki wa bakemono ja nai desu!')
# # elif age > 100:
# #     print('Aniki wa kono kusobaba za nai desu!')
# # else statement
# else:
#     print('Dare yo, Omaye wa!')


# While Loop statements
# spam = 0
# if spam < 5:
#     print('Hello Bro')
#     spam = spam + 1

# name = ''
# while name != 'your name':
#     print("please type your name.")
#     name = input()
# print('Thank You!')

# with break
# while True:
#     print('Your Name: ')
#     name = input()
#     if name == 'your name':
#         break
# print('Thanks')
# while True:
#     print('Dare Desuka?')
#     name = input()
#     if name != 'zion':
#         continue
#     print('Hello, zion-tan. passwordo wa nandei? (sakana desu!) ')
#     password = input()
#     if password == 'sakanaken':
#         break
# print('Access granted.')


# for loop 
# print('Watashi no namaye')
# for i in range(5):
#     print('Manon Five Times (' + str(i) + ')')

# total = 0 
# for num in range(101):
#     total = total + num
# print(total)


# print('Watashino namaye')
# i = 0 
# while i < 5:
#     print('Manon five times (' + str(i) + ')')
#     i + i + 1
#     # whitout break is literally an infinite loop
#     break

# with range
# for i in range(12, 16):
    # print(i)
# for i in range(0, 10, 2):
#     print(i)
# for i in range(5, -1, -1):
#     print(i)

