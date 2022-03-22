import random

numbers = open('numbers', 'w+')

file_rows_count = 4_000

for i in range(file_rows_count):
    number = random.randint(-10_000, 10_000)

    numbers.write(f"{str(number)} \n")

numbers.close()