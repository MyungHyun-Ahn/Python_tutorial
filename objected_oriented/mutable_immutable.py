mutable_object = [1, 2, 3]
immutable_object = (1, 2, 3)

# 가변 타입
mutable_object[0] = 4
print(mutable_object)

# 불변 타입
# 에러 발생 > 속성을 바꿀 수 없음
# 변수가 가리키는 객체 자체를 바꿀순 있음
'''
immutable_object[0] = 4
print(immutable_object)
'''

tuple_x = (6, 4)
# 새로운 튜플 인스턴스를 생성
tuple_x = (4, 1, 7)

print(tuple_x)

list_x = []

list_x.append(4)
list_x.append(1)
list_x.append(7)

print(list_x)