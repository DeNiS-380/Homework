import random

number = random.randint(3, 20)
pairs = []

for i in range(1, number):
    if number % i == 0:
        pairs.append((i, number - i))

result = ""
for pair in pairs:
    result += str(pair[0]) + str(pair[1])

print("Число в первой вставке:", number)
print("Пары чисел для второй вставки:", result)