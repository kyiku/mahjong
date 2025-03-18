class Hai:
    KINDS = {0: '萬', 1: '筒', 2: '索', 3: '東', 4: '南', 5: '西', 6: '北', 7: '白', 8: '発', 9: '中'}
    AKADORA = {16: '赤5萬', 52: '赤5筒', 88: '赤5索'}

    def __init__(self,number0to135,aka=True):
        self.number0to135 = number0to135

        if (number0to135< 108):
            self.kinds = number0to135 // 36
            self.number = self.number0to135 // 4 - self.kinds * 9
            if aka and self.number0to135 in self.AKADORA:
                self.str = self.AKADORA[self.number0to135]
            else:
                self.str = str(self.number + 1) + self.KINDS[self.kinds]

        else:
            self.kinds = 3
            self.number = (self.number0to135 - 108) // 4
            self.str = self.KINDS[self.kinds+self.number]