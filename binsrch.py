def binarySearch(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = int(input("Enter the key to search: "))
result = binarySearch(array, key)
if result != -1:
    print(f"Key {key} found at index {result}.")
else:
    print(f"Key {key} not found in the array.")
