# this is first program

print("Hello World1")
print('What is you name?')
myName = input()
# input() functions means making giving an input available  


print('It is a pleasure to meet you, '+ myName)
print('The length of your name is: ')
print(len(myName))
# len() => length of string 

print('What is your age?')
myAge = input()
print(' You will be ' + str(int(myAge) + 1) + ' in a year.')

print()

# error

# print ('I am ' + 29 + 'Years Old.')
# Traceback (most recent call last):
#   File "D:\ArbinBhasimaOfficial\PythonJourney\Python_Programming_Basics\Chapter1\firstprogram.py", line 22, in <module>
#     print ('I am ' + 29 + 'Years Old.')
#            ~~~~~~~~^~~~
# TypeError: can only concatenate str (not "int") to str
# fix
print('i am ' + str(24) + ' y.o.')
print(int('223'))
print( float('3.14213131224124'))

spam = input()
print(int(spam) * 10 / 5)
int(7.7)
print(int(7.7)+1)