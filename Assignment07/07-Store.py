import qrcode

PRODUCTS =[]

def read_database():
    f = open("07-Database.txt", "r")

    for line in f:
        split_result = line.split(",")
        product_dic = {"code": split_result[0], "name": split_result[3], "price": int(split_result[1]), "stock": int(split_result[2]),}

    #    print(product_dic)
        PRODUCTS.append(product_dic)
     #   print(line)

    f.close

def menu():
    print("1- Add")
    print("2- Edit")
    print("3 -Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Exit")
    print("8- QrCode")

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price")
    stock = input("enter stock: ")
    new_product = {"code": code, "name": name, "price": price, "stock": stock}
    PRODUCTS.append(new_product)

def edit():
    user_input = input("enter product code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            print (product)
            break

    new_name = input("enter a new name: ")
    new_price = input("enter new price: ")
    new_stock = input("enter new stock: ")
    product.update({"name": new_name, "price": new_price, "stock": new_stock})
    print("Editted successfully")
    print(product)

def remove():
    user_input = input("enter product code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            print (product)
            confirm = input("confirm delete 'Y' or 'N': ")  
            if confirm == "Y":
                PRODUCTS.remove(product)
                print("Product removed successfully")
                break
            
                

def show_list():
    print("code\t price\t\t name\t")
    for product in PRODUCTS:
        print(product["code"], "\t", product["price"] , "\t", product["name"])

    
def search():
    user_input = input("search name or code: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t", product["price"], "\t", product["name"])
            break
    else:
        print("not found")
        #doesnt find by name!!

def make_qrcode():
    user_input = input("enter product code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            qr = qrcode.make(product)
            qr.save (product["code"] + (".png"))
            print("qr code for product", product["code"], "successfully saved")
            break
    else:
        print("Not such a product! try again later")
            

def buy():
    total_factor_price = 0
    card = []
    
    while True:
        user_input = input("enter product code or 'fin' to finish buying: ")
        if user_input.lower() == "fin":
            for product in card:
                 print("code", "\t", "name" , "\t", "price", "\t", "amount", "\t", "total_price")
                 print(product["code"], "\t", product["name"] , "\t", product["price"], "\t", product["amount"], "\t", product["total_price"])
            print("total factor price is: ", total_factor_price)
            break
        for product in PRODUCTS:
            if product["code"] == user_input:
                buy_demand = int(input("Enter the amount you want to buy: "))
                if buy_demand <= product["stock"]:
                    product["stock"] = product["stock"] - buy_demand
                    total_price = product["price"] * buy_demand
                    total_factor_price = total_price + total_factor_price
                    purchase_product = {"code": product["code"], "name": product["name"], "price": product["price"], "amount": buy_demand, "total_price": product["price"] * buy_demand}
                    card.append(purchase_product)
                    break
                else:
                    print("The maximum amount you can buy is: ", product["stock"])

                    
                
def write_database():
    f = open("07-Database.txt", "w")
    for product in PRODUCTS:
            line = f"{product['code']},{product['price']},{product['stock']},{product['name']}"
            f.write(line)
    f.close
    print("Database updated successfully")




print("Welcome")
print("Loading...")
read_database()
print("Loaded")

# print(PRODUCTS)
while True:
    menu()
    choice = int(input("enter a number: "))


    if choice ==1 :
        add()
    elif choice ==2 :
        edit()
    elif choice ==3 :
        remove()
    elif choice ==4 :
        search()
    elif choice ==5 :
        show_list()
    elif choice ==6 :
        buy()
    elif choice ==8 :
        make_qrcode()

    elif choice ==7 :
        write_database()
        exit(0)
        break

    else:
        print("Enter correctly!")






# for product in PRODUCTS:
#     print(product)
