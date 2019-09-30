def selection_sort(array):
    # i is the position we are filling
    for i in range(len(array)):
        next_smallest_index = i
        # Search remainder for next smallest
        for k in range(i, len(array)):
            if array[k] < array[next_smallest_index]:
                next_smallest_index = k

        # Swap out values
        aux = array[i]
        array[i] = array[next_smallest_index]
        array[next_smallest_index] = aux

    return array


def insertion_sort(array):
    # Next to place
    for i in range(1, len(array)):
        # Place element within pre-sorted section
        for k in range(0, i):
            if array[i] < array[k]:
                array.insert(k, array.pop(i))
                break
    return array


def bubble_sort(array):
    finished_sorting = False

    while not finished_sorting:
        finished_sorting = True

        for i in range(len(array) - 1):

            if array[i] > array[i + 1]:
                finished_sorting = False
                aux = array[i]
                array[i] = array[i + 1]
                array[i + 1] = aux

    return array


def merge_sort(array):
    if len(array) == 1:
        return array

    mid_point = int(len(array) / 2)
    section1 = merge_sort(array[0: mid_point])
    section2 = merge_sort(array[mid_point: len(array)])

    sorted_array = []

    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(section1) and ptr2 < len(section2) > 0:
        if section1[ptr1] < section2[ptr2]:
            sorted_array.append(section1[ptr1])
            ptr1 += 1
        else:
            sorted_array.append(section2[ptr2])
            ptr2 += 1

    # Add remainder
    for i in range(ptr1, len(section1)):
        sorted_array.append(section1[i])

    for i in range(ptr2, len(section2)):
        sorted_array.append(section2[i])

    return sorted_array


def quick_sort(array, start=None, end=None):
    if start is None or end is None:
        start, end = 0, len(array) - 1

    if end - start < 1:
        return array

    pivot = end
    last_smaller = start - 1

    for i in range(start, end):
        if array[i] <= array[pivot]:
            last_smaller += 1
            array[i], array[last_smaller] = array[last_smaller], array[i]

    array[last_smaller + 1], array[pivot] = array[pivot], array[last_smaller + 1]

    quick_sort(array, start, last_smaller)
    quick_sort(array, last_smaller + 2, end)

    return array
