menu = {  
    "Biryani": 350,  
    "Karahi": 1200,  
    "Naan": 50,  
    "Tea": 100  
}  

print("--- Menu ---")
for food, price in menu.items():
    print(f"{food}: Rs. {price}")

def calculate_item_total(price, quantity):  
    return price * quantity  

total = 0  
ordered_items = {}  
while True:  
    item = input("Enter item name or done: ").title()  
  
    if item == "Done":  
        break  
  
     
    if item in menu:
        quantity = int(input(f"Enter quantity for {item}: "))
         
        item_total = calculate_item_total(menu[item], quantity)
        total += item_total
        
        ordered_items[item] = ordered_items.get(item, 0) + quantity
    else:
        print("Item not available in the menu. Please try again.")

print("\n--- Order Summary ---")
print("Ordered Items & Quantities:", ordered_items)
print("Total bill: Rs.", total) 