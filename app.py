"""
Main Flask application for the BBQ Pricing Calculator.

Handles page routing, order submissions, database connections,
and returning order information to the frontend.
"""
from flask import Flask , render_template, jsonify, request, g
import data_functions
import calculator_functions
import business_logic
import databases
import sqlite3
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/past_order")
def past_order_page():
    orderid= data_functions.get_order_number()
    return render_template("past_orders.html", order_number= orderid)
@app.route("/new_order")
def new_order():
    meat_names=data_functions.get_meat_name()
    side_names=data_functions.get_side_names()
    return render_template("new_order.html", meats= meat_names, sides= side_names)
@app.route("/edit_database")
def edit_database_page():
    meat_names=data_functions.get_meat_name()
    side_names=data_functions.get_side_names()
    return render_template("edit_database.html", meats= meat_names, sides= side_names)
def getdb():
    if "db" not in g:
        g.db= sqlite3.connect("pig_and_pies.db")
    return g.db


@app.teardown_appcontext
def close_db(exeption):
    """Close the SQLite connection when the Flask context ends."""
    db=g.pop("db",None)
    if db is not None:
        db.close()
        
@app.route("/submit_order", methods= ["POST"])
def submit_order():
   """Process a new catering order.

    Retrieve selected meat and side information, calculate costs,
    save the order to SQLite, and return receipt data as JSON.
    """
   databases.make_database()
   data= request.get_json()
   meats = data["meat"]
   sides = data["side"]
   number_of_people = data["number_of_people"]
   print(number_of_people)
   meat_list= []
   side_list =[]
   total_meat_cost =0
   order_number =data_functions.start_order()
   # Retrieve pricing information for the selected meats and sides.
   for meat in meats:
        data_meat = data_functions.set_meats(meat)
        meat_list.append(data_meat)


   for side in sides:
        data_side = data_functions.set_sides(side)
        side_list.append(data_side)

# Calculate the required meat quantities and save each item to the order.
   for meats in meat_list:
        meat_total, raw_weight =calculator_functions.calculator(number_of_people, meats , meats["oz_per_person"])
        data_functions.append_order_meats(order_number,meats["meatID"], raw_weight, meat_total)
        total_meat_cost = total_meat_cost + meat_total

# Calculate the final price, save the totals, and return the receipt.
   total_side = business_logic.sides_logic(side_list,number_of_people, order_number) 
   final_price = calculator_functions.total_calc(total_meat_cost,total_side)     
   data_functions.append_order_totals(order_number,total_meat_cost, total_side, final_price, number_of_people)
   order_data = data_functions.set_order(order_number)
   return jsonify(order_data)

@app.route("/past_order", methods = ["POST"])
def past_order():
    """Retrieve a previously saved order and return it as JSON."""
    data= request.get_json()
    ordernumber=data["order_number"]
    order_data= data_functions.set_order(ordernumber)
    return jsonify(order_data)

if __name__ == "__main__":
    app.run(debug= True)