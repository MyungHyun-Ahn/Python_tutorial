class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민번호"""
        self.name = name
        # __를 붙이고 변수를 선언하면 외부에서 변수 접근 불가능
        self.__age = age
        self.__resident_id = resident_id
    
    # __를 붙인 메소드는 외부에서 접근 불가
    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field
    
    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

    @property
    def age(self):
        print("나이를 리턴합니다.")
        return self.__age
    # setter 메소드
    @age.setter
    def age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 설정합니다.")
            self.__age = 0

        else:
            self.__age = value


kyusik = Citizen("최규식", 25, "12345678")
young = Citizen("younghoon kang", 18, "87654321") # 어린이

print(young.age)

young.age = -23
print(young.age)






