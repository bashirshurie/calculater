number1 = eval(input("Enter number 1: "))
operation = str(input("Enter the sign: "))
number2 = eval(input("Enter number 2: "))

addition = '+'
substriction = '-'
multiply = '*'
dived = '/'

if operation == addition :
    print(number1 + number2)
elif operation == substriction :
    print(number1 - number2)
elif operation == multiply :
    print(number1 * number2)
elif operation == dived :
    print(number1 / number2)
else :
    print("I do know")