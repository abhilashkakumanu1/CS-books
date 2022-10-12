from bisect import bisect_left

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = bisect_left(nums, 6)
print(index)

# Binary search
def binary_search(a_list, target):
    index = bisect_left(a_list, target)
    if index < len(a_list) and a_list[index] == target:
        return True
    return False


print(binary_search(nums, 3))
print(binary_search(nums, 10))

# Get the ASCII code for a character
print(ord("A"))

# Given a list of words in alphabetical order, write a function that performs a binary search for a word and returns whether it is in the list
words = ["get", "going", "lets", "man"]


def binary_search_words(word_list, target):
    index = bisect_left(word_list, target)
    if index < len(word_list) and word_list[index] == target:
        return True
    return False


print(binary_search_words(words, "lets"))
print(binary_search_words(words, "mom"))
