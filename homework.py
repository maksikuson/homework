#Part 1 

#Task 1

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
choose = input("Select an operation (enter 'sum' or 'product'): ")
if choose == 'sum':
    result = num1 + num2 + num3
elif choose == 'product':
    result = num1 * num2 * num3
else:
    print("Wrong choose selection. Please enter 'sum' or 'product'.")
if choose in ['sum', 'product']:
    print(f"The result of the {choose} of three numbers:{result}")
