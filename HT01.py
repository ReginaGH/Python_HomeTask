# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = input('Введите номер дня недели -  ')   
while day not in ('1','2','3','4','5','6','7'):
    day = input('Введите номер дня недели -  ')
day = int(day)
# if day==6 or day==7:
    # print('да')
# else:
    # print('нет')

day = lambda day: 'да' if day==6 or day==7 else 'нет'
print(day(int(input('Введите номер дня недели -  '))))

# import numbers
# def CheckInput(inputText):
#     check_input = False
#     while not check_input:
#         try:
#             number = int(input(f'{inputText}'))
#             check_input = True
#         except ValueError:
#             print('Вы вводите не цифру, введите корректные данные')
#     return number

# def CheckDayOfWeek(day):
#     if day < 1 or day > 7:
#         print('Введите число соответствующее дню недели')
#     elif day == 6 or day == 7:
#         print('Выходной :)')
#     else: 
#         print('Будний день')

# day = CheckInput('Введите цифру соответствующее дню недели: ')
# CheckDayOfWeek(day)