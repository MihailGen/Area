import math

#функция проверки вводимых значений
def correct_value(value):

    try:
        value = float(value)
    except:
        print (f'Некорректное значение: {value}')
        #raise ValueError(f'Некорректное значение: {value}')
        return False

    if (value < 0):
        print(f'Значение не может быть отрицательным: {value}')
        # raise ValueError(f'Значение не может быть отрицательным: {value}')
        return False

    return True


#
class Circle:
    def __init__(self, radius):
        if correct_value(radius):
            self._radius = float(radius)  # Используем защищенный атрибут

    @property
    def radius(self):
        # Геттер
        return self._radius

    @radius.setter
    def radius(self, value):
        # Сеттер
        if correct_value(value):
            self._radius = value

    @property
    def area(self):
        # Вычисление площади
        return round(3.14 * self._radius ** 2,
                     4)  # результат окуругляем до 4 знаков (к примеру) после заятой, для удобства восприятия


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self._side_a = side_a  # Используем защищенный атрибут
        self._side_b = side_b  # Используем защищенный атрибут
        self._side_c = side_c  # Используем защищенный атрибут

    @property
    def side_a(self):
        # Геттер
        return self._side_a

    @property
    def side_b(self):
        # Геттер
        return self._side_b

    @property
    def side_c(self):
        # Геттер
        return self._side_c

    @side_a.setter
    def side_a(self, value):
        # Сеттер
        if correct_value(value):
            self._side_a = value

    @side_b.setter
    def side_b(self, value):
        # Сеттер
        if correct_value(value):
            self._side_b = value

    @side_c.setter
    def side_c(self, value):
        # Сеттер
        if correct_value(value):
            self._side_c = value

    @property
    def area(self):
        p = (self._side_a + self._side_b + self._side_c) / 2
        # Вычисление площади
        return round(math.sqrt(p * (p - self._side_a) * (p - self._side_b) * (p - self._side_c)), 4)

    @property
    def right_angled(self):
        if ((self._side_a ** 2 + self._side_b ** 2 == self._side_c ** 2)
                or (self._side_c ** 2 + self._side_b ** 2 == self._side_a ** 2)
                or (self._side_a ** 2 + self._side_c ** 2 == self._side_b ** 2)):
            return "Треугольник прямоугольный"
        else:
            return "Треугольник не прямоугольный"
