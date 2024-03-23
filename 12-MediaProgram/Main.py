from MediaClass import Media

VIDEOS = []


f = open("Database.txt", "r")
for line in f:
    result = line.strip().split(",")
    # .strip() removes  leading and trailing spaces
    obj = Media(result[0], result[1], result[2], result[3], result[4], result[5])
    VIDEOS.append(obj)

f.close()

# print (VIDEOS): it shows the memory address



def menu():
    print("1- Add")
    print("2- Edit")
    print("3 -Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Exit")

def add():

    name = input("enter name: ")
    director =  input("enter director: ")
    IMBD_score =  input("enter IMBD_score: ")
    url = input("enter url: ")
    duration = int(input("enter duration: "))
    casts = input("enter casts: ")
    new_video = Media(name, director, IMBD_score, url, duration, casts)
    VIDEOS.append(new_video)

def edit():
    user_input = input("enter video name: ")
    for video in VIDEOS:
        if video.name == user_input:
            video.show_ifno()
            break
    new_name = input("enter a new name: ")
    new_director = input("enter new director: ")
    new_IMBD_score = input("enter new score: ")
    video.update({"name": new_name, "director": new_director, "IMBD_score": new_IMBD_score})
    print("Editted successfully")
    video.show()

def remove():
    user_input = input("enter video name: ")
    for video in VIDEOS:
        if video.name == user_input:
            video.show()
            confirm = input("confirm delete 'Y' or 'N': ")  
            if confirm == "Y":
                VIDEOS.remove(video)
                print("Video removed successfully")
                break




def search():
    print("1- search by name")
    print("2- search by duration")
    choice = int(input("Enter search method: "))
    if choice == 1:
        user_input = input("Enter video name: ")
        for video in VIDEOS:
            if video.name == user_input:
                video.show_info()
            else:
                print("name not matched any video")
    elif choice == 2:
        dur1 = int(input("Min duration: "))
        dur2 = int(input("Max duration: "))
        for video in VIDEOS:
            if dur1 <= video.duration <= dur2:
                video.show_ifno()
            else:
                print("Not such a duration.")

def show():
    for video in VIDEOS:
        video.show_info()
        

def write_database():
    f = open("Database.txt", "w")
    for video in VIDEOS:
            line = f"{video}"
            f.write(line)
    f.close
    print("Database updated successfully")



while True:
    menu()
    choice = int(input("enter a number: "))
    if choice == 1 :
        add()
    elif choice == 2 :
        edit()
    elif choice == 3 :
        remove()
    elif choice == 4 :
        search()
    elif choice == 5 :
        show()
    elif choice == 6 :
        write_database()
        exit(0)
    else:
        print("Enter correctly!")