# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.
# Первый вариант, через множество

ord = [1,2,2,3,3,4,4,5,5,6]
new_ord = [1]
for num in range(len(ord)-1):
    if ord[num+1]!=ord[num]:
        new_ord.append(ord[num+1])
print(new_ord)


# -------- Другие решения с семинара ----------
# # Второй вариант, с сохранением того же порядка 
# import numpy
# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 5]
# res = numpy.array(numbers)
# unikum_numbers = numpy.unique(res)
# print(unikum_numbers)


# #-----------------------------

# enum_number = list(map(int, input("input list:").split()))

# enum_unique = list(filter(lambda item: enum_number.count(item) == 1, enum_number))

# print(enum_number, '->', enum_unique)
