#user interface to the main menu
import data
import functions
customer_order_list = []
def show_main_menu():
  while True:
    print("Elliot's diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('C to change an order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      if customer_order_list:
                functions.print_check(customer_order_list)
                customer_order_list.clear()
                print("Order list reset.")
      else:
        print("No orders to print.")
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders
      # User menu choice processing
    elif user_menu_choice in 'Cc':
        change_order()
    else:
        print("You did not enter a valid input, Try again")
  

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  item_price = (functions.get_item_information(item_code)).split()[1]
  customer_order_list.append((item_code,int(quantity)))
  print(f"Added {quantity} of {item_code} at ${item_price} each to your order.")

def change_order():
  """Allows the user to change their order by removing or updating items."""
  if not customer_order_list:
      print("No items to change.")
      return

  print("\nCurrent order:")
  for i, (item, qty) in enumerate(customer_order_list):
      print(f"{i + 1}. {item}: x{qty}")
  
  index = int(input("Enter the number of the item you want to change: ")) - 1
  new_qty = int(input("Enter new quantity (0 to remove): "))

  if new_qty == 0:
      removed_item = customer_order_list.pop(index)
      print(f"Removed {removed_item[0]} from the order.")
  else:
      customer_order_list[index] = (customer_order_list[index][0], new_qty)
      print(f"Updated {customer_order_list[index][0]} to quantity {new_qty}.")

  





if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


