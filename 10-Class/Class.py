class Fraction:
    def __init__(self, a, b):
        self.numerator = a
        self.denominator = b

    def simplify(self):
        ...

    def devision(self):
        ...
    def sum(self):
        ...
    def minus(self):
        ...


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def add_seconds(self, seconds):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second + seconds
        self.hour = total_seconds // 3600
        self.minute = (total_seconds % 3600) // 60
        self.second = (total_seconds % 3600) % 60

# مثال استفاده از کلاس
t1 = Time(10, 30, 45)
print("زمان اولیه:", t1)  # خروجی: 10:30:45

t1.add_seconds(120)
print("زمان پس از افزودن ۱۲۰ ثانیه:", t1)  # خروجی: 10:32:45



class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def change_to_shamsi_cleander(self):
        ...