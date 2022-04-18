# 파라미터로 함수를 받음
def add_print_to(original):
    def wrapper():
        print('함수 시작') # 부가 기능 < print_hello를 꾸밈
        original()
        print('함수 끝')
    return wrapper

# 데코레이터 > 기존 함수에 새로운 기능 추가
@add_print_to
def print_hello():
    print('안녕하세요!')

print_hello()