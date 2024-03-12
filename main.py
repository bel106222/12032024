# begin = int(input('Введите начало диапазона:\n>'))
# end = int(input('Введите конец диапазона:\n>'))
# sum = 0
# for i in range(begin, end + 1):
#     sum += i
# print('Сумма чисел =', sum, "\b, среднее арифметическое =", sum / (end - begin + 1))
#####################################################
# end = int(input('Введите число:\n>'))
# fak = 1
# for i in range(1, end + 1):
#     fak *= i
# print(f'Факториал числа {end}! = {fak}')
#####################################################
# end = int(input('Длина линии:\n>'))
# for i in range(1, end + 1):
#     print('*', end = '')
#####################################################
# end = int(input('Длина линии:\n>'))
# symb = input('Символ:\n>')
# for i in range(1, end + 1):
#      print(symb, end = '')
#####################################################
# height = int(input('Высота:\n>'))
# lenght = int(input('Длина:\n>'))
# symb = input('Символ:\n>')
# buf = symb
# for i in range(1, height + 1):
#     for j in range(1, lenght + 1):
#         if i > 1 and i < height and j > 1 and j < lenght:
#             symb = ' '
#         else:
#             symb = buf
#         print(symb, end = '')
#     print()
#####################################################
height = int(input('Высота:\n>'))
lenght = int(input('Длина:\n>'))
symb = ''

for i in range(1, height + 1):
    
    if i % 2 == 0:
        symb = '*'
    else:
        symb = '#'
        
    for j in range(1, lenght + 1):
        print(symb, end = '')
    
    print()