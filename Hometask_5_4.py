# 5.4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encoding(data):
    encoding_data = []       # создаём список для подсчёта кол-ва похожих букв
    counter = 1    # длину временного списка, равную 1 (если буква в одном экз)
    for i in range(1, len(data)):
        if data[i]==data[i-1]:      # отсчёт длины врем списка, если элемент похож на предыдущий, то 1+1..
            counter+=1
        else:
            encoding_data.extend([str(counter), str(data[i-1])])    # добавлем в виде строки (кол-во букв, сама буква)
            counter = 1    # "обнуляем" счётчик
    encoding_data.extend([str(counter),str(data[-1])])  # добавляем последнюю букву
    return ''.join(encoding_data)   # возвращаем закодированную строку

def decoding(data):
    decoding_data = []
    number = 0
    for i in data:
        if i.isdigit():     # если число, возвращаем в виде числа 
            number = int(i)
        else:
            decoding_data.append(number * i)    # добавляем кол-во(number) * букву 
            number = 0  
    return ''.join(decoding_data)

s = 'ljjjkWDMMMUUUCNNNNsssssssss'
print(s)
print(encoding(s))
print(decoding(encoding(s)))

print(len(s))
print(len(encoding(s)))
print(len(decoding(encoding(s))))