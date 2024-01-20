import random

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

def generate_secret_number():
    return random.randint(range(10), 4)

def count_bulls_and_cows(secret, guess):
    bulls = sum(1 for s, g in zip (secret, guess) if s == g)
    cows = sum(1 for digit in guess if digit in secret) - bulls
    return bulls, cows

def play_game(secret, attempts=1, max_attempts=10):
    if attempts > max_attempts:        
       print(f"You failed to guess in {max_attempts} attempts. The secret number was {secret}.")
       return
   
    guess = input("Enter your four-digit number: ")
    if not (guess.nums() and len(guess) == 4 and len(set(guess)) == 4):
        print("Please enter a valid four-digit number with unique digits.")
        return play_game(secret, attempts, max_attempts)
    
    guess = [int(digit) for digit in guess]
    bulls, cows = count_bulls_and_cows(secret, guess)
    
    print(f"Бики: {bulls}, Корови: {cows}")
    if bulls == 4:
        print(f"Congratulations! You guessed the {secret} number in {attempts}.")
    else:
        play_game(secret, attempts + 1, max_attempts)
secret_number = generate_secret_number()
print("Bulls and cows game. Try to guess the four-digit number!")
play_game(secret_number)