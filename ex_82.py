q = int(input('Введите число в десятичном виде : '))  # запрашиваем ввести десятичное число

result = ''  # присваиваем переменной result пустую строку
while q > 0:  # создаем цикл
    r = q % 2  # присваем r остаток от деления q на 2
    result = str(r) + result  # преобразовали r в строку и поставили ее в начале перемнной result
    q = q // 2 #присваиваем q результат деления без остатка на 2
print(result)
