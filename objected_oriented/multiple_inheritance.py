# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print("{}(으)로 프로그래밍합니다.".format(self.favorite_language))

# 테니스 선수 클래스
class TennisPlayer:
    def __init__(self, tennis_level):
        self.tenis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다".format(self.tenis_level))

class EnginnerTennisPlayer(Engineer, TennisPlayer):
    def __init__(self, favorite_language, tenis_level):
        # 다중 상속의 단점 : super()를 썻을 때 누구를 상속하는지 알 수 없음
        Engineer.__init__(self, favorite_language)
        TennisPlayer.__init__(self, tenis_level)


young = EnginnerTennisPlayer("파이썬", "초급")

young.program()
young.play_tennis()