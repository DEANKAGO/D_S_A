# Accessing/ Traversing the list

shoppingList = [ 'milk', 'Cheese', 'Butter' ]


for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    print(shoppingList[i])

# Updating a list
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(myList)
myList[2] = 33
myList[4] = 55
print(myList)

# Inserting in a list
myList.insert(4, 18)
print(myList)

myList.append(89)
print(myList)

newList = [11, 12, 13, 14, 15, 16]
myList.extend(newList)
print(myList)

# Slice/delete from list
# using slice  update
theList = ['a', 'b', 'c', 'd', 'e', 'f']
theList[0:2] = ['x', 'y']
print(theList)

# delete using pop() method
theList.pop(1)
print(theList)

# delete method
del theList[3]
print(theList)

# remove() method
theList.remove('c')
print(theList)