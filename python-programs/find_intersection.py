def find_intersect(arr1, arr2):
    arr1.sort()
    arr2.sort()
    result = []
    i , j = 0 , 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return list(set(result))
arr1 = [1,23,2,3,2]
arr2 = [2,2]
print(find_intersect(arr1,arr2))



