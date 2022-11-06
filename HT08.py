# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму: (1+1/n)**n
# Пример: для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число - '))
d = {}

# v = [int((1+1/i)**i) for i in range(1, n+1)]

k = []
v = [] 
for i in range(1, n+1):
    k.append(i)
    v.append(int((1+1/i)**i))
d = dict(zip(k,v))
print(d)