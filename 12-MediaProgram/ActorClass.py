class Actor:
    def __init__(self,name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def show(self):
        print("name: ",self.name, "gender: ",self.gender, "age: ", self.age)
        