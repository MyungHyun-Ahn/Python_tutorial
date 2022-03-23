
# import * 로 임포트했을 때 __all__ 에 있는 것만 가져오겠다는 의미
__all__ = ['PI', 'circle']

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