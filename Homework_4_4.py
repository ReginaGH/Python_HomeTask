# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = 5
koef = [randint(0,100) for num in range(k)]  # создание списка коэффициентов
koef = [str(i) for i in koef]

p = ['','']                 # создание списка степеней
for i in range(2,k):
    p.append(i)
p = p[::-1]
p = [str(i) for i in p]

x = ['','x']                # создание списка переменной
for i in range(k-2):
        x.append('x**')
x = x[::-1]

v = [' = 0']                # объединение переметров всех одночленов
for i in range(k):
    v.insert(i,(koef[i] + x[i] + p[i]))
print(v, '\n')

polynomial = ''             
for i in range(len(v)):
    if i < len(v)-2:
        polynomial = polynomial + v[i] + ' + '
    else:
        polynomial = polynomial + v[i]

print(polynomial)

with open('polynomial.txt', 'w+') as data:     # создание и запись в файл
    data.write(polynomial)

data.close()




# ---------------- вариант решения из семинара ------------

# def generate_superscript(x, n):
    # if n == 0:
        # return str(x)
    # if n == 1:
        # return str(x)+"x"
    # superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    # result = str(x)
    # if x != 0:
        # result += "x"
    # for i in str(n):
        # result += superscript[int(i)]
    # return result

# def generate_polynomial(k):
    # result = []
    # for i in range(k, -1, -1):
        # coefficient = random.randint(0, 100)
        # if coefficient != 0:
            # result.append(generate_superscript(coefficient, i))
    # return "+".join(result)
# 
# print(generate_polynomial(10),'= 0')
