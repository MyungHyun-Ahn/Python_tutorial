from xmlrpc.client import boolean
import numpy as np

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

print(array1 > 4) #대소비교

print(array1 % 2 == 0) #나머지

booleans = np.array([True, True, False, True, True, False, True, True, False, True, False])
print(np.where(booleans)) #True인 인덱스 번호 출력

print(np.where(array1 > 4)) #4보다 큰(True)인 인덱스 번호만 출력

filter = np.where(array1 > 4)

print(array1[filter]) #인덱스가 가리키는 것을 출력