import os


file_path = os.path.expanduser("~/Desktop/Groceryproject/groceryitems.txt")

def load_items():
    items = []
    with open(file_path, "r") as f:
        for line in f:
            name, price, quantity = line.strip().split(",")
            items.append({
                "name": name,
                "price": float(price),
                "quantity": int(quantity)
            })
    return items

def save_items(items):
    with open(file_path, "w") as f:
        for item in items:
            f.write(f"{item['name']},{item['price']},{item['quantity']}\n")

def display_table(items):
    print("\nAvailable Products:")
    print("{:<5} {:<15} {:<10} {:<10}".format("No.", "Item", "Price(Rs)", "Stock"))
    print("-" * 45)
    for i, item in enumerate(items, 1):
        print("{:<5} {:<15} {:<10} {:<10}".format(i, item['name'], item['price'], item['quantity']))
    print("-" * 45)

def shopping():
    cart = []
    items = load_items()

    while True:
        display_table(items)

        choice = input("Enter the item number to buy (or 'q' to quit): ")
        if choice.lower() == 'q':
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(items):
                selected = items[index]
                print(f"You selected: {selected['name']} (Stock: {selected['quantity']})")

                qty = int(input("Enter quantity to buy: "))
                if 0 < qty <= selected['quantity']:
                    cart.append({
                        "name": selected['name'],
                        "price": selected['price'],
                        "quantity": qty,
                        "total": qty * selected['price']
                    })
                    items[index]['quantity'] -= qty
                    print("Item added to cart.")
                else:
                    print("Invalid quantity.")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a valid number.")

        cont = input("Do you want to buy another product? (y/n): ")
        if cont.lower() != 'y':
            break

    if cart:
        print("\n========= FINAL BILL =========")
        total_amount = 0
        for i, item in enumerate(cart, 1):
            print(f"{i}. {item['name']} - {item['quantity']} x {item['price']} = Rs.{item['total']}")
            total_amount += item['total']
        print(f"Total Amount: Rs.{total_amount}")
        print("===============================")

        save_items(items)
        print("Stock updated in file.")
    else:
        print("No items purchased.")

if __name__ == "__main__":
    shopping()
