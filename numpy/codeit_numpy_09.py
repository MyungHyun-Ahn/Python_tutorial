import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000, 
    440000, 140000, 180000, 340000, 
    330000, 290000, 280000, 380000, 
    170000, 140000, 230000, 390000, 
    400000, 350000, 380000, 150000, 
    110000, 240000, 380000, 380000, 
    340000, 420000, 150000, 130000, 
    360000, 320000, 250000
]

# 코드를 작성하세요.
# 내가 쓴 답안
won_array1 = np.full(len(revenue_in_yen), 10.08)
won_array1 = won_array1 * revenue_in_yen

print(won_array1)

# 해설 답안
yen_array = np.array(revenue_in_yen) #numpy 배열로 변환시킨후
won_array2 = yen_array * 10.08 #곱셈수행가능

# 정답 출력
print(won_array2)