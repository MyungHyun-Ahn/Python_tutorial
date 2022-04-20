from math import pi, sqrt
from abc import ABC, abstractclassmethod


# 추상 메소드 / 자식 클래스가 반드시 오버라이딩 해야하는 메소드
# 추상 메소드가 1개 이상 있어야 추상 클래스라고 할 수 있음
# 추상 클래스 인스턴스 생성 X
class Shape(ABC):
    """도형 클래스"""
    @abstractclassmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractclassmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height
    
    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)

class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)

class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side
    
    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        # shape 가 Shape 클래스의 인스턴스라면
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다.")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        res_str = "그림판 안에 있는 도형들: \n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


rectangle = Rectangle(3, 7)
circle = Circle(4)

paint_program = Paint()
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())
