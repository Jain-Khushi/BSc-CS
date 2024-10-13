# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

def calculate_sum():
    total_sum = 0
    for val in numbers:
        total_sum += val

    print_sum(total_sum)

def print_sum(sum_val):
    import pdb
    pdb.set_trace()
    print("The sum is", sum_val)
    

calculate_sum()
