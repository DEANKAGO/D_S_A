# Calculate average temperature

# numDays = int(input("How many day's temperature?"))
# total = 0
# for i in range(1, numDays+1):
#     nextDay = int(input("Day " + str(i) + "'s high temp:"))
#     total += nextDay
# avg = round(total/numDays, 2)
# print("\nAverage = " + str(avg))

# Find the days above average temperatures
# numDays = int(input("How many days temperature?"))
# total = 0
# temp = []
# for i in range(numDays):
#     nextDay = int(input("Day " + str(i+1) + "'s high temp:"))
#     temp.append(nextDay)
#     total += temp[i]
# avg = round(total/numDays, 2)
# print("\nAverage = " + str(avg))

# above = 0
# for i in temp:
#     if i > avg:
#         above += 1
# print(str(above) + " day(s) above average")

def missing_number(arr, n):
    total = n * (n + 1) /2
    sum_arr = sum(arr)
    missing = total - sum_arr
    return missing
print(missing_number([1, 2, 3, 4, 6], 6))

def max_product(arr):
    max1, max2 = 0,0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(max_product(arr))

# exclude the first and last elements from the list
def middle(lst):
    return lst[1:-1]
list = [1,2,3,4,5,6,7]
print(middle(list))

# calculate the sum of diagonal elements in a 2D list
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i] [i]
    return total

#  Write a function to get first, second best scores from the list
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
def first_second(my_list):
    bst1, bst2 = 0, 0
    for number in my_list:
        if number > bst1:
            bst2 = bst1
            bst1 = number
        elif number > bst2 and number != bst1:
            bst2 = number
            
    return bst1, bst2
print (first_second(myList))

# function to remove duplicates on given integer array/list
def remove_duplicates(arr):
    new_arr = []
    seen = set()
    for i in arr:
        if i not in seen:
            new_arr.append(i)
            seen.add(i)
    return new_arr

my_arr = [1, 1, 2, 2, 3, 4, 5, 6, 7]
print(remove_duplicates(my_arr))

# function to find pair sum in an array
def pair_sum(arr, target_sum):
    pair = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target_sum:
                pair.append(f"{arr[i]}+{arr[j]}")
    return pair

arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def contains_dublicate(nums):
    new_arr = []
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)           
    return False

nums = [1, 2, 3, 2]
print(contains_dublicate(nums))