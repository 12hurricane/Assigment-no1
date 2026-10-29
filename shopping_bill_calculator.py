product = {
    "Milk" : 250.0,
    "Bread" : 150.0,
    "Eggs" : 400.0,
    "Rice" : 1200
}
def calculate_billDiscount(total):
    if total >= 5000:
        return total * 0.10
    else:
        return 0.0

total = 0
for item, price in product.items():
    print(f"item : {item}, price : {price}")

cart = {}
while True:
    item = input("Enter item you want to buy (or type 'done' to finish): ")
    if item == 'done':
        break
    if item in product:
        quantity = int(input(f"Enter quantity for {item}: "))
        cart[item] = cart.get(item, 0) + quantity
    else:
        print("Item not found in the product list.")
