# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число - '))

f = [1,1]
for i in range(2, num):
    f.append(f[i-1] + f[i-2])
    
n_f = [1,-1]
for i, elem in enumerate(f,2):
    if i%2!=0:
        n_f.append(elem*(-1))
    else:
        n_f.append(elem)
        
n_f.reverse()
n_f.append(0)
print(f + n_f)