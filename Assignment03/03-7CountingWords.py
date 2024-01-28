user_string = input("enter a sentence: ")
sentence_array = [word for word in user_string.split(" ") if word !=" "]
print(len(sentence_array))