expression = input("what math do you want to do? " )
parts = expression.split(" ")

if len(parts) == 3:
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result= round((num1 + num2), 1)
    elif operator == '-':
        result=round((num1 - num2), 1)
    elif operator == '*':
        result= round((num1*num2), 1)
    elif operator == '/':
        if num2 != 0:
            result = round((num1/num2), 1)
        else:
            result = "Enter a number greater than 0"
    else:
        result = "enter valid operator"
else:
    result = "Invalid input format"

print(result)
















