def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    """Add a new item to the shopping list."""
    item = input("Enter item name: ").strip()
    if item:  # Check if item is not empty
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("No item name entered. Nothing was added.")

def remove_item(shopping_list):
    """Remove an item from the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
        return
        
    item = input("Enter item name to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' was not found in your shopping list.")

def view_list(shopping_list):
    """Display all items in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("\nThank you for using Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()