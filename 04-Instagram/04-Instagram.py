import instaloader
import getpass

f = open("followers.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close

L = instaloader.Instaloader()
username = input ("please enter username: ")
password = getpass.getpass("please enter password: ")
L.login(username, password)

print ("logged in successfully")

profile = instaloader.Profile.from_username(L.context, input("please enter an id: "))

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)


for old_follower in old_followers:
    if old_follower not in new_followers:
        print("unfollowers are: ", old_followers)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print("new followers are: ", new_followers)


f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close