# Реализуйте алгоритм перемешивания списка
import random

my_list = [1,2,3,4,5,6,7]
new_list = []
[new_list.append(random.choice(my_list)) for i in range(len(my_list))]

print(my_list)
print(new_list)


# new_list = []
# for i in range(len(my_list)):
    # new_list.append(random.choice(my_list))
# print(my_list)
# print(new_list)
# 