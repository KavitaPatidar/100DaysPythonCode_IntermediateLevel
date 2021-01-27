MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    # converting coins into dollar after taking input
    quarters = int(input("How many quarters?")) / 4
    dimes = int(input("How many dimes?")) / 10
    nickles = int(input("How many nickles?")) / 20
    pennies = int(input("How many pennies?")) / 100
    total = (quarters + dimes + nickles + pennies)
    return total

def transaction_successful(customer_money, drink_cost):
    if customer_money > drink["cost"]:
        global profit
        profit+=drink_cost
        return_money = round(customer_money - drink_cost, 2)
        print(f"Here is {return_money} in change.")
        print(f"Here is your {order} ☕ Enjoy!")
        return True

    elif customer_money < drink_cost:
        print("You gave insufficient amount.")
        return False

    else:
        profit+=drink_cost
        print(f"Here is your {order} ☕ Enjoy!")
        return True

order_continue=True
while order_continue:
    order= input("What would you like? (espresso/latte/cappuccino): ")
    if order=="off":
        print("Thank you 😊.")
        order_continue= False

    elif order=="report":
        for _ in resources:
            print(f"{_} : {resources[_]}")
    else:
        drink= MENU[order]
        if resource_available(drink["ingredients"]):
            cost = drink["cost"]
            print(f"Cost for {order} is : {cost} ")
            customer_money=process_coins()
            if transaction_successful(customer_money, drink["cost"]):
                for item in drink["ingredients"]:
                    resources[item] =resources[item]- drink["ingredients"][item]









