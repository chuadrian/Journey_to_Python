def main():
    goods = {}  # Initialize an empty dictionary to store goods and their quantities

    while True:
        print("\nOptions:")
        print("1. Add/Update a product")
        print("2. Remove a product")
        print("3. List all products")
        print("4. Modify quantity")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter the name of the product: ")
            quantity_str = input(f"Enter the quantity of {name}: ")
            try:
                quantity = int(quantity_str)
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")
                continue

            goods[name] = quantity
            print(f"{name} updated with a quantity of {quantity}")

        elif choice == '2':
            name = input("Enter the name of the product to remove: ")
            if name in goods:
                del goods[name]
                print(f"{name} removed from the list.")
            else:
                print(f"{name} not found in the list.")

        elif choice == '3':
            print("\nList of Goods and Quantities:")
            for name, quantity in goods.items():
                print(f"{name}: {quantity}")

        elif choice == '4':
            name = input("Enter the name of the product to modify: ")
            if name in goods:
                quantity_str = input(f"Enter the amount to add/subtract from {name}: ")
                try:
                    quantity_change = int(quantity_str)
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
                    continue

                goods[name] += quantity_change
                print(f"{name} quantity modified. New quantity: {goods[name]}")

            else:
                print(f"{name} not found in the list.")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()

