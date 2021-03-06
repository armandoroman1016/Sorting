from timeit import default_timer as timer

### Recursive Solution
# TO-DO: Complete the selection_sort() function below 
def selection_sort_recursive( arr, starting_index = 0 ):
    smallest_index = starting_index
    # initialize a temporary smallest value with the value at the starting index argument
    temp_smallest = arr[starting_index]
    if starting_index == len(arr) - 1:
        return arr
    else:   
        for i in range(starting_index, len(arr)):
            cur_index = i
            # if the value of the current element is greater then the starting element 
            # and if the current element is greater then the temporary smallest variable  
            if arr[cur_index] <= arr[starting_index] and arr[cur_index] <= temp_smallest:

                # if the value at the current index is less then the temporary smallest value
                if cur_index < len(arr) - 2:
                    temp_smallest = arr[cur_index]

                # swapping
                smallest_index, cur_index = cur_index, smallest_index
        arr[starting_index], arr[smallest_index] = arr[smallest_index], arr[starting_index]

        return selection_sort_recursive( arr, starting_index + 1)


# 1. Separate the first element from the rest of the array. Think about it as a sorted list of one element.

# 2. For all other indices, beginning with [1]:

#     a. Copy the item at that index into a temp variable

#     b. Iterate to the left until you find the correct index in the "sorted" part of the array at which this element should be inserted  
#     - Shift items over to the right as you iterate
    
#     c. When the correct index is found, copy temp into this position

def selection_sort( arr ):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for j in range(i + 1, len(arr)):
            if arr[smallest_index] >= arr[j]:
                    smallest_index = j

        arr[i], arr[smallest_index]  = arr[smallest_index], arr[i]
                
    return arr

