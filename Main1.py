# This program calculates the final price of meat
# based on the type of meat, the supplier price and the amount cooked off
# for a barbecue catering company

dictionary= {
    "brisket": {"ounces_per_person": 5, "oz_per_person_both" : 3, "supplier_price": 9.12, "cooked_off_weight": .50},
    "pork" : {"ounces_per_person": 4, "oz_per_person_both": 3, "supplier_price" : 2.20, "cooked_off_weight": .50},
    "chicken": {"ounces_per_person": 4, "oz_per_person_both": 2.50, "supplier_price": 2.50, "cooked_off_weight": .70}
}
#========================
# API FUNCTIONS
#========================
#provides the data of the meat from the Dictonary
def meat_api(meat_type):
    if meat_type in dictionary:   
        return dictionary[meat_type]
#provides avalible meat options
def meat_api_list():
    return dictionary.keys()
#validates the users meat type
def meat_api_validation(meat_type):
    if meat_type in dictionary:
        return True
    else:
        return False
#=========================
#  CALCULATOR FUNCTIONS
#=========================
#estimates the amount of cooked meat for an order
def estimate_meat_needed( number_of_people, ounces_per_person):
    
    total_ounces = ounces_per_person * number_of_people
    total_cooked_pounds = total_ounces /16
    return total_cooked_pounds
#generate the total price by marking up the supplier cost  
def markup_calc( supplier_cost, markup_percent):
    markup_percent = markup_percent +1
    total_price = supplier_cost * markup_percent
    return total_price
#estimates the amount of raw meat needed and the supplier cost
def calculator(number_of_people, meat_type, oz_per_person):
    
        total_cooked_pounds= estimate_meat_needed( number_of_people, oz_per_person)
        raw_weight = total_cooked_pounds/ meat_type["cooked_off_weight"]
        raw_weight= round(raw_weight, 2)
        supplier_cost = raw_weight * meat_type["supplier_price"]
        return supplier_cost, raw_weight
    


def main():
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
    print(meat_api_list())
    while True:
        meat_one = (input("Please type the type of meat you want ").strip().lower()) 
        validation_one= meat_api_validation(meat_one)
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
    
    meat_data_one = meat_api(meat_one)
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
        supplier_cost, raw_weight = calculator(number_of_people, meat_data_one, meat_data_one["ounces_per_person"])
        final_cost = markup_calc(supplier_cost, markup_percent)
        print(f"The amount of raw meat needed is {raw_weight}\n",
              f"The total supplier cost before is {supplier_cost}\n",
              "The total cost for the customer is $", round(final_cost, 2))

        return
    #ask for the second meat 
    while True:
        meat_two = input("What is the second meat? ").strip().lower()
        validation_two = meat_api_validation(meat_two)
        if validation_two == True:
            break
        else:
            print("Not a valid meat type")
    meat_data_two = meat_api(meat_two)
    #ask for the serving style
    while True:
        serving_type = input("Is everyone having both meats or one or the other? Please answer either both or one ").strip().lower()
        if serving_type == "both" or serving_type == "one":
            break
        else: 
            print("please inter either both or one ")
   #if the serving style is both then use oz per person both instead of ounces per person then terminate the program
    if serving_type == "both":
        supplier_cost, raw_weight= calculator(number_of_people, meat_data_one, meat_data_one["oz_per_person_both"])
        supplier_cost_one, raw_weight_2 = calculator (number_of_people,  meat_data_two, meat_data_two["oz_per_person_both"])
        total_cost= supplier_cost + supplier_cost_one
        final_cost = markup_calc(total_cost, markup_percent)
        print(f"The amount of raw meat you need is {raw_weight} of {meat_one} and {raw_weight_2} of {meat_two}\n",
              f"The total cost to you is ${total_cost}\n",
              f"The total cost for the customer is $ {round(final_cost, 2)}")
        return
    #if the serving style is one then just use ounces per person then terminate the program
    else:
        supplier_cost, raw_weight= calculator(number_of_people, meat_data_one, meat_data_one["ounces_per_person"])
        supplier_cost_one, raw_weight_2 = calculator (number_of_people,  meat_data_two, meat_data_two["ounces_per_person"])
        total_cost= supplier_cost + supplier_cost_one
        final_cost = markup_calc(total_cost, markup_percent)
        print(f"The amount of raw meat you need is {raw_weight} of {meat_one} and {raw_weight_2} of {meat_two}\n",
              f"The total cost to you is ${total_cost}\n",
              f"The total cost for the customer is $ {round(final_cost, 2)}")
        


    

main()