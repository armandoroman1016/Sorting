from timeit import default_timer as timer

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr, starting_index = 0 ):
    smallest_index = starting_index
    # initialize a temporary smallest value with the value at the starting index argument
    temp_smallest = arr[starting_index]
    if starting_index == len(arr) - 1:
        return arr
    else:   
        for i in range(starting_index, len(arr)):
            cur_index = i
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)

            # if the value of the current element is greater then the statring element 
            # and if the current element is greater then the temporary smallest variable  
            if arr[cur_index] <= arr[starting_index] and arr[cur_index] <= temp_smallest:

                # if the value at the current index is less then the temporary smallest value
                if cur_index < len(arr) - 2:
                    temp_smallest = arr[cur_index]

                # swapping
                smallest_index, cur_index = cur_index, smallest_index
        arr[starting_index], arr[smallest_index] = arr[smallest_index], arr[starting_index]

        return selection_sort( arr, starting_index + 1)

test_list = [408, 19, 142, 288, 652, 744, 284, 831, 992, 642, 330, 825, 777, 473, 355, 755, 83, 663, 890, 515, 413, 372, 123, 301, 521, 773, 603, 430, 402, 974, 235, 647, 751, 740, 460, 336, 567, 985, 486, 573, 40, 354, 114, 794, 703, 561, 20, 997, 551, 108, 747, 849, 29, 837, 240, 861, 923, 577, 811, 906, 396, 358, 232, 84, 485, 17, 441, 121, 916, 422, 969, 98, 100, 737, 639, 909, 209, 190, 218, 365, 314, 76, 1, 344, 41, 623, 483, 440, 88, 979, 383, 944, 414, 687, 117, 374, 325, 578, 899, 714, 387, 982, 648, 519, 904, 918, 37, 67, 326, 771, 607, 158, 963, 87, 181, 927, 645, 805, 297, 273, 842, 86, 33, 579, 706, 846, 182, 834, 245, 8, 989, 285, 175, 367, 318, 789, 260, 917, 977, 520, 782, 243, 370, 555, 349, 947, 231, 237, 787, 633, 581, 282, 698, 902, 606, 654, 814, 853, 780, 463, 404, 54, 168, 637, 929, 932, 635, 563, 438, 970, 822, 377, 109, 854, 503, 719, 419, 379, 936, 280, 248, 524, 640, 180, 757, 388, 310, 208, 884, 562, 753, 399, 202, 244, 806, 894, 588, 42, 234, 545, 386, 650, 214, 407, 961, 103, 266, 274, 138, 487, 871, 516, 893, 594, 496, 357, 634, 433, 296, 700, 572, 775, 956, 321, 272, 718, 267, 605, 191, 949, 427, 134, 329, 62, 238, 697, 631, 449, 169, 629, 482, 223, 625, 800, 119, 454, 841, 868, 920, 242, 199, 254, 624, 129, 953, 102, 601, 764, 283, 612, 922, 306, 934, 459, 262, 361, 583, 809, 547, 609, 541, 65, 315, 424, 46, 844, 821, 342, 951, 90, 596, 804, 752, 785, 699, 745, 35, 10, 746, 96, 324, 530, 198, 556, 998, 776, 320, 436, 364, 599, 604, 769, 636, 858, 74, 144, 569, 966, 366, 816, 213, 826, 859, 597, 80, 85, 220, 693, 668, 688, 860, 695, 658, 799, 534, 726, 317, 621, 803, 489, 638, 540, 224, 845, 575, 539, 79, 850, 911, 543, 554, 685, 241, 857, 838, 52, 16, 253, 926, 990, 319, 943, 739, 513, 900, 511, 914, 878, 78, 510, 401, 44, 72, 286, 881, 713, 915, 673, 620, 405, 632, 728, 12, 152, 807, 233, 279, 767, 228, 743, 122, 955, 526, 462, 216, 480, 371, 659, 671, 950, 786, 299, 59, 298, 293, 116, 201, 484, 506, 877, 788, 708, 557, 883, 132, 879, 28, 492, 672, 133, 533, 334, 287, 148, 733, 362, 971, 382, 395, 468, 61, 110, 962, 796, 984, 183, 993, 976, 166, 661, 704, 722, 731, 147, 112, 453, 531, 759, 905, 653, 363, 73, 347, 616, 448, 170, 143, 333, 171, 912, 887, 177, 9, 679, 707, 393, 730, 258, 880, 580, 791, 870, 300, 537, 508, 53, 291, 311, 772, 351, 48, 162, 729, 504, 219, 179, 141, 570, 497, 443, 763, 415, 550, 105, 151, 137, 470, 781, 778, 762, 23, 942, 465, 339, 131, 783, 535, 792, 392, 227]
start = timer()
selection_sort(test_list)
end = timer()
print(end-start)

# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr