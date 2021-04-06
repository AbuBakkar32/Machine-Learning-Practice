def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)


#####################################################################################

# def merge_sort(arr):
#     # The last array split
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     # Perform merge_sort recursively on both halves
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
#
#     # Merge each side together
#     return merge(left, right, arr.copy())
#
#
# def merge(left, right, merged):
#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):
#
#         # Sort each one and place into the result
#         if left[left_cursor] <= right[right_cursor]:
#             merged[left_cursor + right_cursor] = left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1
#
#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]
#
#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]
#
#     return merged
#
#
# print(merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
