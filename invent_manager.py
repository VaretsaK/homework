import time


def add_store_item():
    item_name = input("Item name: ").capitalize()
    item_description = input("Item description: ")
    item_quantity = int(input("Item quantity: "))
    store_items[item_name] = [item_description, item_quantity]


def view_store_items():
    for name, descr in store_items.items():
        print(f"{name:^10}: {descr[0]:>20} - {descr[1]} item(s)")


def remove_store_item():
    view_store_items()
    item_to_remove = input("What item do you want to remove? ")
    store_items.pop(item_to_remove)


def update_store_item():
    view_store_items()
    item_to_update = input("What item do you want to update? ")
    new_quantity = int(input("Enter the new quantity: "))
    store_items[item_to_update][1] = new_quantity


def search_inventory():
    search_request = input("Enter a search term (either an item name or description): ")
    for name, descr in store_items.items():
        if search_request == name or search_request in descr[0]:
            print(f"{name:^10}: {descr[0]:>20} - {descr[1]} item(s)")


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

        if menu_choice[0].lower() == "v":
            view_store_items()
            time.sleep(5)
        elif menu_choice[0].lower() == "a":
            add_store_item()
        elif menu_choice[0].lower() == "r":
            remove_store_item()
        elif menu_choice[0].lower() == "u":
            update_store_item()
        elif menu_choice[0].lower() == "s":
            search_inventory()
        elif menu_choice[0].lower() == "q":
            break
