
import data_functions
import calculator_functions
import business_logic
import databases
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
            data_functions.list_sides()
            side_type= input("What is your side? ").strip().lower()
            side_validation = data_functions.side_validation(side_type)
            if side_validation == True:
                break
            else:
                print("Error please enter one of the listed sides")
      
        side_data = data_functions.set_sides(side_type)
        user_sides.append(side_data)
    return user_sides

        


def main():
   
    databases.make_database()
    #decide if making a new order in database or looking up an old one
    while True:
        program_type = input("Are you looking up a previous order or making a new entry plase type old or new ").strip().lower()
        if program_type == "old" or program_type == "new":
            break
        else:
            print("incorrect value please type new or old")

    # look up the old order if there is no orders in the database end the program 
    if program_type == "old":
     result = data_functions.order_validation()
     if result == []:
         print("No orders in database please start and order before trying to find an old one")
         return
     while True:
            order_number = int(input("what is the order number?"))
            result = data_functions.order_number_validation(order_number)
            if result == True:
                break
            else:
                print("incorect order number please put a proper order number")
     data_functions.print_order(order_number)
     return
    
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
    data_functions.list_meat()
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
    
    meat_data_one = data_functions.set_meats(meat_one)
    
    #if there is only one meat calculate the final cost and terminate the program
    if meat_number == 1:
        order_number = data_functions.start_order()
        meat_total, raw_weight = calculator_functions.calculator(number_of_people, meat_data_one, meat_data_one["oz_per_person"])
        data_functions.append_order_meats(order_number,meat_one,raw_weight, meat_total)
        sides_data  = ask_sides()
        side_total = business_logic.sides_logic(sides_data, number_of_people,order_number)
        
        final_cost = (calculator_functions.total_calc(meat_total ,side_total))
        final_cost = round(final_cost, 2)
        meat_total = round(meat_total,2)
        data_functions.append_order_totals(order_number, meat_total, side_total, final_cost, number_of_people )
     
        
        data_functions.print_order(order_number)
        
        

        return
    #ask for the second meat 
    while True:
        meat_two = input("What is the second meat? ").strip().lower()
        validation_two = data_functions.meat_validation(meat_two)
        if validation_two == True:
            break
        else:
            print("Not a valid meat type")
    meat_data_two = data_functions.set_meats(meat_two)
   
    #calculate the order then terminate the program
    order_number = data_functions.start_order()
    meat_total, raw_weight= calculator_functions.calculator(number_of_people, meat_data_one, meat_data_one["oz_per_person"])
    meat_total_1, raw_weight_2 = calculator_functions.calculator (number_of_people,  meat_data_two, meat_data_two["oz_per_person"])
    total_meat_cost= meat_total + meat_total_1
    sides_data  = ask_sides()
    side_total = business_logic.sides_logic(sides_data, number_of_people,order_number)
    final_cost= (calculator_functions.total_calc(total_meat_cost, side_total)) 
    final_cost = round(final_cost, 2)
    
    data_functions.append_order_totals(order_number, meat_total, side_total, final_cost, number_of_people)
    data_functions.append_order_meats(order_number, meat_one,raw_weight, meat_total)
    data_functions.append_order_meats(order_number, meat_two, raw_weight_2 ,meat_total_1)
    
    
    data_functions.print_order(order_number)
    return
        


    

main()