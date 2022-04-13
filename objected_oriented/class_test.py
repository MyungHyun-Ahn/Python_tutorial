# 클래스의 첫글자는 항상 대문자
from typing_extensions import Self


class User:
    # 첫번째 파라미터로 들어오는 인스턴스를 self로 쓰기를 권장
    # 특수 메소드 __init__ 특정 상황에서 자동으로 실행 : 인스턴스가 생성될때 자동 실행
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def say_hello(self):
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        return self.name == name

# User 인스턴스를 생성 
# 3개는 같은 클래스로 만들었어도 모두 다른 인스턴스임

# 인스턴스 변수 정의 하기 인스턴스 이름.속성이름(인스턴스 변수) = "속성에 넣을 값"
# name email password 는 인스턴스 변수
# 인스턴스 변수를 사용하려면 사용 전에 꼭 정의 해두어야함.
# initialize 메소드로 바로 생성가능
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 인스턴스 메소드의 특별한 규칙
# 인스턴스의 메소드를 호출 > 파라미터로 인스턴스가 자동으로 전달
user1.say_hello()
user1.login("young@codeit.kr", "123456")
print(user1.check_name("Young"))