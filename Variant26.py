import math
from random import random
import matplotlib.pyplot as pyplot
from matplotlib.patches import Rectangle
from scipy import integrate
import numpy

def function(x):
    return math.exp(2*x)

n = int(input("Введите количесво отрезков в разбиении: "))
left_limit = int(input("Введите левую границу отрезка: "))
right_limit = int(input("Введите правую границу отрезка: "))

check = False

while not check:
    equipment_type = int(input("Введите тип оснощения левые (1), правые (2), средние (3), случайные (4): "))
    if equipment_type in {1, 2, 3, 4}:
        check = True
    else:
        print("Некоректное значение")

step = (right_limit - left_limit) / n
x = numpy.arange(left_limit, right_limit + 0.01, 0.01)
f_line = numpy.exp(2*x)

def getEquipment(start_of_Segment):
    if equipment_type == 1:
        return start_of_Segment
    elif equipment_type == 2:
        return start_of_Segment + step
    elif equipment_type == 3:
        return start_of_Segment + step/2
    elif equipment_type == 4:
        return start_of_Segment + random() % step

integral_sum = 0.0

i = left_limit

max_function_result = function(left_limit)
min_function_result = function(left_limit)
while i < right_limit - step:
    function_result = function(getEquipment(i))
    rectangle = Rectangle((i, 0), step, function_result, edgecolor = 'black', facecolor = 'blue', fill= True, lw=1)
    integral_sum += rectangle.get_width() * rectangle.get_height()
    pyplot.gca().add_patch(rectangle)
    max_function_result = max(max_function_result, function_result)
    min_function_result = min(min_function_result, function_result)
    i += step

pyplot.ylim(min_function_result - 1, max_function_result + 1)

print("")
print("Результаты:")

integral = integrate.quad(function, left_limit, right_limit)[0]

print("Нужное значение: " + str(integral))
print("Получили: " + str(integral_sum))

pyplot.plot(x, f_line, 'r', lw=2)
pyplot.show()

