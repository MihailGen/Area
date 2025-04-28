from figures import Circle, Triangle, correct_value

triangl = Triangle(12, 13, 5)
print (triangl.area) # выводит 7.4833
print (triangl.right_angled) #Треугольник прямоугольный

radius = input("Enter radius: ")
if correct_value(radius):
    circle = Circle(radius) #cоздаёт объект
    print (circle.area) # выводит 200.96

    circle.radius = 8  #меняет радиус объекта
    print (circle.area) # выводит 200.96