# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from functools import reduce
dot_1 = list(map(int, input('Напишите через пробел 2 координаты первой точки A: ').split())) 
dot_2 = list(map(int, input('Напишите через пробел 2 координаты первой точки B: ').split()))
def dot_range(dot_1, dot_2):
     rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
     return round(rng, 2)
print(dot_range(dot_1, dot_2))