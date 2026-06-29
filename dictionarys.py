# where the data is stored 
meats= {
    "brisket": {"name": "brisket", "ounces_per_person": 5, "oz_per_person_both" : 3, "supplier_price": 9.12, "cooked_off_weight": .50},
    "pork" : {"name": "pork", "ounces_per_person": 4, "oz_per_person_both": 3, "supplier_price" : 2.20, "cooked_off_weight": .50},
    "chicken": {"name": "chicken", "ounces_per_person": 4, "oz_per_person_both": 2.50, "supplier_price": 2.50, "cooked_off_weight": .70}
}

sides= {
    "mac and cheese": {"name": "mac and cheese", "price_per_half_pan": 25, "half_pan_people": 15},
    "baked beans" :{ "name": "baked beans", "price_per_half_pan": 20, "half_pan_people": 22},
    "cole slaw" :{"name": "cole slaw", "price_per_half_pan":18, "half_pan_people": 25 },
    "green beans":{"name": "green beans", "price_per_half_pan" : 18, "half_pan_people": 15}
}
# gains peices of the whole order as the program runs
# sides has to be a list to ensure multiple sides does not break the program
order={"meats":{},
       "sides":[],
       "totals":{}}