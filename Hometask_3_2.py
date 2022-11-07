# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# from string import 

len_list1 = int(input('Введите число, соответствующее размеру списка - '))
list1 = []

[list1.append(int(input(f'Введите целое число с индексом [{i}] - '))) for i in range(len_list1)]
print(list1)

list2 = []
for i in range(len_list1//2):
    list2.append(list1[i]*list1[-1-i])
if len_list1%2==1:
    list2.append(list1[len_list1//2]**2)

print(list2)
