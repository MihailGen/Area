import unittest

from .figures import Circle, Triangle


class TestCircle(unittest.TestCase):
    def test_area(self):
        circ = Circle(5)
        result = circ.area
        self.assertEqual(result, 78.5)
        circ = Circle(6)
        result = circ.area
        self.assertEqual(result, 113.04)
        circ = Circle(7)
        result = circ.area
        self.assertEqual(result, 153.86)
        circ = Circle(8)
        result = circ.area
        self.assertEqual(result, 200.96)


class TestTriangle(unittest.TestCase):
    def test_area(self):
        tri = Triangle(5, 6, 7)
        result = tri.area
        self.assertEqual(result, 14.6969)
        tri = Triangle(3, 4, 5)
        result = tri.area
        self.assertEqual(result, 6)
        tri = Triangle(11, 6, 7)
        result = tri.area
        self.assertEqual(result, 18.9737)
        tri = Triangle(13, 14, 15)
        result = tri.area
        self.assertEqual(result, 84)

    def test_right_angled(self):
        tri = Triangle(4, 3, 5)
        result = tri.right_angled
        self.assertEqual(result, "Треугольник прямоугольный")

        tri = Triangle(5, 6, 7)
        result = tri.right_angled
        self.assertEqual(result, "Треугольник не прямоугольный")

        tri = Triangle(6, 10, 8)
        result = tri.right_angled
        self.assertEqual(result, "Треугольник прямоугольный")

        tri = Triangle(6, 7, 8)
        result = tri.right_angled
        self.assertEqual(result, "Треугольник не прямоугольный")


if __name__ == '__main__':
    unittest.main()
