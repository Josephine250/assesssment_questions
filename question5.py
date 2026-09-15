def flatten_array(arr):
    result = []

    for item in arr:
        if isinstance(item, list):
            result.extend(flatten_array(item))
        else:
            result.append(item)

    return result


arr = [1, [2, 3], 4]

print(flatten_array(arr))