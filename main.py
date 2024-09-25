import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)  
cashier_instance = Cashier()  

def main():
    while True: 
        order = input("What would you like? (small/ medium/ large/ off/ report): ")
        if order == "off":
            print("Turning off the machine...")
            break
        elif order == "report":
            print(sandwich_maker_instance.resources) 
        elif order in recipes:
            sandwich = recipes[order]  
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                inserted_coins = cashier_instance.process_coins()  
                if cashier_instance.transaction_result(inserted_coins, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(order, sandwich["ingredients"]) 
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()
