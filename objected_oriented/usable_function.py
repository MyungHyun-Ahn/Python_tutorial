# max : 최대 값을 반환\
from numpy import square


print(max(2, 5))
print(max(2, 7, 5))

# min : 최소 값을 반환
print(min(2, 5))
print(min(2, 7, 5, 11, 6))

# sum : 리스트, 튜플, 딕셔너리에 있는 숫자형 요소들의 합을 반환
int_list = [1, 2, 3, 4, 5]
int_tuple = (4, 3, 6, 1, 2)
int_dict = {1: "one", 2: "two", 3: "three"}
    
print(sum(int_list))
print(sum(int_tuple))
print(sum(int_dict))


# ternary expression : 불린 값에 따라 다른 값을 리턴하는 구문
condition = True    
condition_string = "nice" if condition else "not nice"    
print(condition_string)

# list comprehension : 새로운 리스트를 만드는 간편한 방법
int_list = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in int_list]
print(squares)

# zfill : 몇자리 이상을 가진 문자열로 변환시켜줌
print("1".zfill(6))
print("333".zfill(2))
print("a".zfill(8))
print("ab".zfill(8))
print("abc".zfill(8))