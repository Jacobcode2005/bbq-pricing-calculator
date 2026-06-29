import calculator_functions
import data_functions
#does all of the calculatons and adding of the sids to order 
#is its own file because it did not fit into any pre established file
def sides_logic(sides_data, number_of_people,order):
    half_pan_list=[]
    total_side= 0
    for sides in sides_data:
            
            number_of_half = calculator_functions.side_round(number_of_people, sides["half_pan_people"])
            side_price = calculator_functions.side_calc(number_of_half, sides["price_per_half_pan"])
            order = data_functions.append_order_sides(order,sides["name"], number_of_half, side_price)
            total_side= total_side+ side_price
            half_pan_list.append(number_of_half)
    return total_side,order
