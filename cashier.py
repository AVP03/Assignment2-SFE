class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        dollars = int(input("how many dollars?: ")) * 1
        half_dollars = int(input("how many half dollars?: ")) * 0.5
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return half_dollars + dollars + quarters + nickels

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print("Transaction successful")
            change = (coins - cost)
            print(f"Here is your change: ${change:.2f}")
            return True
        else:
            print("Transaction failed: Insufficient funds")
            return False
