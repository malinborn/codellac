class Health:
    def __init__(self, points: int):
        self.__points = points
        self.alive = True

    def damaged(self, damage: int) -> int:
        if not self.alive:
            return 0

        self.__points -= damage

        if self.__points <= 0:
            print("О ужас!")
            self.__points = 0
            self.alive = False
            return 0

        return self.__points

    def __new__(cls, *args, **kwargs):
        raise TypeError("Творить вот так людей доступно демиургам только, Богу\n"
                        "А ты здоровье дай рожденьем, начало дав прологу\n"
                        "Health.give_birth_a_knight()")

    @staticmethod
    def give_birth_a_knight():
        instance = super(Health, Health).__new__(Health)
        instance.__init__(100)
        return instance

    @staticmethod
    def _give_birth_a_dragon():
        instance = super(Health, Health).__new__(Health)
        instance.__init__(200)
        return instance

    def check(self) -> int:
        return self.__points
