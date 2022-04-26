# deque 는 파이썬 collections 모듈에서 가지고 온다
from collections import deque
# 리스트 스택이나 더블리 링크드 리스트나 완전히 동일, 메소드도 물론 동일
#stack = deque()
stack = []

# 스택 맨 끝에 데이터 추가
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")

print(stack) # 스택 출력

# 맨 끝 데이터 접근
print(stack[-1])

# 맨 끝 데이터 삭제
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)