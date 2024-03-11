import numpy as np

twoDArray = np.array([[11, 15, 12, 5], [12, 15, 12, 5], [12, 15, 13, 20], [12,17, 20, 18]])
print(twoDArray)

newTwoDArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

newTwoDArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newTwoDArray)

# Accessing an element in two dimensional arrays
def accessElements(array, rawIndex, colIndex):
    if rawIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrrect index')
    else:
        print(array[rawIndex][colIndex])
accessElements(twoDArray, 2, 3)

# Traversing two dimentional arrays
def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
traverseTDArray(twoDArray)

# Search elements in an array using Linear search method
def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:           
                return 'The value is located at index'+str(i)+" "+str(j)
    return 'The value is not found'

print(searchTDArray(twoDArray, 15))

# deleting raws and columns from the array
newTDAraay = np.delete(twoDArray, 1, axis=1)
print(newTDAraay)