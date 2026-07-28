import sqlite3
import copy
con = sqlite3.connect("pig_and_pies.db")
cur = con.cursor()
#========================
# SET FUNCTIONS
#========================
def set_meats(object):
     
    cur.execute("select * from meats where meatID = ?", (object,))
        
    meat_object = cur.fetchone()
    meat_data = {
            "meatID" : meat_object[0], "price_per_pound": meat_object[1], "oz_per_person": meat_object [2], "cooked_off_weight": meat_object [3]
        }
    return meat_data
    
    
def set_sides(object):
     cur.execute("select * from sides where sideID = ?", (object,))
     side_object = cur.fetchone()
     side_data = {
            "sideID": side_object[0], "price_per_half_pan" : side_object[1], "half_pan_people": side_object[2]
        }
     return side_data
#========================
# LIST FUNCTIONS
#========================
def list_meat():
    cur.execute("select meatID from meats")
    meat_names= cur.fetchall()
    for meats in meat_names:
        print(meats)
    

def list_sides():
    cur.execute("select sideID from sides")
    side_names= cur.fetchall()
    for sides in side_names:
        print (sides)
    
#========================
# VALIDATION FUNCTIONS
#========================

#validates the users meat type
def meat_validation(object):
    cur.execute("select meatID from meats where meatID = ?", (object,))

    result= cur.fetchall()
    if result:
        return True
    else:
        return False
#validates the users side type
def side_validation(object):
    cur.execute("select sideID from sides where sideID = ?", (object,))
    result = cur.fetchall()
    if result:
        return True
    else:
        return False

def order_number_validation(order_number):
    cur.execute("select orderID from orders where orderID = ?", (order_number,))
    result= cur.fetchone()
    if result:
        return True
    else:
        return False
def order_validation():
    cur.execute("select orderID from orders")
    result= cur.fetchall()
    return result
#========================
# APPEND ORDER FUNCTIONS
#========================
def append_order_meats(order_id, meat_type, raw_weight, supplier_cost):
    cur.execute("insert into orderMeats(meatID,orderID, meat_total, raw_weight )" \
    "values(?,?,?,?)", (meat_type, order_id ,supplier_cost, raw_weight, ))
    cur.execute("commit")
    


def append_order_sides(order_number, side_type, number_of_half, price):
    cur.execute("insert into orderSides(sideID, orderID, number_of_half, side_price)" \
    "values(?,?,?,?)",(side_type, order_number,number_of_half, price ))
    cur.execute("commit")
def append_order_totals(order_number, meat_total, side_total, final_price, number_of_people):
    cur.execute("update orders " \
    "set number_of_people = ?, meat_total = ? , side_total = ?,final_price = ? " \
    "where orderID = ?", (number_of_people, meat_total, side_total, final_price,order_number,))
    cur.execute("commit")
# starts a new order
def start_order():
    cur.execute("select max(orderID) from orders")
    result = cur.fetchone()
    # adds one to the previous order number 
    if result[0] != None:
        order_id = result[0] +1
        cur.execute("insert into orders(orderID, date_made)" \
        "values(?, date('now'))",(order_id,))
        cur.execute("commit")
        return order_id
    else :
        cur.execute("insert into orders(orderID, date_made)" \
        "values(?, date('now'))",(1,))
        cur.execute("commit")
        order_number =1
        return order_number
# prints the full order
def print_order(order_number):
    cur.execute("select * from orderMeats where orderID = ?" , (order_number,))
    
    object =cur.fetchall()
    print(f"The order number is {object[0][1]}")
    for  meat in object:
        print(f"The meat type is {meat[0]}\n"
          f"The total for this meat is {meat[2]}\n"
          f"The amount of raw weight needed is {meat[3]}\n")
    
    cur.execute("select * from orderSides where orderID = ?", (order_number,))

    sides= cur.fetchall()
    for side in sides:
        print(f"The side is {side[0]}\n"
              f"The number of half pans is {side[2]}\n"
              f"The total for this side is {side[3]}\n")
        
    cur.execute("select * from orders where orderID = ?", (order_number,))
    orders = cur.fetchall()

    print(f"The number of people needed is {orders[0][1]}\n",
          f"The total for the meat is {orders[0][2]}\n"
          f"The total for the sides is {orders[0][3]}\n"
          f"The final price is {orders[0][4]}\n")
   
    