import qrcode
name = input("please enter your name: ")
number = input("please enter your number: ")
name_number = name + "\n" + number
qr = qrcode.make(name_number)
qr.save (input("enter file name: ") + (".png"))
print(name_number)