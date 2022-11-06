# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from unicodedata import digit

number = input('Введите число - ')
digit_sum = 0
for i in number:
    if i.isdigit():
        i = int(i)
        digit_sum += i
print(digit_sum)

