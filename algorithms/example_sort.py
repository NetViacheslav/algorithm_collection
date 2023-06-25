from algorithms.example_search_low_element_array import find_smallest
def selection_sort(arr: list[int]) -> int:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 2, 5, 6]))
