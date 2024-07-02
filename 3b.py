def find_max_min(arr):
    max_num = max(arr)
    min_num = min(arr)
    return max_num, min_num

def find_second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.remove(max(unique_arr))
    second_largest = max(unique_arr)
    return second_largest

array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_num, min_num = find_max_min(array)
second_largest = find_second_largest(array)

print(f"Maximum number: {max_num}")
print(f"Minimum number: {min_num}")
print(f"Second largest number: {second_largest}")
