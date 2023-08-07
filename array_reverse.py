def reverse_array(arr):
  n = len(arr)
  for i in range(n // 2):
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
def print_array(arr):
  for i in range(len(arr)):
    print(arr[i], end=" ")
arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print_array(arr)