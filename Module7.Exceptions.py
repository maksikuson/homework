#Task 1

try:
    name = str(input("Enter your name : "))
    age = int(input("Enter your age : "))
    if 0 < age < 130:
        print(f"Hello, {name}! Your age - {age}")
    else:
        raise ValueError('Incorrect age')
except ValueError as e:
    print(f'ERROR: {e}')
    
#Task 2

def userInfo(name, age):
    if 0 < age < 130:
        return f"Hello, {name}! Your age - {age}."
    else:
        raise ValueError('Incorrect age')
try:
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    result = userInfo(user_name, user_age)
    print(result)
except ValueError as e:
    print(f'ERROR: {e}')
    
    
def userInfo(name, age):
    try:
        if 0 < age < 130:
            return f"Hello, {name}! Your age - {age}."
        else:
            raise ValueError('Incorrect age')
    except ValueError as e:
        return f'ERROR: {e}'
    
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

try:
    user_age = int(user_age)
    result = userInfo(user_name, user_age)
    print(result)
except ValueError as e:
    print(f'ERROR: {e}')

#Task 3

list1 = []

for i in range(3):
    try:
        number = int(input("Enter a positive number: "))
        if number < 0:
            raise ValueError("Please enter a positive number.")
        list1.append(number)
    except ValueError as e:
        print(f"ERROR: {e}")
    else:
        print(f"Running total: {sum(list1)}")
print(f"Final list: {list1}")

#Task 4

def calculate_sum(numbers):
    return sum(numbers)

def main():
    try:
        user_input = [int(input("Enter a number: ")) for _ in range(3)]
        result = calculate_sum(user_input)
        print(f"Sum of numbers: {result}")
    except ValueError as e:
        print(f"ERROR: {e}")
        
if __name__ == "__main__":
    main()

   
def calculate_sum(numbers):
    try:
        return sum(numbers)
    except TypeError:
        raise ValueError("Invalid input. Please enter valid numbers. ")

def main():
    try:
        user_input = [int(input("Enter a number: ")) for _ in range(3)]
        result = calculate_sum(user_input)
        print(f"Sum of numbers: {result}")
    except ValueError as e:
        print(f"ERROR: {e}")
        
if __name__ == "__main__":
    main()