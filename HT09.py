# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Write a number - '))
num_list = list(range(-num,num+1))
print(num_list)

production = 1
data = open('file.txt','r')
for index_line in data:
    print(f'{num_list[int(index_line)]}', end=' ')  # для проверки 
    production*=num_list[int(index_line)]
print(f'\n Произведение: {production}')

data.close()