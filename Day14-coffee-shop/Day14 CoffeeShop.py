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
    "water": 400,
    "milk": 400,
    "coffee": 400,
}

money_box = 0.0





# input_string = input('What would you like?(espresso/latte/cappuccino)')
def machine_interface():
    global money_box
    # TODO 1 Prompt question
    input_string = input('What would you like?(espresso/latte/cappuccino)')

    # TODO 2 Turn off the machine -done
    if input_string == 'off':
        exit()
    elif input_string == 'report':
        # TODO 3 Print report
        print(f"""
Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: {money_box}
                """)


    # elif input_string == 'espresso' or 'latte' or 'cappuccino':
    # GPT是建议用下面这种写法，否则，无论输入是什么，都会进入这个分支
    elif input_string in ['espresso', 'latte', 'cappuccino']:
        if check_sufficient(input_string):
            if process_coins(input_string):
                money_box += MENU[input_string]['cost']
                make_coffee(input_string)



    machine_interface()

def check_sufficient(input_string):
    # TODO 4 Check resources sufficient
    sufficient_count = 0
    for ingredient, amount in MENU[input_string]['ingredients'].items():
        if resources.get(ingredient,0) < amount:
            sufficient_count += 1
            print(f'Sorry there is no enough {ingredient}')

    if sufficient_count == 0:
        return True
    else:
        return False

# TODO 5 Process Coins
def process_coins(input_string):
    print(f'Please input money\n'
          f'The price of {input_string} is {MENU[input_string]['cost']}.')
    quarters = float(input('Insert quarters: '))
    dimes = float(input('Insert dimes: '))
    nickles = float(input('Insert nickles: '))
    pennies = float(input('Insert pennies: '))

    coins = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01

    if coins >= MENU[input_string]['cost']:
        print(f"Here's the change ${{:0.2f}}".format(coins - MENU[input_string]['cost']))
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(input_string):

    for ingredient, amount in MENU[input_string]['ingredients'].items():
        global resources
        resources[ingredient] -= amount
    print('Here is your latte. Enjoy!')

machine_interface()



















# TODO 7 Make coffee





