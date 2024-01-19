def add(a, b):
    return a + b

def add(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

def perform_calculation():
    input_value = int(input('Enter the first value: '))
    input_value2 = int(input('Enter the second value: '))
    input_operator = input ('Enter the operator: ')
    
    if input_operator == '+':
        result = add(input_value, input_value2)
    elif input_operator == '-':
        result = subtract(input_value, input_value2)
    elif input_operator == '*':
        result = multiply(input_value, input_value2)
    elif input_operator == '/':
        result = divide(input_value, input_value2)
    else:
        result = "Invalid operator"
        
    print("Result: ", result)

perform_calculation()