# 1. Вычислить число c заданной точностью *d*
#     *Пример:*  - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = float(input('Введите число с искомой точностью - '))       # для упрощения задаю сразу
print(pi)
d = str(d)      # перевожу оба числа(float) в строки, чтобы перевести к единой длине
p = str(pi)
l = len(d)      # нахожу искомую длину
print(p[:l])    # срез строки по нужной длине

#  --------- варианты решения из семинара --------
# d =  input('Введите число для заданной точности числа Пи: ')
# d = len(str(d).split('.')[1])
# # print(f'число Пи с заданной точностью "{d} знак" равно {round(pi, d)}')
# # -----

# ---------- след вариант ---------

# print('pi->', int(pi / d) * d)
# # этот же код подробнее
# from math import pi
# d = 0.000000001
# print(pi / d)
# print(int(pi / d))
# print(int(pi / d) * d)
# print('pi->', int(pi / d) * d)
