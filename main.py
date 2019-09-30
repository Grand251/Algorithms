from numpy.random import rand

from sorting import selection_sort, insertion_sort, bubble_sort, merge_sort, quick_sort

array_to_sort = (rand(10) * 100).tolist()


print(selection_sort(array_to_sort.copy()) == sorted(array_to_sort))

print(insertion_sort(array_to_sort.copy()) == sorted(array_to_sort))

print(bubble_sort(array_to_sort.copy()) == sorted(array_to_sort))

print(merge_sort(array_to_sort.copy()) == sorted(array_to_sort))

print(quick_sort(array_to_sort.copy()) == sorted(array_to_sort))
