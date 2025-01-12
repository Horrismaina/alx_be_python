shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                item = input("Enter item name: ")
                shopping_list.append(item)
                print(f"{item} has been added to the list.")
            elif choice == '2':
                item = input("Enter item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"{item} has been removed from the list.")
                else:
                    print(f"{item} is not in the list.")
            elif choice == '3':
                if shopping_list:
                    print("\nCurrent shopping list:")
                    for item in shopping_list:
                        print(item)
                else:
                    print("The shopping list is empty.")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()