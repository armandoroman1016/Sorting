# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    a_index = 0
    b_index = 0

    for i in range(elements):

        if a_index >= len(arrA):
            merged_arr[i] = arrB[b_index]
            b_index += 1

        elif b_index >= len(arrB):
            merged_arr[i] = arrA[a_index]
            a_index += 1

        elif arrA[a_index] > arrB[b_index]:
            merged_arr[i] = arrB[b_index]
            b_index += 1

        elif arrA[a_index] < arrB[b_index]:
            merged_arr[i] = arrA[a_index]
            a_index += 1

        elif arrA[a_index] == arrB[b_index]:
            merged_arr[i] += arrA[a_index]
            a_index += 1
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) > 1:    

        middle = len(arr) // 2

        left = arr[0 : middle]
        right = arr[middle: ]

        left_side = merge_sort(left)

        right_side = merge_sort(right)

        arr = merge( left_side, right_side )

    return arr


nums = [100, 13, 88, 321]

merge_sort(nums)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
