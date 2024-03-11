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