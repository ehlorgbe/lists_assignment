#user interface to the main menu
import data
import functions
customer_order_list = []
def show_main_menu():
  while True:
    print("Elliot's diner") #edit to show your name
    print("__________")
    print('N for a new order')
    print('X for close orders and print the check')
    print('Q for quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      print('This option prints the list of items ordered, extended price, total, Taxes, and Grand total ')
    elif user_menu_choice in 'Nn':
      print('New order')
      make_order(user_menu_choice.upper())  #calls a function for adding to the orders
      # User menu choice processing
      choice = input("Type 'A' to add another item, 'R' to remove an item").upper()
      if user_menu_choice in ['D1','D2','D3','D4'] :
          if choice.upper() == 'A':
              functions.add_item_to_order(customer_order_list,data.menu_items, data.drink_items)
          elif choice.upper() == 'R':
              functions.remove_item_from_order(customer_order_list)

      elif user_menu_choice in ['A1','A2','A3','A4','A5']:
          if choice.upper() == 'A':
              add_item_to_order(appetizer_order_list, appetizer_items, "Appetizers")
          elif choice.upper() == 'R':
              remove_item_from_order(appetizer_order_list, "Appetizers")

      elif user_menu_choice == 'E':
          if choice.upper() == 'A':
              add_item_to_order(entree_order_list, entree_items, "Entrees")
          elif choice.upper() == 'R':
              remove_item_from_order(entree_order_list, "Entrees")

      elif user_menu_choice == 'S':
          if choice.upper() == 'A':
              add_item_to_order(salad_order_list, salad_items, "Salads")
          elif choice.upper() == 'R':
              remove_item_from_order(salad_order_list, "Salads")

      elif user_menu_choice == 'T':
          if choice.upper() == 'A':
              add_item_to_order(dessert_order_list, dessert_items, "Desserts")
          elif choice.upper() == 'R':
              remove_item_from_order(dessert_order_list, "Desserts")

  # customer_order.append([functions.get_item_information(item_code),quantity])
  

def close_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  print("")

def make_order(menu_choice):
  print('Functionality for menu choice ', menu_choice)
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  print(functions.get_item_information(item_code))
  






if __name__ == '__main__':
    #initialize the lists
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    #print(functions.get_item_information('D1'))
    show_main_menu()


