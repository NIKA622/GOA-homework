print("===== Welcome to group 2 Bank =====")

name = input("Enter your name to create an account: ")
pin = input("Create a 4-digit PIN: ")
balance = 0
history = ""  

print("Account created for", name)
print("PIN set to:", pin)
print("Your starting balance is", balance)

login_name = input("Enter your name to log in: ")

if login_name == name:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == pin:
        print("Login successful! Welcome,", name)

        running = "yes"

        while running == "yes":
            print("\n--- MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Take a Loan")
            print("6. View Account Details")
            print("7. Exit")

            choice = input("Choose an option (1-7): ")

            if choice == "1":
                print("Your balance is", balance)

            else:
                if choice == "2":
                    amount = int(input("Enter amount to deposit: "))
                    if amount > 0:
                        balance = balance + amount
                        history = history + "Deposited " + str(amount) + "\n"
                        print("Deposit successful! New balance:", balance)
                    else:
                        print("Invalid amount.")

                else:
                    if choice == "3":
                        amount = int(input("Enter amount to withdraw: "))
                        if amount > balance:
                            print("Not enough money!")
                        else:
                            if amount > 0:
                                balance = balance - amount
                                history = history + "Withdrew " + str(amount) + "\n"
                                print("Withdrawal successful! New balance:", balance)
                            else:
                                print("Invalid amount.")

                    else:
                        if choice == "4":
                            if history == "":
                                print("No transactions yet.")
                            else:
                                print("--- Transaction History ---")
                                print(history)

                        else:
                            if choice == "5":
                                loan = int(input("Enter loan amount: "))
                                if loan > 0:
                                    balance = balance + loan
                                    history = history + "Loan taken: " + str(loan) + "\n"
                                    print("Loan approved! New balance:", balance)
                                else:
                                    print("Invalid loan amount.")

                            else:
                                if choice == "6":
                                    print("--- Account Details ---")
                                    print("Name:", name)
                                    print("PIN:", pin)
                                    print("Balance:", balance)
                                    if history == "":
                                        print("No transactions yet.")
                                    else:
                                        print("Recent activity:\n" + history)

                                else:
                                    if choice == "7":
                                        print("Goodbye", name)
                                        running = "no"
                                    else:
                                        print("Invalid choice. Please try again.")

    else:
        print("Wrong PIN! Access Denied.")

else:
    print("Name not found!")
