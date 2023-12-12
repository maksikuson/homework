#Part 1

#Task 1

num1 = int(input("Enter start of range : "))
num2 = int(input("Enter end of range : "))
for number in range(num1, num2 + 1):
    if number %7 == 0:
        print(number)
        
#Task 2

num1 = int(input("Enter start of range : "))
num2 = int(input("Enter end of range : "))
print("All number of the area:")
for number in range(num1, num2 + 1):
    print(number,      )
    
#я не знаю як це робити(
     
#Task 3

num1 = int(input("Enter start of range : "))
num2 = int(input("Enter end of range : "))
for number in range(num1, num2 + 1):
    result = "Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0)
    print(result if result else number)






