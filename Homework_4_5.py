# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def polinomial_from_file_to_dict(file, poly, d):    # 1) функция для извлечения многочлена и конвертация в словарь
    with open(file, 'r') as data:
        poly = data.read()
    poly = poly.replace(' = 0','')
    poly = poly.split(' + ')
    poly = poly[::-1]
    
    for i, elem in enumerate(poly):
        if elem.isdigit():
            d[i] = int(elem)
        else:
            d[i] = int(elem.partition('x')[0])
    return d

d1 = {}
d2 = {}
poly1 = ''
poly2 = ''
file1 = 'polynomial_1.txt'
file2 = 'polynomial_2.txt'
polinomial_from_file_to_dict(file1, poly1, d1)
polinomial_from_file_to_dict(file2, poly2, d2)
print(d1)
print(d2,'\n')

if len(d2) < len(d1):   # -----------------2) нахождение меньшего многочлена и приведение к одинаковой длине
    diff = len(d1) - len(d2)
    for i in range(len(d2), len(d2) + diff):
        d2[i] = 0
#    print(d2,' Проверяем увеличение "короткого" словаря \n')
elif len(d1) < len(d2):
    diff = len(d2) - len(d1)
    for i in range(len(d1), len(d1) + diff):
        d1[i] = 0
#    print(d1, ' Проверяем увеличение "короткого" словаря \n')


for i in d1:    # ---------------------- 3) сложение словарей
    d1[i] = d1[i] + d2[i]
print(d1, 'результат сложения словарей \n')


polynomial = []     # ------------------- 4) перевод словаря в отдельные одночлены и , список из строк - одночленов
for key, value in d1.items():
    if key> 0:
        polynomial.append(str(value) + 'x**' + str(key) +' + ')
    elif key == 0:
        polynomial.append(str(value) + ' = 0')
polynomial = polynomial[::-1]


polynomial = ''.join(polynomial)   # 5) перевод списка в строку, многочлен
print(polynomial)


with open ('result_polynomilal.txt','w+') as file:  # 6) запись в новый файл
    file.write(polynomial)