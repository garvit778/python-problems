print("welcome to the machine sir ")
profit = 0
menu = { 
    "espresso" :
    {
        "ingredients" :{
            "water": 50,
            "coffee": 18,
        },
        "cost" : 1.5
    },
     
    "latte" : {
        "ingredients" : {
            "water": 200 ,
            "coffee" : 24 ,
            "milk" : 150
            
        },
        'cost' : 2.5
    },
   "Cappuccino" : {
       "ingredients":{
           "water": 250,
            "milk": 100,
            "coffee": 24,
       },
       'cost' : 3
   }
    
}



resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficient(order_ingredients):
    is_enough = True
    for i in order_ingredients:
        if order_ingredients[i] >= resources[i]:
            print (f"sorry there is not enough {i} " )
            is_enough = False
        else:
            is_enough = True
def process_coins():
        total  = int(input ("how many quarters?:"))*0.25
        total +=int(input ("how many dimes?")) *0.1
        total +=int(input ("how many nickles?")) *0.05
        total +=int(input(" how many pennies?:"))*0.01
        return total
def is_transaction_sucessful(money_recieved,drink_cost):
    if money_recieved>= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"here is your {change} change")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry that's not enough money , your money has been refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} \U0001F60B")


is_on = True    
while is_on:
    order = input ("what would you like? (espresso/latte/Cappuccino)")
    if order == "off":
        is_on =False
    elif order == "report":

        print(f"water: {resources['water'] } ml")
        print(f"milk: {resources['milk']} ml ")
        print(f"coffee : {resources['coffee'] } g ")
        print(f'money : ${profit}')
    else :
        drink = menu[order]
        resource_sufficient(drink["ingredients"])
        payment = process_coins()
        if is_transaction_sucessful(payment,drink['cost']):
            make_coffee(order,drink["ingredients"])


    
       
        
        
        
        
        
        

                



        
        

        

