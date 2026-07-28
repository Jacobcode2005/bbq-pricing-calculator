import sqlite3

def make_database():
# create the database if it does not exist
    con = sqlite3.connect("pig_and_pies.db")
    cur = con.cursor()
#========================
#   CREATE TABLES 
#========================
    cur.execute("create table if not exists meats(meatID varchar(50) primary key, price_per_pound real, oz_per_person real, cooked_off_weight real)")

    cur.execute("create table if not exists sides(sideID varchar(50) primary key,  price_per_half_pan real, half_pan_people int)")

    cur.execute("create table if not exists orders(orderID int primary key, number_of_people int, meat_total real, side_total real , final_price real, date_made date)")

    cur.execute("create table if not exists orderMeats(meatID varchar(50), orderID int, "
    "meat_total real, raw_weight real,  primary key(MeatID, orderID)," \
    "foreign key(meatID) references meats(meatID) " \
    "foreign key(orderID) references orders(orderID) )")

    cur.execute("create table if not exists orderSides(sideID varchar(50), orderID int, number_of_half int, side_price real," \
    "primary key(sideID, orderID)," \
    "foreign key(sideID) references sides(sideID)," \
    "foreign key(orderID)references orders(orderID) )")
#========================
# SET MEATS INTO DATABASE 
#========================
    cur.execute("insert into meats (meatID, price_per_pound, oz_per_person, cooked_off_weight) " \
    "values ('brisket', 25, 5, .50 )"\
    "on conflict(meatID) do nothing")

    cur.execute("insert into meats (meatID, price_per_pound, oz_per_person, cooked_off_weight) " \
    "values ('pork', 16, 4,.50 )"\
    "on conflict(meatID) do nothing")

    cur.execute("insert into meats (meatID, price_per_pound, oz_per_person, cooked_off_weight) " \
    "values ('chicken', 16, 4,.70 )"\
    "on conflict(meatID) do nothing")
#========================
# SET SIDES INTO DATABASE
#========================
    cur.execute("insert into sides(sideID, price_per_half_pan, half_pan_people)" \
    "values ('mac and cheese', 25, 15)" \
    "on conflict(sideID) do nothing")

    cur.execute("insert into sides(sideID, price_per_half_pan, half_pan_people)" \
    "values ('baked beans', 20, 22)" \
    "on conflict(sideID) do nothing")

    cur.execute("insert into sides(sideID, price_per_half_pan, half_pan_people)" \
    "values ('cole slaw', 18, 25)" \
    "on conflict(sideID) do nothing")

    cur.execute("insert into sides(sideID, price_per_half_pan, half_pan_people)" \
    "values ('green beans', 18, 15)" \
    "on conflict(sideID) do nothing")
    cur.execute("commit")

