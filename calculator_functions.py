#=========================
#  CALCULATOR FUNCTIONS
#=========================
#estimates the amount of cooked meat for an order
def estimate_meat_needed( number_of_people, ounces_per_person):
    
    total_ounces = ounces_per_person * number_of_people
    total_cooked_pounds = total_ounces /16
    return total_cooked_pounds
#generate the total price
def total_calc( meat_totals, side_total):
    total_price = meat_totals + side_total
    return total_price
#estimates the amount of raw meat needed and the supplier cost
def calculator(number_of_people, meat_type, oz_per_person):
    
        total_cooked_pounds= estimate_meat_needed( number_of_people, oz_per_person)
        raw_weight = total_cooked_pounds/ meat_type["cooked_off_weight"]
        raw_weight= round(raw_weight, 2)
        #meat prices are fixed per pound based on the business pricing model
        meat_total = total_cooked_pounds * meat_type["price_per_pound"]
        meat_total = round(meat_total, 2)
        return meat_total, raw_weight
# rounds the number of half pansif there is a remander always round up
def side_round(number_of_people, number_of_people_per, ):
     remander= number_of_people % number_of_people_per
     number_of_half = (number_of_people - remander)/ number_of_people_per
     if remander > 4:
        number_of_half = number_of_half + 1
        return number_of_half
     else:
          return number_of_half
#estimates the total side cost
def side_calc(number_of_half, side_price):
     side_price = number_of_half * side_price
     return side_price
