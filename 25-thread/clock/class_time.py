
class MyTime:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def plus(self):
        self.second += 1
        self.fix()

    def minus(self):
        self.second -= 1
        self.fix()


    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1
        
        if self.minute >= 60:
            self.hour += 1
            self.minute -= 60

        if self.second < 0:
            self.second += 60
            self.minute -=1

        if self.minute < 0:
            self.hour -= 1
            self.minute += 60
        
        # if self.hour < 0:
        #     self.hour = 0
        #     self.minute = 0
        #     self.second = 0



    
