import numpy as np

# max() : 최대값     min : 최솟값     #mean() : 평균값
# median(array) : 중앙값     std() 표준 편차     var() : 분산

arr1 = np.array([14, 6, 13, 21, 23, 31, 9, 5])

print(arr1.max())  # 최대값
print(arr1.min())  # 최솟값

print(arr1.mean()) # 평균값

print(np.median(arr1)) #중앙값 
# median은 numpy array의 메소드가 아닌 numpy의 메소드

print(arr1.std())  # 표준 편차
print(arr1.var())  # 분산