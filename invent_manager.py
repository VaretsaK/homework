import time


def add_store_item():
    item_name = input("Item name: ").capitalize()
    item_description = input("Item description: ")
    try:
        item_quantity = int(input("Item quantity: "))
        store_items[item_name] = {"description": item_description, "items": item_quantity}
    except ValueError as error:
        print(error)


def view_store_items():
    for name, descr in store_items.items():
        print(f"{name:^10}: {descr['description']:>20} - {descr['items']} item(s)")


def remove_store_item():
    view_store_items()
    item_to_remove = input("What item do you want to remove? ")
    try:
        store_items.pop(item_to_remove)
    except KeyError:
        print("Wrong item!")


def update_store_item():
    view_store_items()
    item_to_update = input("What item do you want to update? ")
    try:
        new_quantity = int(input("Enter the new quantity: "))
        store_items[item_to_update]["items"] = new_quantity
    except (KeyError, ValueError) as errors:
        print(f"{errors} Try again!")


def search_inventory():
    search_request = input("Enter a search term (either an item name or description): ")
    for name, descr in store_items.items():
        if search_request == name or search_request in descr["description"]:
            print(f"{name:^10}: {descr['description']:>20} - {descr['items']} item(s)")


if __name__ == "__main__":
    store_items = {}
    while True:
        menu_choice = input("""
        Store inventory system... 
        The menu: 
        - View the current inventory
        - Add items to the inventory
        - Remove items from the inventory
        - Update the quantity of items in the inventory
        - Search for items in the inventory
        - Quit the program
        >>> """)
        try:
            choice = menu_choice[0].lower()
        except IndexError:
            print("Wrong input.\n- Add items to the inventory ")
            choice = "a"
        finally:
            print("Loading...")
            time.sleep(2)

        if choice == "v":
            view_store_items()
            time.sleep(5)
        elif choice == "a":
            add_store_item()
        elif choice == "r":
            remove_store_item()
        elif choice == "u":
            update_store_item()
        elif choice == "s":
            search_inventory()
        elif choice == "q":
            break
