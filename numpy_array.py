import numpy as np

arr1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) #파이썬 리스트를 통해 생성
print(arr1)

arr2 = np.full(6, 7) #균일한 값으로 생성 numpy.full(n, m) 배열에 m으로 n개 만큼 채움
print(arr2)

arr3 = np.zeros(6, dtype=int) #0으로 채우는 매소드 ones 메소드를 사용하면 1로 채움
print(arr3)

arr4 = np.random.random(6) #랜덤한 소수 값으로 채울수 있음
print(arr4)

arr5 = np.arange(6) #arange(m) 0부터 m-1까지의 값으로 채움
print(arr5)

arr6 = np.arange(2, 7) #arange(n, m) n부터 m-1까지의 값으로 채움
print(arr6)

arr7 = np.arange(3, 17, 3) #arange(n, m, s) n부터 m-1까지의 값들 중 간격이 s인 값들로 채움
print(arr7)