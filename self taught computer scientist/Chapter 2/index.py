# Print the numbers from 1 to 10 recursively

# iterative approach
def print_nums_iter(min, max):
    num = min
    while num <= max:
        print(num)
        num += 1


# print_nums_iter(1, 10)

# recursive approach
def print_nums_recur(min, max):
    if max == min:
        print(min)
        return min
    num = 1 + print_nums_recur(min, max - 1)
    print(num)
    return num


print_nums_recur(1, 10)
