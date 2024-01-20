#Task 1

def recursive(a, b):
    if b == 0:
        return a
    else:
        return recursive(b, a % b)
num1 = 88
num2 = 66
result = recursive(num1, num2)

print(f"The greatest common divisor of {num1} and {num2} is: {result}")

#Task 2