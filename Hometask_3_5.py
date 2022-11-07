# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

input_number = int(input('Введите число - '))

fibonacci = [1,1]
for i in range(2, input_number):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

nego_fibonacci = [1,-1]
for i, elem in enumerate(fibonacci,2):
    if i%2!=0:
        nego_fibonacci.append(elem*(-1))
    else:
        nego_fibonacci.append(elem)
   
nego_fibonacci.reverse()
nego_fibonacci.append(0)
print(nego_fibonacci + fibonacci)