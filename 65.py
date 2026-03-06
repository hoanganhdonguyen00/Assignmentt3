def remove_odds(numbers):
    return [x for x in numbers if x % 2 == 0]

original_list = [1,2,3,4,5,6,7,8,9]
filtered_list = remove_odds(original_list)
print("Original:", original_list)
print("Even only:", filtered_list)