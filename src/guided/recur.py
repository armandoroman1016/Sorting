def recur_power(a, b):
    if b == 0: return 1
    return a * recur_power(a, b - 1)

# print(recur_power(2, 8))

def partition(data):
    left = []
    pivot = data[0]
    right = []

    for v in data[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right

def quicksort(data):
    
    if len(data) <= 1:
        return data

    print('data', data)
    
    left, pivot, right = partition(data)

    print('partition:', left, pivot, right)

    return quicksort(left) + [pivot] + quicksort(right)

quicksort([5, 9, 3, 7, 2, 8, 1, 6])