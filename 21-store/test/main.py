import sqlite3

con = sqlite3.connect("chinook.db")
my_cursor = con.cursor()

# for data in my_cursor.execute("SELECT * FROM customers WHERE Country = 'France' "):
#     print(data)
result = my_cursor.execute("SELECT * FROM customers WHERE Country ='Germany'")
ger_customers = result.fetchall()

for i in ger_customers:
    print(i)


# my_cursor.execute("INSERT INTO genres(GenreId, Name) Values(26, 'Sonati')")
# con.commit()

my_cursor.execute("UPDATE customers SET City='Mashhad', Country='Iran' WHERE FirstName='Helena' AND CustomerId=6")
con.commit()
