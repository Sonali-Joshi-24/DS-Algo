# This is an iterative code for Binary Search algorithm.

lst = [0,1,2,3,4,5,6]
searchElement = 9
start = 0
end = len(lst)-1
found = 0

while start<=end:
    mid = (start + end) // 2
    if searchElement == lst[mid]:
        found = 1
        break
    elif searchElement<lst[mid]:
        end = mid - 1
    elif searchElement>lst[mid]:
        start = mid + 1


if found==1:
    print("Element Found")
else:
    print("Element Not Found")
