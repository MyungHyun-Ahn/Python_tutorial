print('area 모듈 이름 : {}'.format(__name__))

PI = 3.14

def circle(radius):
    return PI * radius * radius

def square(length):
    return length * length


# __name__
# __main__
if __name__ == '__main__':
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)
    print(square(4) == 16)
    print(square(2) == 4)