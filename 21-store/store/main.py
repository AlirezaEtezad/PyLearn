import sqlite3
import qrcode

connection = sqlite3.connect("store.db")
my_cursor = connection.cursor()

def menu():
    print("1- Add")
    print("2- Edit")
    print("3 -Remove")
    print("4- Search")
    print("5- Show Products")
    print("6- Buy")
    print("7- Show Card")
    print("8- QrCode")
    print("9- Exit")

def search():
    user_input = input("Please enter product name: ")
    if user_input =="fin":
        print("Operation Ended")
        return user_input, None
    else:        
        result = my_cursor.execute(f"SELECT * FROM products WHERE name='{user_input}'")
        for product in result:
            print (product)
            return user_input,product
        else:
            print("product not found!")
            return user_input, None

def add():
    user_input, product = search()
    if product == None:
        price = input("To add please eneter product price: ")
        stock = input("Please enter product stock: ")
        my_cursor.execute(f"INSERT INTO products (name, price, stock) VALUES ('{user_input}', '{price}', '{stock}')")
        connection.commit()
        print("Product inserted successfully.")
    else:
        print("You already have this product")
        
def edit():
    user_input, product = search()
    if product:
        name = input("Enter new name: ")
        price = input("Enter new price: ")
        stock = input("Enter new stock: ")
        my_cursor.execute(f"UPDATE products SET name='{name}', price={price}, stock={stock} WHERE name='{user_input}'")

def remove():
    user_input, product = search()
    if product:
        user_confirm = input("Are you sure you want to delete this product? y/n: ")
        if user_confirm.lower() == "y":
            my_cursor.execute(f"DELETE FROM products WHERE name='{user_input}'")
            connection.commit()
            print("product deleted succussfully")
        else:
            print("Deletion cancelled")
            return
    # else:
    #     return

def show_products():
    result = my_cursor.execute("SELECT * FROM products").fetchall()
    for product in result:
        print (product)

def buy():
    while True:
        user_input, product = search()
        if user_input == "fin":
            break
        if product:
            id, name, price, stock = product
            if stock > 0:
                amount = int(input("please enter the amount: "))

                if amount <= stock and stock >0:
                    remaining_stock = stock - amount
                    my_cursor.execute(f"UPDATE products SET stock={remaining_stock} WHERE name='{user_input}'")
                    my_cursor.execute(f"INSERT INTO card (id, name, price, amount, total_price) VALUES ({id}, '{name}', {price}, {amount}, {amount*price})")
                    connection.commit()
                    print("Product added to card! To finish purchase insert 'fin'")
                else:
                    print("There is not enough in stock!!")
            else:(print("The stock is 0 or less!!"))

def show_card():
    sub_total = 0
    result = my_cursor.execute("SELECT * FROM card").fetchall()
    for product in result:
        print (product)
        *_, total_amount = product
        sub_total += total_amount
    print(f"You have to pay {sub_total} $")

def make_qrcode():
        user_input, product = search()
        qr = qrcode.make(product)
        id, *_ = product
        qr.save (f"{id}.png")
        print("qr code for product", id, "successfully saved")        
    

while True:
    menu()
    choice = int(input("enter a number: "))
    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        search()
    elif choice == 5:
        show_products()
    elif choice == 6:
        buy()
    elif choice == 7:
        show_card()
    elif choice == 8:
        make_qrcode()
    elif choice == 9:
        confirm = input("After exit your card will be cleard. Are you sure to exit? y/n: ")
        if confirm.lower() == "y":
            my_cursor.execute("DELETE FROM card")
            connection.commit()
            exit(0)
        else:
            print("Exit cancelled")
    else:
        print("Enter correctly!")