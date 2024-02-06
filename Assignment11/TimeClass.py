class Time:
    def __init__(self, hh, mm, ss):
        self.hour = hh
        self.minute = mm
        self.second = ss
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)

    def sum(self, other):
        sum_s = self.second + other.second
        sum_m = self.minute + other.minute
        sum_h = self.hour + other.hour
        result = Time(sum_h, sum_m, sum_s)
        return result
    
    def sub(self, other):
        sub_s = self.second - other.second
        sub_m = self.minute - other.minute
        sub_h = self.hour - other.hour
        result = Time(sub_h, sub_m, sub_s)
        return result

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

    def second_to_time(self):
        H = self.second // 3600
        M = (self.second % 3600) // 60
        S = self.second % 60
        result = Time(H, M, S)
        return result
    
    def time_to_second(self, H, M, S):
        TotalSeconds = self.H * 3600 + self.M * 60 + self.S
        return TotalSeconds
    
    def GMT_to_tehran(self, hh, mm, ss):
        tehran_h = self.hh + 3
        tehran_m = self.mm + 30
    
        

t1 = Time(int(input("hh: ")), int(input("mm: ")) ,int(input("ss: ")))
t1.show()
