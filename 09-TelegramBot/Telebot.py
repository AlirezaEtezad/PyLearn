import random
import telebot
from telebot import types
import gtts

bot = telebot.TeleBot("******************************", parse_mode=None)

my_keyboard = types.ReplyKeyboardMarkup(row_width=3)
button1 = types.KeyboardButton("/game")
button2 = types.KeyboardButton("/fal")
button3 = types.KeyboardButton("/max")
button4 = types.KeyboardButton("عکس")
button5 = types.KeyboardButton("/help")
button6 = types.KeyboardButton("/age")
button7 = types.KeyboardButton("/argmax")
button8 = types.KeyboardButton("/voice")

my_keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f"سلام {user_name} خوش آمدی")
	
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message,"انتخاب کن", reply_markup=my_keyboard)

@bot.message_handler(commands=["fal"])
def send_fal(message):
	fal_list =["فال1", " فال2 ", " فال3", "فال4"]
	selected_fal = random.choice(fal_list)
	bot.send_message(message.chat.id, selected_fal)


@bot.message_handler(commands=['game'])
def game(message):
	bot.send_message(message.chat.id, "باید یه عدد بین 1 تا 100 حدس بزنی")
	computer_number = random.randint(1,100)
	for i in range (100):
		user_number = int(message.text)

		if computer_number == user_number :
			bot.send_message(message.chat.id, "آفرین برنده شدی")
			break
		elif computer_number > user_number:
			bot.send_message(message.chat.id, "برو بالا")

		else:
			bot.send_message(message.chat.id, "برو پایین")
	bot.send_message(message.chat.id, "تو ",i+1," بار حدس زدی.")


@bot.message_handler(commands=["age"])
def age(message):
	bot.send_message(message.chat.id, "سال تولد خود را به صورت شمسی وارد کنید: ")
	user_birth_year = int(message.text)
	Year = 1402
	age = Year - user_birth_year
	bot.send_message(message.chat.id, "سن شما {age} میباشد.")

@bot.message_handler(commands=["voice"])
def voice(message):
	bot.send_message(message.chat.id, "Please enter an English sentence: ")
	user_sentence = message.text
	x = gtts.gTTS(user_sentence, lang="en", slow=False, tld='com.au')
	x.save("voice.mp3")
	voice = open('voice.mp3', 'rb')
	bot.send_voice(message.chat.id, user_sentence)


@bot.message_handler(commands=["max"])
def max(message):
	bot.send_message(message.chat.id, "Enter an array of digits splited by ',': ")
	user_input = message.text
	user_array = [int(num) for num in user_input.split(",")]
	max_value = max(user_array)
	bot.send_message(message.chat.id, "مقدار ماکزیمم {max_value} میباشد.")

	
@bot.message_handler(commands=["argmax"])
def arg_max(message):
	bot.send_message(message.chat.id, "Enter an array of digits splited by ',': ")
	user_input = message.text
	user_array = [int(num) for num in user_input.split(",")]
	max_value = max(user_array)
	for i in user_array:
		if user_array[i] == max_value:
			bot.send_message(message.chat.id, "اندیس مقدار ماکزیمم {i} میباشد.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):

	if message.text == "سلام":
		bot.reply_to(message, "علیک سلام")
	elif message.text == "خوبی؟" :
		bot.reply_to(message, " نه فقط تو خوبی")
		
	elif message.text == "دوست دارم":
		bot.send_message(message.chat.id, "عادی")
	elif message.text == "عکس":
		photo = open("photo.jpg", "rb")
		bot.send_photo(message.chat.id, photo)
	# elif message.text == "بازی":
	# 	bot.reply_to(message, "باید یه عدد بین 1 تا 100 حدس بزنی")
	# 	computer_number = random.randint(1,100)
	# 	for i in range (100):
	# 		user_number = int(message.text)
	# 		print(user_number)

	# 		if computer_number == user_number :
	# 			bot.send_message(message.chat.id, "آفرین برنده شدی")
	# 			break
	# 		elif computer_number > user_number:
	# 			bot.send_message(message.chat.id, "برو بالا")

	# 		else:
	# 			bot.send_message(message.chat.id, "برو پایین")
	# 	bot.send_message(message.chat.id, "تو ",i+1," بار حدس زدی.")

	else:
		bot.send_message(message.chat.id,"انتخاب کن", reply_markup=my_keyboard)




bot.infinity_polling()