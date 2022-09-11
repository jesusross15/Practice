"""Write a program that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates."""

# let's solve this using a function first a for loop
def dupe1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

#this one is a function using sets
def dupe2(x):
    return list(set(x))

a = [1,2,2,2,4,5,5,6,7,8,8,8,8,8,9]
print(a)

print(dupe1(a))
print(dupe2(a))

# way to use the set method I used the official python documentation for that