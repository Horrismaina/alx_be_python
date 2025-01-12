shopping_list = []  # Defined at module level as required

def display_menu():
    """Display the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    return input("Enter your choice (1-4): ").strip()  # Return the choice

def add_item():
    """Add a new item to the shopping list."""
    item = input("Enter item name: ").strip()
    if item:  # Check if item is not empty
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("No item name entered. Nothing was added.")

def remove_item():
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

def view_list():
    """Display all items in the shopping list."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour Shopping List:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")

def main():
    while True:
        choice = display_menu()  # Get the choice from display_menu
        
        try:
            choice_num = int(choice)  # Convert choice to integer
            
            if choice_num == 1:
                add_item()
            elif choice_num == 2:
                remove_item()
            elif choice_num == 3:
                view_list()
            elif choice_num == 4:
                print("\nThank you for using Shopping List Manager. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()