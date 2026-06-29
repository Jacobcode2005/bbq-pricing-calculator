import dictionarys
import data_functions
import calculator_functions
import business_logic
# This program calculates the final price of meat
# based on the type of meat, the supplier price and the amount cooked off
# for a barbecue catering company

# gets the input for the sides
def ask_sides():
    user_sides = []
    while True:
     try: 
        number_of_sides = int(input("How many sides do you want? please insert a value between 1 and 4 "))
        if number_of_sides > 0 and number_of_sides < 5:
            break
     except ValueError:
         print("incorrect value please put a whole number between 1 and 4")
    
    for _ in range(number_of_sides):
        while True:
            print(data_functions.list_sides())
            side_type= input("What is your side? ").strip().lower()
            side_validation = data_functions.side_validation(side_type)
            if side_validation == True:
                break
            else:
                print("Error please enter one of the listed sides")
      
        side_data = data_functions.set_data(side_type)
        user_sides.append(side_data)
    return user_sides

def print_sides(order):
    for sides in order["sides"]:
        print(f"The side is {sides['name']}\n",
            f"The number of half pans needed is {sides['number_of_half']}\n",
            f"The price for just this side is ${sides['price']}")
        
def print_totals(order):
    print(f"The total side price is ${round(order['totals']['side_total'], 2)}\n",
          f"The total meat price with markup is ${round(order['totals']['meat_total'],2 )}\n",
          f"The final price for the order is ${round(order['totals']['final_price'],2)}")

def main():
    order= data_functions.copy_order()
   
   #ask how many meats in the order
    while True:
        try:
            meat_number= int((input("How many meats are you having 1 or 2? ")))
          
            if meat_number == 1 or meat_number == 2:
                break
        except ValueError:
            print("Incorrect value please enter either 1 or 2 ")
  
   # asking what the first meat is
    print("What type of meat do you want?")
    print(data_functions.list_meat())
    while True:
        meat_one = (input("Please type the type of meat you want ").strip().lower()) 
        validation_one= data_functions.meat_validation(meat_one)
        if validation_one == True:
            break
        else:
             print("Incorrect option please enter a valid meat type")

    
    #getting the number of people served
    while True:
        try:
            number_of_people = int(input("How many people are you serving? "))
            if number_of_people >=0:
                break
        except ValueError:
           print("Error incorect value")
    
    meat_data_one = data_functions.set_data(meat_one)
    #ask for the markup percent 
    while True:
        try:
            markup_percent = float(input("What would you like your markup percent to be? Please put as a decimal"))
            if 0<= markup_percent <1:
                break
        except ValueError:
            print("Error incorect value please put your percentege as a decimal")
    #if there is only one meat calculate the final cost and terminate the program
    if meat_number == 1:
        supplier_cost, raw_weight = calculator_functions.calculator(number_of_people, meat_data_one, meat_data_one["ounces_per_person"])
        data_functions.append_order_meats(order,meat_one,raw_weight,supplier_cost)
        sides_data  = ask_sides()
        side_total, order = business_logic.sides_logic(sides_data, number_of_people,order)
        
        final_cost, meat_price = (calculator_functions.markup_calc(supplier_cost, markup_percent, side_total))
        order = data_functions.append_order_totals(order, meat_price, side_total, final_cost )
        print_sides(order)
        
        print(f"The amount of raw meat needed is {round(order['meats'][meat_one]["raw_weight"],2)}\n",
              f"The total cost for you is {round(order["meats"][meat_one]["supplier_cost"], 2)}\n",)
        print_totals(order)
        

        return
    #ask for the second meat 
    while True:
        meat_two = input("What is the second meat? ").strip().lower()
        validation_two = data_functions.meat_validation(meat_two)
        if validation_two == True:
            break
        else:
            print("Not a valid meat type")
    meat_data_two = data_functions.set_data(meat_two)
    #ask for the serving style
    while True:
        serving_type = input("Is everyone having both meats or one or the other? Please answer either both or one ").strip().lower()
        if serving_type == "both" or serving_type == "one":
            break
        else: 
            print("please inter either both or one ")
   #if the serving style is both then use oz per person both instead of ounces per person then terminate the program
    if serving_type == "both":
        supplier_cost, raw_weight= calculator_functions.calculator(number_of_people, meat_data_one, meat_data_one["oz_per_person_both"])
        supplier_cost_one, raw_weight_2 = calculator_functions.calculator (number_of_people,  meat_data_two, meat_data_two["oz_per_person_both"])
        total_cost= supplier_cost + supplier_cost_one
        sides_data  = ask_sides()
        side_total, order = business_logic.sides_logic(sides_data, number_of_people,order)
        
        order = data_functions.append_order_meats(order, meat_one,raw_weight, supplier_cost)
        order = data_functions.append_order_meats(order, meat_two, raw_weight_2 ,supplier_cost_one)
    
        final_cost, meat_total = (calculator_functions.markup_calc(total_cost, markup_percent, side_total)) 
        order = data_functions.append_order_totals(order, meat_total, side_total, final_cost)
        print_sides(order)
        print_totals(order)

        print(f"The amount of raw meat you need is {order['meats'][meat_one]['raw_weight']} lbs. of {order['meats'][meat_one]['name']} and {order['meats'][meat_two]['raw_weight']} lbs. of {order['meats'][meat_two]['name']}\n")
        return
        
        
    #if the serving style is one then just use ounces per person then terminate the program
    else:
        supplier_cost, raw_weight= calculator_functions.calculator(number_of_people, meat_data_one, meat_data_one["ounces_per_person"])
        supplier_cost_one, raw_weight_2 = calculator_functions.calculator (number_of_people,  meat_data_two, meat_data_two["ounces_per_person"])
        total_cost= supplier_cost + supplier_cost_one
        sides_data  = ask_sides()
        side_total,order = business_logic.sides_logic(sides_data, number_of_people,order)
        final_cost, meat_total = (calculator_functions.markup_calc(total_cost, markup_percent, side_total)) 
        order = data_functions.append_order_totals(order, meat_total, side_total, final_cost)
        order = data_functions.append_order_meats(order, meat_one,raw_weight, supplier_cost)
        order = data_functions.append_order_meats(order, meat_two, raw_weight_2 ,supplier_cost_one)
        print_sides(order)
        print_totals(order)
        print(f"The amount of raw meat you need is {order['meats'][meat_one]['raw_weight']} lbs. of {order['meats'][meat_one]['name']} and {order['meats'][meat_two]['raw_weight']} lbs of {order['meats'][meat_two]['name']}\n")
        return
        


    

main()