class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거" # 가게 이름
    raise_percentage = 1.03 # 시급 인상률

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name  # 이름
        self.wage = wage  # 시급
    
    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage
    
    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + "직원: " + self.name


# 상속할 부모 클래스를 파라미터로 넣어줌
class Cashier(Employee):
    def __init__(self, name, wage, number_sold):
        """인스턴스 변수 설정"""
        # super() 부모클래스의 메소드를 사용하고 싶을 때 사용
        super().__init__(name, wage)
        self.number_sold = number_sold # 판매량

class DeliveryMan(Employee):
    pass


young = Cashier("강영훈", 8900, 4)
young.raise_pay()

print(young.wage)
print(young)

"""
# 모든 클래스는 builtins.object 클래스를 자동으로 상속 받음
# help(Cashier)


# 클래스가 상속하고 있는 부모 클래스 출력
print('\nmro')
print(Cashier.mro())

# 인스턴스가 주어진 클래스의 인스턴스인지 확인
print('\nisinstance')
print(isinstance(younghoon, Cashier))
print(isinstance(younghoon, DeliveryMan))
print(isinstance(younghoon, Employee))

# 한 클래스가 다른 클래스의 자식 클래스인지 확인
print('\nissubclass')
print(issubclass(Cashier, Employee))
print(issubclass(Cashier, object))
"""

