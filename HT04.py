# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = input('Номер четверти - ')
while n not in ('1','2','3','4'):
    n = input('Введите корректный номер четверти - ')
n = int(n)
if n == 1: print('0 < x < ∞ and 0 < y < ∞')
elif n == 2: print('0 > x < -∞ and 0 < y < ∞')
elif n == 3: print('0 > x < -∞ and 0 > y < -∞')
else: print('0 < x < ∞ and 0 > y < -∞')