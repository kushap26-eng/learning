class ATM:
    def __init__(self,account_holder,bank_name,initial_balance,pin):
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.__balance = initial_balance
        self.__pin = pin
        self.__failed_aatempts = 0
        self.__is_locked = False

    def __verify_pin(self,entered_pin):
        if self.__is_locked:
            print("Secirity Alert: The account is locked due to multiple incorrect PIN attempts.")
            return False
        if self.__pin == entered_pin:
            self.__failed_aatempts = 0
            return True

        self.__failed_aatempts += 1
        print(f"Incorrect PIN. ({3- self.__failed_attempts} attempts remaining.)")
        if self.__failed_aatempts >= 3:
            self.__is_locked = True
            print("Account has been locked. Please contact support")
            return False

    def display_welcome_message(self):
        print(f"{'='*40}")
        print(f"Welcome to {self.bank_name}")
        print(f"Cardholder: {self.account_holder}")
        print(f"{'='*40}")

    def check_balance(self,entered_pin:int):
        if self.__verify_pin(entered_pin):
            print(f"Current Available Balance: ₹{self.__balance:,.2f}")
        else:
            print("Transaction Denied.")

    def deposit(self,enetered_pin: int,amount: float):
        if not self.__verify_pin(enetered_pin):
            print("Transaction Denied.")
            return

        if amount <= 0:
            print("Error: Deposit amount must be positive.")


        self.__balance += amount
        print(f"Success: Deposited ₹(amount:.2f)")   
        print(f"New Balance: ₹(self,__balance:.2f)")

    def withdraw(self,entered_pin,amount):
            if not self.__verify_pin(entered_pin):
                print("Transaction Denied")
                return

            if amount <= 0:
                print("Error: Withdrawl amount must be positive.")
                return

            if amount > self.__balance:
                print(f"Success: Dispensing ₹{amount: .2f}")
                print(f"Remaining Balance: ₹{self.__balance:.2f}")

    def update_pin(self,old_pin,new_pin):
            if not self.__verify_pin(old_pin):
                print("Security Alert: Cannot change PIN without verification.")
                return

            if len(str(new_pin)) != 4:
                print("Error: New PIN must be a 4-digit number.")
                return

            self.__pin = new_pin
            print("Success: Your security PIN has been updated.")

    def run_atm_application():
        user_atm = ATM("Kushangi Madhu","State Bank of India",25000.50,2600)

        while True:
            user_atm.display_welcome_message()
            print("1.Check Balance")
            print("2.Deposit Funds")
            print("3.Withdraw Cash")
            print("4.Updated Security PIN")
            print("5.Exit System")

            choice_input = input("Select an optiom (1-5):")
            if not choice_input.isdigit():
                print("Invalid Input: Please type a number.")
                continue

            choice = int(choice_input)
            if choice == 5:
                print("Thank you for banking with State Bank of India. Goodbye!")

            if choice >= 1 and choice <= 4:
                pin_string = input("Enter your 4-digit PIN: ")
                if not pin_string.isdigit():
                    print("Security Error: PIN must be numbers only.")
                    continue

                pin_input = int(pin_string)

                if choice == 1:
                    user_atm.check_balance(pin_input)

                elif choice == 2:
                    amount_string = input("Enter deposit amount(₹):")
                    if not amount_string.replace('.','',1).isdigit():
                        print("Error: Invalid currency formatting.")
                        continue

                    user_atm.deposit(pin_input,float(amount_string))

                elif choice == 3:
                    amount_string = input("Wnter withdrawl amount(₹):")
                    if not amount_string.replace('.','',1).isdigit():
                        print("Error: Invalid currency formatting.")
                        continue
                    user_atm.withdraw(pin_input,float(amount_string))

                elif choice == 4:
                    new_pin_string = input("Enter new 4-digit PIN:")
                    if not new_pin_string.isdigit():
                        print("Error: Invalid currency formatting.")
                        continue

                    user_atm.update_pin(pin_input,int(new_pin_string))
                else:
                    print("Error: Out of bounds choice selection. Choose 1 through 5.")

                input("Press Enter to return to main menu...")

    if __name__ == "__main__":
        run_atm_application() 