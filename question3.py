def count_occurrence(arr,value):
        count = 0
        for num in arr:
                if num == value:
                        count += 1
        return count                
arr = [1,2,2,3,3,2]
print(count_occurrence(arr,3))