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
    