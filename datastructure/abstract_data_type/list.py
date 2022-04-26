# 파이썬 리스트 생성
trending = []

# 특정 위치에 데이터 삽입
trending.insert(0, "연애인 A씨")
trending.insert(1, "잠실 콘서트")
trending.insert(2, "한국 휴일 수")
trending.insert(3, "추석 음식")

print(trending) # 리스트 출력

# 괄호를 이용한 인덱스 접근
print(trending[0])
print(trending[1])

trending[2] = 4

print(trending)

# in 을 이용한 탐색 / 리스트에 있는지 없는지 불린 값으로 리턴
print("연애인 A씨" in trending)
print("연애인 B씨" in trending)

# del 을 이용한 삭제
del trending[0]

print(trending)

# 추상 자료형 리스트의 특징
# 개발자들이 어떻게 구현했는지 전혀 몰라도 됨
# 기능만 알고 사용할 수 있음!

