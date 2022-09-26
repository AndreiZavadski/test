import math

number = int(input('Введите целое число : '))
factor = 2
while factor <= number: #создали цикл
    if number % factor == 0: #создали условие
        factor = math.trunc( number / factor) #делим с округлением вниз
        print(factor)
        break
else:
    factor += 1 #увеличиваем на 1
print('Простые множители числа ', number,' : ', factor )
