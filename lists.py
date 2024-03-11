# Searching for an element in the list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# search using in operator
target = 50
if target in my_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

#  Search using linear search
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1
print(linear_search(my_list, target))

# List operaitons and functions
mLIST = list()
while (True):
    inp = input('Enter a number')
    if inp == 'done': break
    value = float(inp)
    mLIST.append(value)
average = sum(mLIST) / len(mLIST)
print('Average:', average)

# Conditional List comprehension
prev_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = [i*2 for i in prev_list]
print(prev_list)
print(new_list)

language = 'python'
new_language = [letter for letter in language]
print(new_language)

a=[1,2,3,4,5,6,7,8,9]
print(a[::2])

a=[1,2,3,4,5]
print(a[3:0:-1])

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6): 
    print(arr[i], end = " ")
