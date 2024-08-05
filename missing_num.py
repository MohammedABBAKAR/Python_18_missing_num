# Find the Missing Number

# Create a function that takes a list of numbers between 1 and 10
# (excluding one number) and returns the missing number.
# Examples

# missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5

# missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

# missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) ➞ 7


def missing_num(lst):
    lstnum =[1,2,3,4,5,6,7,8,9,10]
    for i in lstnum:
        if i not in lst:
         return i
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))


# *********************************************************


def missing_num(lst):
    lstnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # List of all numbers from 1 to 10
    for i in lstnum:  # Iterate through each number in lstnum
        if i not in lst:  # If the number is not in the given list
            return i  # Return the missing number

# Example
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))  # Output: 7


# *********************************************************


def missing_num(lst):
    # Sum of numbers from 1 to 10
    total_sum = sum(range(1, 11))
    # Sum of numbers in the list
    list_sum = sum(lst)
    # The missing number is the difference
    missing_number = total_sum - list_sum
    return missing_number

# Examples
print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # ➞ 5
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))  # ➞ 10
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))

# *********************************************************