import numpy as np

# Read and display a 2D Array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:")
print(array)

# Display the array elements in reverse order
reverse_array = np.flip(array)
print("Array elements in reverse order:")
print(reverse_array)

# Display all the elements of the principal diagonal elements
principal_diagonal = np.diagonal(array)
print("Principal diagonal elements:")
print(principal_diagonal)

# Sort the 2D array in ascending order
sorted_array_asc = np.sort(array, axis=None).reshape(array.shape)
print("2D array sorted in ascending order:")
print(sorted_array_asc)

# Sort the 2D array in descending order
sorted_array_desc = np.sort(array, axis=None)[::-1].reshape(array.shape)
print("2D array sorted in descending order:")
print(sorted_array_desc)