test_list = [4212, 1729, 4680, 4423, 5092, 6932, 2568, 5032, 1146, 6778, 1544, 2755, 6389, 5414, 9780, 6683, 8534, 810, 5302, 2039, 1364, 7301, 5107, 6310, 49, 6168, 359, 3827, 4155, 3255, 2998, 3997, 7884, 7425, 6279, 909, 6301, 5108, 2509, 7191, 4149, 1476, 8198, 5901, 31, 3637, 4367, 1683, 6784, 3054, 8243, 79, 5865, 3318, 8574, 8591, 4636, 9902, 5519, 3282, 3678, 8992, 2934, 7485, 5089, 4308, 8656, 8592, 1540, 7892, 8939, 1413, 7116, 1321, 9265, 8295, 3466, 1741, 6751, 8146, 4490, 9893, 3029, 8436, 8638, 990, 9781, 7020, 2869, 1425, 1329, 936, 7285, 1341, 3487, 8022, 4771, 1436, 4118, 595, 1180, 4306, 8118, 5528, 8893, 3634, 5820, 4365, 3961, 2976, 2843, 6117, 8317, 8103, 7120, 339, 149, 3458, 6204, 4775, 9263, 8765, 9609, 4418, 771, 2394, 5178, 2596, 1928, 3220, 1318, 8442, 4027, 7545, 1509, 6652, 4496, 499, 4110, 1934, 303, 6684, 2124, 1351, 5935, 6190, 5845, 8339, 3614, 1952, 3104, 7294, 1279, 5124, 3618, 9585, 4248, 8030, 3967, 8353, 5826, 8882, 805, 8073, 4528, 1615, 3853, 856, 2163, 5146, 6677, 9850, 6353, 6550, 2062, 919, 8858, 2734, 3043, 1281, 9936, 1749, 8841, 8790, 226, 8613, 1957, 7081, 9067, 6324, 9713, 9332, 5045, 7487, 1097, 1752, 326, 5904, 6224, 2786, 1268, 6640, 18, 7949, 5929, 4043, 4320, 8938, 7573, 3544, 472, 9784, 9018, 6916, 2679, 9388, 3871, 4253, 5683, 4068, 1001, 3443, 6026, 1108, 3923, 7439, 3492, 2460, 6930, 1661, 2056, 2226, 4399, 6256, 9147, 1550, 9818, 9566, 5279, 3457, 7649, 1591, 4559, 8651, 5292, 7078, 8511, 4628, 6064, 611, 9841, 9959, 1395, 2224, 4773, 9954, 8637, 2715, 4609, 8980, 5536, 8369, 7856, 7270, 1215, 3024, 7517, 6145, 3233, 5480, 2533, 2450, 120, 8394, 3723, 6835, 8392, 9560, 1264, 5703, 3954, 7838, 4317, 6029, 1405, 3266, 4225, 6834, 7556, 5191, 1350, 1290, 5770, 2914, 7700, 5778, 9886, 8999, 9788, 6473, 7783, 8750, 9799, 5301, 4577, 6407, 4487, 107, 7865, 9447, 8386, 5079, 3052, 3478, 7479, 4222, 4722, 7560, 3092, 7685, 780, 5962, 556, 6973, 5938, 5900, 5941, 1850, 2960, 4456, 3990, 9237, 119, 3335, 2754, 1379, 8023, 662, 2115, 8130, 8885, 490, 8843, 5836, 8225, 7003, 1109, 2593, 8677, 9236, 5153, 7956, 9950, 5639, 4552, 99, 9708, 4506, 9318, 4518, 2730, 3302, 7859, 9912, 9802, 8816, 8920, 8898, 8955, 9169, 1767, 8768, 6783, 8827, 2212, 5116, 1017, 4380, 8316, 484, 2561, 8134, 5162, 9428, 6421, 2179, 3909, 2257, 9891, 3133, 1051, 7188, 1454, 7765, 5777, 3683, 4067, 1111, 3869, 6357, 6394, 6877, 5647, 4619, 4023, 7166, 8049, 5303, 942, 1909, 9808, 7840, 4586, 8781, 1287, 3317, 2891, 7650, 7502, 2281, 1925, 5844, 1831, 3356, 6359, 2617, 3791, 126, 2114, 6657, 3548, 7099, 8543, 4717, 8007, 8384, 5020, 8652, 9854, 3432, 3307, 8396, 2977, 9732, 7912, 1302, 3235, 2275, 5790, 7962, 8770, 6370, 6126, 1044, 3303, 6893, 3023, 3889, 7655, 6225, 6146, 8889, 8897, 6049, 4058, 7229, 6515, 1526, 9156, 3433, 8926, 5615, 4165, 7360, 7684, 9418, 128, 8213, 715, 7872, 6539, 9440, 1898, 1214, 4825, 6847, 3851, 7908, 2164, 1118, 5606, 4254, 7518, 1356, 6036, 1558, 7992, 2746, 922, 9812, 4178, 2435, 4593, 3987, 4959, 313, 1570, 1800, 3981, 6679, 4718, 3700, 8143, 1801, 7234, 8953, 7558, 4376, 4373, 7731, 6870, 928, 5148, 2258, 9588, 2479, 5190, 4116, 778, 1870, 586, 2231, 9153, 5515, 8995, 6892, 2969, 5572, 4861, 9769, 2794, 2597, 1856, 643, 7242, 195, 2173, 5057, 4411, 8438, 2823, 5624, 9574, 981, 7653, 7094, 9373, 8266, 2836, 5275, 5551, 1936, 9487, 5105, 3796, 7262, 9605, 8456, 6108, 2468, 5157, 3281, 203, 6675, 141, 4476, 4463, 9978, 4993, 4249, 1083, 2964, 1516, 9432, 8166, 6321, 5392, 8075, 2193, 3161, 6638, 433, 6343, 6074, 8141, 8641, 6075, 736, 274, 4561, 1449, 8888, 2288, 7897, 1524, 6129, 8779, 200, 5028, 537, 8824, 2157, 5239, 3812, 1220, 686, 8694, 6580, 8568, 4246, 4263, 5297, 3699, 9744, 9652, 3439, 3428, 8857, 5976, 4689, 494, 844, 9089, 4188, 3823, 1879, 2445, 2413, 842, 4010, 4278, 3080, 9049, 3272, 3597, 182, 206, 6386, 6243, 1033, 6332, 2295, 4863, 3725, 8175, 5537, 1457, 7961, 5736, 9581, 1057, 7008, 6235, 4388, 5298, 4910, 8397, 8826, 500, 6105, 1529, 7940, 6621, 2064, 3454, 5283, 9554, 6633, 4061, 8584, 8497, 8288, 3738, 6131, 7957, 7414, 4141, 4750, 664, 5142, 3948, 1128, 8300, 190, 9539, 9963, 2135, 1607, 3148, 634, 3817, 2340, 4019, 5842, 3231, 7152, 9429, 1547, 4756, 9155, 3837, 3534, 2389, 3227, 9786, 9130, 4830, 6738, 1305, 1902, 2485, 5896, 9275, 2330, 7763, 8722, 2347, 5304, 9492, 9922, 1492, 3593, 1827, 6520, 5983, 8231, 4515, 3199, 8887, 918, 8473, 9064, 1045, 2440, 9255, 3404, 1192, 6681, 2520, 2682, 3759, 2661, 3627, 1823, 299, 6260, 6890, 9107, 8941, 9970, 4701, 1818, 9154, 5290, 3772, 4793, 1095, 6672, 3380, 7513, 4041, 8047, 1263, 409, 8909, 4881, 5449, 8358, 8818, 1495, 8268, 8626, 3872, 6699, 8393, 722, 7394, 2078, 314, 3792, 3784, 4362, 2499, 9056, 5062, 7792, 7349, 2696, 8907, 8390]
test_list_copy = test_list.copy()

start = timer()
selection_sort(test_list)
end = timer()
print('selection-sort / test_list', end-start)

start = timer()
selection_sort_recursive(test_list_copy)
end = timer()
print('selection-sort_recursive / test_list', end-start)


test_list_2 =[ 35, 10, 8, 13, 4, 24, 1, 17, 25, 5, 11, 13]
test_list_2_copy = test_list_2.copy()

start = timer()
selection_sort(test_list_2)
end = timer()
print('selection-sort / test_list_2', end-start)

start = timer()
selection_sort_recursive(test_list_2)
end = timer()
print('selection-sort_recursive / test_list_2', end-start)



# TO-DO:  implement the Bubble Sort function below

## Bubble Sort
# In **Bubble Sort**, we make a series of swaps between adjacent elements, 
# gradually moving larger elements towards the end of the array (or _bubbling_ larger elements up).

### Algorithm
# 1. Loop through your array
#     - Compare each element to its neighbor
#     - If elements in wrong position (relative to each other, swap them)
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.

def bubble_sort( arr ):
    sorted = False
    while not sorted:
        global swap_count 
        swap_count = 0
        for i in range(0, len(arr) - 1):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] =  arr[i + 1], arr[i]
                swap_count = swap_count + 1
        if swap_count == 0:
            sorted = True 


    return arr


start = timer()
bubble_sort(test_list)
end = timer()
print('bubble-sort_time / test_list', end-start)

start = timer()
bubble_sort(test_list_2)
end = timer()
print('bubble-sort_time / test_list_2', end-start)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr