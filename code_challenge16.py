class BankAccount:
    def __init__(me, your_name, initial_deposit):
        me.name = your_name
        me.balance = initial_deposit

    def deposit(me, amount):
        me.balance += amount
        print(f"Deposited {amount}. Balance: {me.balance}")
        me.breakdown_denomination(amount)

    def withdraw(me, amount):
        if amount > me.balance:
            print("Insufficient funds.")
        else:
            me.balance -= amount
            print(f"Withdrew {amount}. Balance: {me.balance}")

    def check_balance(me):
        print(f"Balance: {me.balance}")

    def breakdown_denomination(me, amount):
        denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
        print("Denomination breakdown:")
        for denom in denominations:
            count = amount // denom
            if count > 0:
                print(f"{denom} peso: {count} bill(s)")
                amount -= count * denom

def create_account():
    your_name = input("Name: ")
    while True:
        try:
            deposit = float(input("Initial deposit: "))
            return BankAccount(your_name, deposit)
        except ValueError:
            print("Invalid input. Please enter a valid number for the deposit.")

def main():
    account = None
    while True:
        print("\n1. Create account\n2. Deposit\n3. Withdraw\n4. Balance\n5. Exit")
        choice = input("Choice: ")

        if choice == "1" and not account:
            account = create_account()
        elif choice == "2" and account:
            while True:
                try:
                    amount = float(input("Deposit amount: "))
                    account.deposit(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the deposit amount.")
        elif choice == "3" and account:
            while True:
                try:
                    amount = float(input("Withdraw amount: "))
                    account.withdraw(amount)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for the withdrawal amount.")
        elif choice == "4" and account:
            account.check_balance()
        elif choice == "5":
            print("That's all, thank you!")
            break
        else:
            print("Invalid choice or account not created.")

if __name__ == "__main__":
    main()