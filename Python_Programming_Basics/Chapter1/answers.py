# Questions no 1: 
    # operators are : 
        # * , -, /, +
    # Values aare :
        # 'hello', -88.8, 5

# Question no 2:
    # variable is spam and
    # string is 'spam'

# Question no 3:
    # three data types are:
        # 1. String
        # 2. Integer
        # 3. Float
    
# Question no 4:
    # expression is made up of :
        # spam1 + spam2 = result
    # expression helps to single down the answers

# Question no 5
    # spam = 10
    # the difference between the expression and assignment statement are:
    # expression is an equation whereas assignment statement is assigning the value to its variable
    # expression is 1 + 2 = 3
    # assignment statement is spam = 12

# question no 6
    # initial value is 20 i.e bacon = 20
    # it is incremented by 1 but the value is not 
    # bacon = 20
    # print(int(bacon) + 1)
    # the answer is 21

# question no 7
    # print('spam' + 'spamspam')
    # print('spam' * 3)
    # two expression evaluates to following
    # both expression evaluates to spamspamspam

# question no 8
    # egg is a valid variable name but 100 is invalid because of the naming conventions python provides, where the egg is perfectly acceptable but the variable name cannot start 
    # with the numeric value (int or float)

# question no 9
    # the three functions which can be used to get the integer, floating-point or string values are :
    # int(), float() and string()

# question no 10
    # the following expression 
    # 'I  have eaten ' + 99 + ' burritos.'
    # throws error because the integer value 99 cannot be concatenate with the given string
    # to fix the given expression we need to 
    # add the string function
    # given
# print('I have eaten ' + 99 + ' burritos.')
print('I have eaten ' + str(99) + ' burritos.')
    # or
print('I have eaten ' + str(int(99) - 98) + ' burrito.')


# Round function round()
    # this functions rounds a number to a specified number of decimal places.
    # syntax is round(number, digits) 
print(round(3.14159)) # defaults to a zero decimal
print(round(3.1415, 2)) 
print(round(2.3)) # rounds to nearest even number - "banker's rounding"
print(round(3.7))