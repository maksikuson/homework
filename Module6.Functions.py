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
    # Генерує чотиризначне випадкове число без повторень цифр
    return random.sample(range(10), 4)

def count_bulls_and_cows(secret, guess):
    # Підраховує кількість биків і корів у вгаданому числі
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for digit in guess if digit in secret) - bulls
    return bulls, cows

def play_game(secret, attempts=1):
    # Головна функція гри
    guess = input("Введіть ваше чотиризначне число: ")
    
    # Перевірка правильності введеного числа
    if not guess.isdigit() or len(guess) != 4:
        print("Будь ласка, введіть чотиризначне число.")
        return play_game(secret, attempts)

    guess = [int(digit) for digit in guess]
    
    # Підрахунок биків і корів
    bulls, cows = count_bulls_and_cows(secret, guess)
    print(f"Бики: {bulls}, Корови: {cows}")

    # Перевірка, чи вгадано число
    if bulls == 4:
        print(f"Ви вгадали число за {attempts} спроб!")
    else:
        # Рекурсивний виклик для наступної спроби
        play_game(secret, attempts + 1)

if __name__ == "__main__":
    # Генеруємо випадкове чотиризначне число для вгадування
    secret_number = generate_secret_number()

    print("Гра 'Бики і корови'. Спробуйте вгадати чотиризначне число!")

    # Запускаємо гру
    play_game(secret_number)