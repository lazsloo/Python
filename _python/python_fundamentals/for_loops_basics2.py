# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".

# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(new_list):
    for i in range(len(new_list)):
        if new_list[i] > 0:
            new_list[i] = "big"
    return new_list
print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(lst):
    count = 0
    for val in lst:
        if val > 0:
            count += 1
    lst[len(lst) - 1] = count
    return lst
print(count_positives([-1, 1, 1, 1]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.

# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(a):
    total = 0
    for i in range(len(a)):
        total = total + a[i]
    return total
print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))

# Average - Create a function that takes a list and returns the average of all the values.

# Example: average([1,2,3,4]) should return 2.5

def average(a):
    total = 0
    for i in range(len(a)):
        total = total + a[i]
    return total / len(a)
print(average([1, 2, 3, 4]))

# Create a function that takes a list and returns the length of the list.

# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(a):
    count = 0
    for i in a:
        count += 1
    return count
print(length([1, 2, 3, 4]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.

# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(a):
    if len(a) == 0:
        return False
    current_min = a[0]
    for i in a:
        if i < current_min:
            current_min = i
    return current_min
print(minimum([37, 2, 1, -9, 2, 1]))
print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.

# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maxium(a):
    if len(a) == 0:
        return False
    current_max = a[0]
    for i in a:
        if i > current_max:
            current_max = i
    return current_max
print(maxium([2, 1, 3, 14, 22, 31, 1, 26, 199, 11]))
print(maxium([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.

# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(lst):
    result = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return result
    else:
        result['sum_total'] = 0
        result['maximum'] = lst[0]
        result['minimum'] = lst[0]
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1
    result['average'] = result['sum_total'] / len(lst)

    return result

print(ultimate_analysis([37, 2, 1, -9]))
print(ultimate_analysis([]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)

# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

print(reverse_list([37, 2, 1, -9]))