# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    if len(arr) > 0:

        for i in range(0, len(arr) - 1):
            cur_index = i
            smallest_index = cur_index
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)  
            for j in range((cur_index + 1), len(arr)):
                if arr[j] < arr[smallest_index]:
                    smallest_index = j

            # TO-DO: swap
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]     


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    while True:

        changes = 0

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] 
                changes += 1
                
        if changes == 0:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr