import random

def generate_random_number(start, end):
    return random.randint(start, end)

# Задаем диапазон
start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

random_number = generate_random_number(start_range, end_range)
print(f"Случайное число в диапазоне [{start_range}, {end_range}]: {random_number}")
