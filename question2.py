def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    result = expected_sum - actual_sum
    return result


arr = [1, 2,3, 5]

print(find_missing(arr, 5))