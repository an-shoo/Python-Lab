def add_item_to_tuple(t, item):
    return t + (item,)

def tuple_length(t):
    return len(t)

def check_item_in_tuple(t, item):
    return item in t

def access_item_in_tuple(t, index):
    return t[index]

my_tuple = (1, 2, 3, 4)

# Adding an item
my_tuple = add_item_to_tuple(my_tuple, 5)
print("Tuple after adding an item:", my_tuple)

# Displaying the length of the tuple
print("Length of the tuple:", tuple_length(my_tuple))

# Checking for an item in the tuple
item_to_check = 3
print(f"Is {item_to_check} in the tuple?", check_item_in_tuple(my_tuple, item_to_check))

# Accessing an item
index_to_access = 2
print(f"Item at index {index_to_access}:", access_item_in_tuple(my_tuple, index_to_access))
