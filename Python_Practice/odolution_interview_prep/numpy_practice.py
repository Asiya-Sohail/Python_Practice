import numpy as np

# # Creating arrays
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.zeros(5)          # [0, 0, 0, 0, 0]
# arr3 = np.ones(3)           # [1, 1, 1]
# arr4 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
# arr5 = np.linspace(0, 1, 5) # 5 points between 0 and 1

# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)

# # 2D arrays
# matrix = np.array([[1, 2], [3, 4]])
# zeros_2d = np.zeros((2, 3))
# # It will give an error
# # zeros_2d = np.zeros(2,3)
# print(matrix)
# print(zeros_2d)

# # Mathematical operations
# arr = np.array([1, 2, 3, 4])
# print(arr + 5)         # Add scalar
# print(arr * 2)        # Multiply by scalar
# print(arr ** 2)        # Square elements
# print(np.sqrt(arr))    # Square root
# print(np.sum(arr))     # Sum all elements
# print(np.mean(arr))    # Average
# print(np.max(arr))     # Maximum value
# print(np.min(arr))     # Minimum value

# # Array indexing and slicing
# print(arr[0])          # First element
# print(arr[-1])        # Last element
# print(arr[1:3])        # Slice
# print(matrix[0, 1])    # 2D indexing


# # Array properties
# print(arr.shape)      # Dimensions
# # It returns a tuple representing the number of elements along each dimension (axis).

# print(arr.size)      # Total elements
# print(arr.dtype)       # Data type
# print(arr.ndim)        # Number of dimensions

arr = np.array([1, 5, 3, 8, 2])
mean_val = np.mean(arr)
result = arr[arr > mean_val]
print(result)