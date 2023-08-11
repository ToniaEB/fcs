def ex1(s, i):
  new_string = ""
  n = len(s)
  if i == 0:
    return new_string
  for j in range(i):
    for char in range(n):
      new_string = s[char] + new_string
  return new_string


ex1("hello", 2)


def ex2(s):
  upper_string = ""
  lower_string = ""
  final_string = ""
  n = len(s)
  for i in range(n):
    if s[i].islower():
      lower_string += s[i]
    else:
      upper_string += s[i]
  final_string = upper_string + lower_string
  return final_string


ex2("HelloWorld")


def ex3(s1, s2):
  new_s2 = sorted(s2)
  if len(s1) == len(s2):
    for i in range(len(s1)):
      if s1[i] != new_s2[i]:
        return False
    return True
  else:
    return False


ex3("abcde", "edacb")
ex3("aabc", "edabc")


def ex4(L):
  max = L[0]
  max_i = 0
  for i in range(1, len(L)):
    if max < L[i]:
      max = L[i]
      max_i = i
  print(f"the highest value in the list is {max} at index {max_i}")


L = [5, 6, 3, 2, 7, 2, 0, 1, 6]
ex4(L)


def ex4_BONUS(L):
  min = L[0]
  min_i = 0
  for i in range(1, len(L)):
    if min > L[i]:
      min = L[i]
      min_i = i
  print(f"the lowest value in the list is {min} at index {min_i}")


L = [5, 6, 3, 2, 7, 2, 0, 1, 6]
ex4_BONUS(L)


def ex5(n):
  a = str(n)
  count = 0
  for i in range(len(a)):
    count += 1
  return count


ex5(123)
ex5(10000)


def list_jumps(jumps):
  index = 0
  n = len(jumps)
  visited = set()

  while 0 <= index < n:
    if index in visited:
      return "cycle"

    visited.add(index)
    next_index = index + jumps[index]

    if next_index < 0 or next_index >= n:
      return "out-of-bounds"

    index = next_index

    # Additional check for a special case where the jump takes you back to the same index
    if jumps[index] == 0:
      return "cycle"

  return "out-of-bounds"


jumps = [2, -1, 1, -2]
jumps = [2, -1, 2, -1]
list_jumps(jumps)


def add_item(items, barcode, name, price):
  items[barcode] = {"name": name, "price": price}


def start_receipt(items):
  while True:
    new_receipt = input("Start a new receipt? (yes/no): ").lower()
    if new_receipt == 'no':
      print("Exiting POS system.")
      break
    elif new_receipt == 'yes':
      process_receipt(items)


def process_receipt(items):
  receipt_items = []
  total_amount = 0

  while True:
    barcode = input("Enter item barcode: ")
    if barcode not in items:
      print("Item not found.")
      continue

    quantity = int(input("Enter quantity purchased: "))
    item = items[barcode]
    total_cost = item["price"] * quantity

    receipt_items.append((item["name"], quantity, total_cost))
    total_amount += total_cost

    add_another = input("Add another item? (yes/no): ").lower()
    if add_another == 'no':
      print_receipt(receipt_items, total_amount)
      break


def print_receipt(items, total_amount):
  print("\nReceipt:")
  for item_name, quantity, item_total in items:
    print(f"{item_name} - Quantity: {quantity}, Total Cost:{item_total}")
  print("Total Amount:", total_amount)
  print("\nReceipt printed.\n")


# Dictionary to store items by barcode
items = {}

# Adding items to the system
add_item(items, "123", "Item 1", 5.99)
add_item(items, "456", "Item 2", 2.49)
add_item(items, "789", "Item 3", 10.99)

# Starting the POS system
start_receipt(items)
