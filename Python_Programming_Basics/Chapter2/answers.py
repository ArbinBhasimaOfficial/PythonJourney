# Question no 1
    # The Two types of Boolean Data type is :
        # true
        # false
    
    # The way of writing those data types are
        # True
        # False

# Question no 2
    # the three boolean operators are:
        # Binary Boolean Operators
        # and 
        # or
        # not

# Question no 3
    # truth table of each boolean table

    # and
    # The and Operator's Truth table
    #         Expression      Evaluates to...
    #         True and True   True
    #         True and False  False
    #         False and True  False
    #         False and False False

    # or
    # The or Operator;s Truth Table
    #         Expression      Evaluates to...
    #         True or True    True
    #         True or False   True
    #         False or True   True
    #         False or False  False

    # not
    # The not Operator's Truth Table
    #         Expression      Evaluates to...
    #         Not True        False
    #         Not False       True

# Questions no 4
    # (5 > 4) and (3 == 5)
        # this expression evaluates to 5 is greater than 4 (which is true) and 3 is equal to 5 (which is false) that is True and False so the evaluated answer is False.

    # not (5 > 4)
        # this express that the 5 is greater than 4 (which is true) so the expression becomes not true so it evaluates to False.

    # (5 > 4) or (3 == 5)
        # this expresses that the 5 is greater than 4 (which is true) or 3 is equal to 5 (which is false) that is True or False so the evaluated answer is True.

    # not ((5 > 4) or (3 == 5))
        # this expresses that the 5 is greater than 4 (which is true) or 3 is equal to 5 (which is false) that is True or False so the evaluated answer is True.
        # but there is not operator so the evaluated answer becomes False.

    # (True and True) and (True == False)
        # this expresses that the True and True which is True and True == False which is false so the expression becomes True and False so it evaluates to the False.

    # (not False) or (not True)
        # this expresses that the not False which is True or not True which is False so the expression is Truw or False so it evaluates to True.

# Questions no 5

    # the six comparison operators are following:
        # Operator    Meaning
        # ==          Equal to
        # !=          Not Equal to
        # <           Less than
        # >           Greater than
        # <=          less than or equal to
        # >=          Greater than or eual to

# Question no 6
    # The difference between equal to and assignment operator is given below
        # Assignment (=) vs Equality (==)

        # Assignment (=) — Stores a value in a variable
        # x = 10      # "x gets the value 10"
        # name = "Arbin"  # "name gets 'Arbin'"

        # Equality (==) — Compares two values, returns True or False
        # x == 10    # "Is x equal to 10?" → True or False
        # name == "Arbin"  # "Is name equal to 'Arbin'?" → True or False

        # Quick mnemonic:
        # - = → "is assigned" (goes one way → into the variable)
        # - == → "equals" (compares both ways ←→)

        # Common mistake:
        # # Wrong - assigns instead of comparing
        # if x = 10:    # SyntaxError!

        # # Correct - compares
        # if x == 10:

# Question no 7
    #  the condition is the statmente which we use inside the while loop and for loop to make it able to skip the loop and go stright to the start of the loop
    # while True:
                # print('Dare Desuka?')
                # name = input()
                # if name != 'zion':
                #     continue
                # print('Hello, zion-tan. passwordo wa nandei? (sakana desu!) ')
                # password = input()
                # if password == 'sakanaken':
                #     break
                # print('Access granted.')

# Question no 8
    #  the three blocks in the given code are : 
        # spam = 0 # this is first block
        # if spam == 10: # this is first block
            # print('eggs') # this is first block
            # if spam > 5: this is second block
                # print('bacon') this is second block
            # else: this is third block
            #     print('ham') this is third block
            # print('spam') this is second block
        # print('spam') # this is first block

# Question no 9
    # code is given bellow:
    # spam = 3
    # if spam == 1:
    #     print('Hello')
    # elif spam == 2:
    #     print('Howdy')
    # else:
    #     print('Greetings')


# Question no 10
    # you can press CTRL-C if program is stuck in an infinite loop

# Question no 11
    # The difference between break and continue are
    # break statement is used to terminate the loop where as continue statement is used to go to the start of the loop
    # break keyword is used in break statement where as continue keyword is used in continue statement

# Question no 12
    # The difference between range(10), range(0,10), and range(0, 10, 1) are following 
    # for i in range(10):
    #     print(i) # answer is 0 to 9
    # for i in range(0,10):
    #     print(i) # answer is 0 to 9
    # for i in range(0, 10, 1):
    #     print(i) # answer is 0 to 9
# the difference is that the int range(10) there are no starting and stepping values tho it counts as  0 and 1 itself
# the difference is that the int range(0,10) there are no stepping values tho it counts as 1 itself
# the difference is that the int range(0, 10, 1) there all the values given

# Question no 13
    #  a short program is given bellow
    #  using for loop
    # for i in range(1, 11, 1):
    #     print(i)

    # using while loop
    # i = 1
    # while True:
    #     print(i) 
    #     i = i + 1
    #     if i == 11:
    #         break

# Qusetion no 14
    # importing bacon() from spam
    # from spam import bacon
    # or
    # from spam import *

    # after importing bacon()
    # we call the function like this 
    # spam.bacon()


# round() and abs() in Python

#   round(number, ndigits) — Rounds a number to specified decimal places
#   round(3.14159)       # 3
#   round(3.14159, 2)    # 3.14
#   round(2.5)           # 2  (rounds to even)
#   round(1.9)           # 2

#   abs(number) — Returns the absolute (positive) value
#   abs(-5)    # 5
#   abs(10)    # 10
#   abs(-3.14) # 3.14
#   abs(0)     # 0

#   Practical example — rounding without round():
# import math
# price = 19.99
# rounded = math.floor(price)  # 19
#   # or
# rounded = int(price)  # 19 (truncates, doesn't round)

#   Both are built-in functions — no import needed.

# Program: Temperature Converter with abs() and round()

print("=== Temperature Converter ===")

  # User inputs
celsius = float(input("Enter temperature in Celsius: "))
  
  # Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

  # Calculate the difference from freezing point (0°C)
difference = celsius - 0
abs_difference = abs(difference)

  # Display results
print(f"\nFahrenheit: {round(fahrenheit, 2)}°F")
print(f"Difference from freezing: {abs_difference}°")
print(f"Rounded difference: {round(abs_difference)}°")

  # Show how abs() handles negative temperatures
if celsius < 0:
    print(f"\nThe absolute value of {celsius} is {abs(celsius)} — it's {abs_difference} degrees below freezing!")
else:
    print(f"\nThe absolute value of {celsius} is {abs(celsius)}")