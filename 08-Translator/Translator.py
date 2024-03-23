import gtts

def read_file():
    global words_bank    

    f = open("Translate.txt", "r")
    temp = f.read().split("\n")
  #  print(words)


    words_bank = []
    for i in range (0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)
   #     print(words_bank)
        
def append_file():
    f = open("Translate.txt", "a")
    f.write("\n")
    f.write(EN_word)
    f.write("\n")
    f.write(Fa_word)
    f.close()
    output ="your word added to database succussfully"
    return output

while True:
  read_file()
  print("1- En to Fa")
  print("2- Fa to En")
  print("3- Add new world to database")
  print("4- exit")
  user_choice = int(input("Enter your choice: "))


  if user_choice == 1:
    user_text = input("Enter English text: ")
    user_words = user_text.split(" ")
    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
              output = output + " " + word["fa"]
              break
        else: output = output + " " + user_word

  if user_choice == 2:
    user_text = input("Enter Fingilish text: ")
    user_words = user_text.split(" ")
    output = ""
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
              output = output + " " + word["en"]
              break
        else: output = output + " " + user_word
  
  if user_choice ==3:
     EN_word =input("Enter English word: ")
     Fa_word = input("Enter Fingilish Translation: ")
     append_file()

  if user_choice ==4:
     print("Good Bye")
     exit(0)

  print(output)
  x = gtts.gTTS(output, lang="en", slow=False, tld='com.au')
  x.save("voice.mp3")