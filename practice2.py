# Python program to interchange first and last elements in a list
"""Given a list, write a Python prgoram to swap first and last element of the list."""

# function for swap
def swap_list(new_list):
    size = len(new_list)
    
    #swapping
    temp = new_list[0]
    new_list[0] = new_list[size - 1]
    new_list[size - 1] = temp
    
    return new_list

# testing list
new_list = [1, 42, 2, 9, 15, 17, 21]

print(swap_list(new_list))


    