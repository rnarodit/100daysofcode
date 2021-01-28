from data import MENU


def report(resources):
    print(f"Water:{resources['water']}\n Milk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney:{resources['money']}")   


def enoughResources(resources, coffee):
    enoughResources = True
    if (resources["water"] < MENU[coffee]["ingredients"]["water"]):
        print("Sorry, there is not enough water")
        enoughResources = False
    if (not coffee == "espresso"):
        if (resources["milk"] < MENU[coffee]["ingredients"]["milk"]):
            print("Sorry, there is not enough milk")
            enoughResources = False
    if(resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]):
        print("Sorry, there is not enough coffee")
        enoughResources = False
    return enoughResources


quarters = 0
dimes = 0
pennies = 0
nickles = 0
resources = {
    "water": 100,
    "milk": 100,
    "coffee": 100,
    "money": 0
     }
cont = True
while (cont):
    coffee = input("what would you like? (espresso($1.5)/latte($2.5)/cappuccino($3.0))").lower()
    if coffee == "off":
        cont = False
    else:
        if(coffee == "report"):
            report(resources)

        else:
            if(enoughResources(resources, coffee)):
                coffeePrice = MENU[coffee]["cost"]
                quarters = int(input("how many quarters ?")) * 0.25
                dimes = int(input("how many dimes ?")) * 0.10
                nickles = int(input("how many nickles ?")) * 0.05
                pennies = int(input("how many pennies ?")) * 0.01
                total = quarters+dimes+nickles+pennies
                if (total < coffeePrice):
                    print("Sorry that's not enough money, money refunded")
                else:
                    change = total - coffeePrice
                    print(f"here is your {coffee}☕, Enjoy!")
                    print(f"Hear is ${change} in change.")
                    resources["water"] -= MENU[coffee]["ingredients"]["water"]
                    if (not coffee == "espresso"):
                        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
                    resources["money"] += coffeePrice
