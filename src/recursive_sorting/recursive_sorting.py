# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    a_index = 0
    b_index = 0
    print('a', arrA)
    print('b', arrB)

    if elements == 2:
        smaller = min(arrA[0], arrB[0])
        larger = max(arrA[0], arrB[0])
        merged_arr[0] = smaller
        merged_arr[1] = larger
        return merged_arr

    else:
        for i in range(0, elements):
            if a_index == len(arrA):
                a_index = len(arrA)
                merged_arr[i] = arrB[b_index]
                b_index += 1
            elif b_index == len(arrB):
                b_index = len(arrB)
                merged_arr[i] = arrA[a_index]
                a_index += 1
            elif arrA[a_index] < arrB[b_index]:
                merged_arr[i] = arrA[a_index]
                a_index += 1
            elif arrA[a_index] > arrB[b_index]:
                merged_arr[i] = arrB[b_index]
                b_index += 1
            elif arrA[a_index] == arrB[b_index]:
                merged_arr[i] = arrA[a_index]
                a_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# Algorithm
'''
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
'''


def merge_sort(arr):
    # TO-DO

    if len(arr) > 1:
        middle_index = len(arr) // 2
        left = arr[0: middle_index]
        right = arr[middle_index:]
        s_left = merge_sort(left)
        s_right = merge_sort(right)
        arr = merge(s_left, s_right)

    return arr


print(merge_sort([10, 5, 99, 12, 65, 49, -10, 18, 33, 45, 88, 10]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
