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
    "money": 0
}

def out_resource():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk.: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: ${resources["money"]}")

while True:
    choice = input("What would you like? (espresso/latte/cappuchino):")
    if choice == "report":
        out_resource()
        continue
    if choice == "off":
        break
    sufficient = True
    choice_dic = MENU[choice]["ingredients"]
    for each in choice_dic:
        if choice_dic[each] > resources[each]:
            print(f"Sorry there us not enough {each}")
            sufficient = False
    if sufficient == False:
        continue
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if amount < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        continue
    for each in choice_dic:
        resources[each] -= choice_dic[each]
    resources["money"] += MENU[choice]["cost"]
    print(f"Here is ${round(amount - MENU[choice]["cost"], 2)} dollars in change.")
    print(f"Here is your {choice}. Enjoy!")

