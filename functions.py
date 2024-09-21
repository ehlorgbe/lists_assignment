#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  print(item_code)
  for item in data.menu_items:
    item_number, item_name, item_price = item.split(' ')
    if item_number == item_code:
      return [item_name.encode("ascii", "ignore").decode(),int(item_price)]

def display_items():
  """Displays all menu items grouped by category."""
  print('Drinks', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'D'])
  print('Appetizers', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'A'])
  print("Salads: ", [d.replace('\u200b','') for d in data.menu_items if d[0] == 'S'])
  print("Entrees: ", [d.replace('\u200b','') for d in data.menu_items if d[0] == 'E'])
  print("Desserts: ", [d.replace('\u200b','') for d in data.menu_items if d[0] == 'T'])

def get_item_number():
  display_items()
  while True:
    #write code for displaying the other dishes also
    order_item = input('Enter dish number and quantity: ')
    if order_item.split()[0] in data.all_items:
      return order_item
    else:
      print('Invalid dish number.  Please try again')

# def add_item_to_order(order_list, item_category):
#     while True:
#         # Get user input and append to the order
#         item_code = input(f"Enter item code from {item_category}: ")
#         item_name, item_price = get_item_information(item_code)
#         order_list.append(item_name)

#         # Ask if the user wants to add more items
#         another_item = input('Add another item to the list? Y/N: ').upper()
#         if another_item == 'N':
#             break

# def remove_item_from_order(order_list):
#     if len(order_list) != 0:
#         print(f"Current items in your cart {order_list}")
#         item_code = input(f"Enter item code to remove from {order_list}: ").upper()
#         if item_code in order_list:
#             order_list.remove(item_code)
#         else:
#             print(f"{item_code} not found in {order_list} order.")
#     else:
#         print(f"No items in {order_list} order to remove.")

def print_check(order_list):
    """Prints the customer order and calculates total, taxes, and grand total."""
    total = 0
    print("\n--- Check ---")
    for item, qty in order_list:
        item_name, item_price = get_item_information(item)
        extended_price = item_price * qty
        print(f"{item_name} (x{qty}): ${extended_price}")
        total += extended_price
    taxes = total * 0.08 # Asummming a tax rate of 8% 
    grand_total = total + taxes
    print(f"Total: ${total:.2f}")
    print(f"Taxes: ${taxes:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")