# function that accept no arguments and returns nothing
def hello ():
    print("Hello user!")

# function that acceept 3 arguments and returns a single list with 3 arguments inside
def pack(x, y, z):
    return[x,y,z]

# function accept a list of any length, and print out a series of strings that say 
# "First I eat___" (the first element of the list), and "Next I eat___" (for the following elements in the list)
# if list is empty print "My lunchbox is empty"

# my_list is an object? 
def lunch(my_lst):
# len function returns the number of items in an object
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
# the for loop is looping through the number of items(len)
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
print(pack("a","b","c"))
print(pack(1,2,3))
lunch([])
lunch(["sandwich"])
lunch(["apple","banana","sandwich","cookie"])