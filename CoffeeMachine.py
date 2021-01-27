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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1. taking order from customer. Giving 3 options and using resources.

order_continue=True
while order_continue:
    order= input("What would you like? (espresso/latte/cappuccino): ")
    if order=="report":
        for _ in resources:
            print(f"{_} : {resources[_]}")
    else:
        coffee_order = True
        while coffee_order:
            cost = MENU[order]["cost"]
            print(f"Cost for {order} is : {cost} ")
            coins = input("Please insert coins.")
            # converting coins into dollar after taking input
            quarters = int(input("How many quarters?")) / 4
            dimes = int(input("How many dimes?")) / 10
            nickles = int(input("How many nickles?")) / 20
            pennies = int(input("How many pennies?")) / 100
            customer_money = (quarters + dimes + nickles + pennies)

            if customer_money > MENU[order]["cost"]:
                return_money = round(customer_money - MENU[order]["cost"], 2)
                print(f"Here is {return_money} in change.")
                print(f"Here is your {order} ☕ Enjoy!")
                coffee_order = False

            elif customer_money < MENU[order]["cost"]:
                print("You gave insufficient amount.")

            else:
                print(f"Here is your {order} ☕ Enjoy!")
                coffee_order = True

            for _ in resources:
                for key in MENU[order]["ingredients"]:
                    if _ == key:
                        resources[_]=resources[_]-MENU[order]["ingredients"][key]
                print(f"{_} : {resources[_]}")









