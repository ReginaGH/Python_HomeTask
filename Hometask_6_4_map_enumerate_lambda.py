#_________ map, enumerate, lambda ___________

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def selection(f, data):
    return [elem for i, elem in enumerate(data) if f(i)]
data = list(map(int, input('Ввести числа через пробел ').split()))
selection_list= selection(lambda i: i%2!=0, data)
print(sum())

# --------- первоначальное решение ----------
# my_list = [2,3,7,8,5,1,4]
# sum = 0
# for i,elem in enumerate(my_list):
    # if i %2 != 0:
        # sum+=elem
# print(sum)  # 
