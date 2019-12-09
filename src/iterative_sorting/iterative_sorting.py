# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements

    smallest_num = None

    for i in range(0, len(arr) - 1):
        cur_index = i
        # smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        if cur_index == 0 or arr[cur_index] < smallest_num:
            smallest_num = arr[cur_index]
            smallest_index = cur_index


        # TO-DO: swap

    print(smallest_index)


    return arr

selection_sort([1,4,3,6,-10,25])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr