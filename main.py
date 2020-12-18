from cashRegister import CashRegister

a_choices = {
            "1": CashRegister,
            "2": "self.pay",
            "3": "self.retrieve_basket_on_hold",
            "4": "self.on_hold",
            "5": "self.quit"
        }

if __name__ == '__main__':
    print("Start")
    print("POS System \n1. Cash register \n2. Not Implemented \n3. Not Implemented \n4. Not Implemented \n5. Not Implemented")
    s_choice = input("Enter an option: ")
    action = a_choices.get(s_choice)

    if action:
        action = action()
        action.start()
    else:
        print("{0} is not a valid choice".format(s_choice))


