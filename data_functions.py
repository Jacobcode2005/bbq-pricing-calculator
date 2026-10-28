import sqlite3
from flask import g 
# create or reuse an sqlight
def getdb():
    if "db" not in g:
        g.db= sqlite3.connect("pig_and_pies.db")
    return g.db

#========================
# SET FUNCTIONS
#========================
def set_meats(object):

    db = getdb()
    cursor= db.cursor()
    object =object.lower()
    cursor.execute("select * from meats where meatID = ?", (object,))
        
    meat_object = cursor.fetchone()
    meat_data = {
            "meatID" : meat_object[0], "price_per_pound": meat_object[1], "oz_per_person": meat_object [2], "cooked_off_weight": meat_object [3]
        }
    return meat_data
def get_meat_name():
    db= getdb()
    cursor= db.cursor()
    cursor.execute("select meatID from meats")
    meat_names= cursor.fetchall()
    meatlist=[]
    for names in meat_names:
        meatlist.append(names[0])
    
    return meatlist
    
def set_sides(object):
     db = getdb()
     cursor= db.cursor()
    
     cursor.execute("select * from sides where sideID = ?", (object,))
     side_object = cursor.fetchone()
     side_data = {
            "sideID": side_object[0], "price_per_half_pan" : side_object[1], "half_pan_people": side_object[2]
        }
     return side_data
def get_side_names():
    db = getdb()
    cursor= db.cursor()
    cursor.execute("select sideID from sides")
    side_names= cursor.fetchall()
    sidelist=[]
    for names in side_names:
        sidelist.append(names[0])
    return sidelist
def set_order(order_number):
    #lookup and return order
    #Retrieve a saved order and combine its meats, sides, and totals
    #into a dictionary used to display the order receipt.
    
    meat_list=[]
    side_list=[]
    db = getdb()
    cursor= db.cursor()
    cursor.execute("select * from orders where orderID = ?", (order_number,))
    order = cursor.fetchone()
    cursor.execute("select * from orderMeats where orderID= ?", (order_number,))
    meats= cursor.fetchall()
    for o in meats:
        meat_list.append({"meatID": o[0], "meat_total": o[2], "raw_weight": o[3]})
    cursor.execute("select * from orderSides where orderID= ?",(order_number,))
    sides= cursor.fetchall()
    for i in sides:
         side_list.append({"sideID": i[0], "number_of_half":i[2], "side_total": i[3]})
    order_data= {"order_number": order[0], "number_of_people":order[1],"meat_total":order[2],"side_total": order[3],"final_price":order[4],"date":order[5],
                 "meats": meat_list, "sides": side_list }
    return order_data
def get_order_number():
    db=getdb()
    cursor = db.cursor()
    cursor.execute("select orderID from orders Order by orderID DESC")
    ids= cursor.fetchall()
    idlist= []
    for id in ids:
        idlist.append(id[0])
    return idlist
#========================
# LIST FUNCTIONS
#========================
def list_meat():
    db = getdb()
    cursor= db.cursor()
    cursor.execute("select meatID from meats")
    meat_names= cursor.fetchall()
    for meats in meat_names:
        print(meats)
    

def list_sides():
    db = getdb()
    cursor= db.cursor()
    cursor.execute("select sideID from sides")
    side_names= cursor.fetchall()
    for sides in side_names:
        print (sides)

#========================
# APPEND ORDER FUNCTIONS
#========================
def append_order_meats(order_id, meat_type, raw_weight, supplier_cost):
    db = getdb()
    cursor= db.cursor()
    cursor.execute("insert into orderMeats(meatID,orderID, meat_total, raw_weight )" \
    "values(?,?,?,?)", (meat_type, order_id ,supplier_cost, raw_weight, ))
    cursor.execute("commit")
    


def append_order_sides(order_number, side_type, number_of_half, price):
    db = getdb()
    cursor= db.cursor()
    cursor.execute("insert into orderSides(sideID, orderID, number_of_half, side_price)" \
    "values(?,?,?,?)",(side_type, order_number,number_of_half, price ))
    cursor.execute("commit")
def append_order_totals(order_number, meat_total, side_total, final_price, number_of_people):
    db = getdb()
    cursor= db.cursor()
    cursor.execute("update orders " \
    "set number_of_people = ?, meat_total = ? , side_total = ?,final_price = ? " \
    "where orderID = ?", (number_of_people, meat_total, side_total, final_price,order_number,))
    cursor.execute("commit")
# starts a new order
def start_order():
    #Generates order_number
    db = getdb()
    cursor= db.cursor()
    cursor.execute("select max(orderID) from orders")
    result = cursor.fetchone()
    # adds one to the previous order number 
    if result[0] != None:
        order_id = result[0] +1
        cursor.execute("insert into orders(orderID, date_made)" \
        "values(?, date('now'))",(order_id,))
        cursor.execute("commit")
        return order_id
    else :
        cursor.execute("insert into orders(orderID, date_made)" \
        "values(?, date('now'))",(1,))
        cursor.execute("commit")
        order_number =1
        return order_number

   
    