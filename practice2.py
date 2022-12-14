# Python program to interchange first and last elements in a list
"""Given a list, write a Python prgoram to swap first and last element of the list."""
print("First approach:")
# Approach 1: find the length of the list and swap the firt element w the (n-1)th (last) element
list = [1, 42, 2, 9, 15, 17, 21]
# function for swap
def swap(list):
    size = len(list)
    
    #swapping
    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp
    
    return list

# testing list
print("This is the original list: " + str([1, 42, 2, 9, 15, 17, 21]))
print("This is the swapped list: " + str(swap(list)))

print("\nSecond approach:")
#approach #2
# if we refer to the last element of the list as list[-1] we can simply swap index [0] w index [-1]
new_list = [19, 42, 16, 18, 22, 89]
# swap function
def swap_list(new_list):
    
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list

#testing code
print("This is the original list: " + str([19, 42, 16, 18, 22, 89]))
print("This is the swapped list: " + str(swap_list(new_list)))

    