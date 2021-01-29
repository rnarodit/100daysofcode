from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffeeMachine= CoffeeMaker ()
money = MoneyMachine()

coffee_item =input (f"what would you like {menu.get_items()}")
while(not coffee_item == "off"):
    if (not coffee_item == "off"):
        if(coffee_item == "report"):
            coffeeMachine.report()
            money.report()
        else:
            chosenItem = menu.find_drink (coffee_item)
            if (coffeeMachine.is_resource_sufficient(chosenItem)):
                if (money.make_payment(chosenItem.cost)):
                    coffeeMachine.make_coffee (chosenItem)
        coffee_item =input (f"what would you like {menu.get_items()}")
            