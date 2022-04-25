import time

# 0 ~ 10000000을 리스트에 저장
test_list = [x for x in range(0, 1000001)]

# 0 ~ 10000000을 set에 저장
test_set = set([x for x in range(0, 1000001)])

# 특정 데이터가 리스트에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
print(10000000 in test_list)
t_1 = time.time()

print("리스트에서 걸린 시간: {}".format(t_1 - t_0))

# 특정 데이터가 set에 있는지 확인할 때 걸리는 시간 파악
t_0 = time.time()
print(10000000 in test_set)
t_1 = time.time()

print("set에서 걸린 시간: {}".format(t_1 - t_0))

# 세트가 더 빠름을 확인 가능