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