# Create a new empty list named shopping_list
shopping_list = []

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for help.
Enter 'SHOW' to display your current list.
""")

# Create a function named add_to_list that declares a parameter named item
def add_to_list(item):
    # Add the item to the list
    shopping_list.append(item)
    # Notify user that the item was added, and stat the number of items in the list currently
    print("Added! List has {} items.").format(len(shopping_list))

# Define a function named show_list that prints all the items in the List
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()
while TRUE:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    #Call add_to_list with new_item as an argument
    add_to_list(new_item)

show_list()
