import dictionarys
import copy
#========================
# DATA FUNCTIONS
#========================
#provides the data of the meat from the Dictonary
def set_data(object):
    if object in dictionarys.meats:   
        return dictionarys.meats[object]
    elif object in dictionarys.sides:
        return dictionarys.sides[object]
#provides avalible meat options
def list_meat():
    return dictionarys.meats.keys()
#provides the avalible sides options
def list_sides():
    return dictionarys.sides.keys()
#validates the users meat type
def meat_validation(object):
    if object in dictionarys.meats:
        return True
    else:
        return False
#validates the users side type
def side_validation(object):
    if object in dictionarys.sides:
        return True
    else:
        return False
#copys the order to ensure that the original diconary is not used
def copy_order():
    order= copy.deepcopy(dictionarys.order)
    return order

def append_order_meats(order, meat_type, raw_weight, supplier_cost):
    order ["meats"][meat_type] ={"name": meat_type, "raw_weight": raw_weight,
                                 "supplier_cost": supplier_cost }
    return order


def append_order_sides(order, side_type, number_of_half, price):
    order ["sides"].append({"name": side_type,
                       "number_of_half": number_of_half,
                        "price":price})
    return order
def append_order_totals(order, meat_total, side_total, final_price):
    order["totals"] = {"meat_total":meat_total,
                       "side_total": side_total,
                       "final_price": final_price}
    return order