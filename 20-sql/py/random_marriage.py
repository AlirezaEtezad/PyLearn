import random
boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman", "amir"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]
marriage =[]
for i in range(len(boys)):
    for j in range(len(girls)):
        rand_groom = random.choice(boys)
        rand_bride = random.choice(girls)
        boys.remove(rand_groom)
        girls.remove(rand_bride)
        marriage.append((rand_groom, rand_bride))

print(marriage)