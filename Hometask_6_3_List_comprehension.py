# ________List comprehension_______

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 1) 6782 -> 23;      2) 0,56 -> 11

number = input('Введите число - ')
digits_sum = sum([int(i) for i in number if i.isdigit()])
print(digits_sum)

# ---- Первоначальный вариант решения ------
# digit_sum = 0
# for i in number:
    # if i.isdigit():
        # i = int(i)
        # digit_sum += i
# print(digit_sum)


