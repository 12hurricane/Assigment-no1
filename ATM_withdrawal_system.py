acount={
    "name" : "Ali",
    "password" : "1234",
    "balance" : 10000
}
def withdraw(amount,balance):
    if amount <= balance:
        balance -= amount
        print("withdrawal successful.")
    else:
        print("insufficient balance>")
    return balance
attempt = 0
while attempt < 3:
    pin = (input("Enter your pin:"))
    if pin == acount["password"]:
        print(f"welcome,{acount['name']}")
        amount = float(input("Enter amount to withdraw:"))
        if amount > 0:
            acount["balance"] = withdraw(acount["balance"],amount)
            print(f"Remaining balance: {acount['balance']}")
        else:
            print("Invalid amount entered.")
            login_succeful = True
            break
    else:
        attempt += 1
        print(f"Incorrect pin. You have {3 - attempt} attempts left.")


if not login_succeful:
    print("Card blocked due to too many incorrect attempts.")