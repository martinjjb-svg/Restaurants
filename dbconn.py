import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Martin",
  password="password",
  database="restaurants"
)

mycursor = mydb.cursor()
'''
sql = "INSERT INTO restaurants (name, address, nationality, tel, comment, rating) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    ('Pizza Express', '1 High St, Harpenden, Albans', 'European, Italian', '01582765714', 'Easy, close to common', '5'),
    ('Aqua Shard', '32 London Bridge St, London', 'European, British', '02030111256', 'Smart fashionable, great views of London', '9')
    ]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")'''

# mycursor.execute ("CREATE TABLE users (name VARCHAR(255), restaurant VARCHAR(255), fav_food VARCHAR(255), fav_drink VARCHAR(255))")
'''
sql = "INSERT INTO users (name, restaurant, fav_food, fav_drink) VALUES (%s, %s, %s, %s)"
val = [
    ('Martin', 'Aqua Shard', 'Grilled Hand-Dived Scallops', 'Cloudy Bay 2020 Sauvignon Blanc, Marlborough, NZ'),
    ('Karen', 'Aqua Shard', 'Cornish Sea Bass', 'Cabernet-Merlot-Tempranillo 2019 Villa d Orta, Somontano, Spain'),
    ('Jordan', 'Aqua Shard', 'Beef Fillet', 'Meantime London Lager'),
    ('Hannah', 'Aqua Shard', 'Beef Fillet', 'Diet Coke'),
    ('Rose', 'Aqua Shard', 'Cornish Sea Bass', 'Pineapple Juice')
    ]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")'''

# sql = "UPDATE restaurants SET rating = 7 WHERE name = 'Sketch'"
# mycursor.execute(sql)
# mydb.commit()
