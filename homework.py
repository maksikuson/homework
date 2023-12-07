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

#Task 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
choose = input("Choose an operation (enter 'maximum', 'minimum' or 'average'): ")
if choose == 'maximum':
    result = max(num1,num2,num3)
    print(f"Maximum of three numbers: {result}")
elif choose == 'minimum':
    result = min(num1,num2,num3)
    print(f"Minimum of three numbers: {result}")
elif choose == 'averege':
    result = averege(num1,num2,num3)
    print(f"Averege of three numbers: {result}")
else:
    print("Invalid operation selection. Please enter 'maximum', 'minimum' or 'average'.")
    
#Task 3

meters = float(input("Enter number of meters"))
chooce = input("Select units of measurement (enter 'miles', 'inches' or 'yards'): ")
meter_to_mile = 1609.344
meter_to_inch = 0.0254
meter_to_yard = 0.9144
if chooce == 'miles':
    result = meters * meter_to_mile
    print(f"{meters} meters is {result} miles")
elif choose == 'inches':
    result = meters * meter_to_inch
    print(f"{meters} meters is {result} inches")
elif choose == 'yards':
    result = meters * meter_to_yard
    print(f"{meters} meters is {result} yard")
else:
    print("Incorrect unit selection. Please enter 'miles', 'inches' or 'yards'.")
    
#Part 2

#Task 1

day_number = int(input("Enter the number of the day of the week (1-7): "))
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= day_number <= 7:
    print(f"Day of the week with the number {day_number}: {days_of_week[day_number - 1]}") #підглянув в ChatGPT
else:
     print("Invalid input. Please enter a day number from 1 to 7.")
     
#Task 2

month_number = int(input("Enter month number (1-12)"))
month_name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if 1 <= month_number <= 12:
    print(f"Month with number {month_number}: {month_name[month_number - 1]}") #а вже тут робив підглянучи на верх
else:
    print("Invalid input. Please enter a month number from 1 to 12.")
    
#Task 3

number = float(input("Enter the number: "))

if number <0:
    print("Number is positive")
if number >0:
    print("Number is negative")
if number == 0:
    print("Number is equal to zero")
    
    
     
