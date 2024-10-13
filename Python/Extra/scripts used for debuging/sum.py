# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

def sum_of_list():
    import pdb
    pdb.set_trace()
    total_sum = 0
    for val in numbers:
        total_sum += val

    return total_sum

sum_val = sum_of_list()
print("The sum is", sum_val)
