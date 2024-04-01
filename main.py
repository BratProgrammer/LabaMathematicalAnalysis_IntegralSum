import math

import matplotlib.pyplot as pyplot
from matplotlib.patches import Rectangle
import numpy

def function(x):
    return math.exp(1)**(3*x)

x = numpy.arange(0, 0.51, 0.01)
f = numpy.exp(1)**(3*x);

n = int(input("Введите количесво отрезков в разбиении: "))

step = 0.5 / n

pyplot.ylim(-2, 5)

integral_sum = 0

i = 0
while i < 0.5:
    rectangle = Rectangle((i, 0), step, function(i + step/2), edgecolor = 'black', facecolor = 'blue', fill= True, lw=1)
    integral_sum += rectangle.get_width() * rectangle.get_height()
    pyplot.gca().add_patch(rectangle)
    i += step

print("Результаты:")

integral = math.exp(1.5) / 3 - 1/3

print("Нужное значение: " + str(integral))
print("Получили " + str(integral_sum))
print("Разница: " + str(abs(integral - integral_sum)))

pyplot.plot(x, f, 'r', lw=2)
pyplot.show()
