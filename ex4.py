from math import pi
from math import tan

long = int(input('Введите длинну стороны : ')) #запрашиваем длинну стороны
quantity = int(input('Введите количество старон : ')) #запрашиваем количство сторон
area = (quantity * long ** 2) / (4 * (tan(pi / quantity))) #расчитываем формулу расчета площади правильного многоугольника
print(area) #выводим результат
