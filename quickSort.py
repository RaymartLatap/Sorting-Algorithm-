def quick_sort(array, left_subarray, right_subarray):
    if left_subarray < right_subarray:
        partition_positon = partition(array, left_subarray, right_subarray)
        quick_sort(array, left_subarray, partition_positon - 1)
        quick_sort(array, partition_positon + 1, right_subarray)

def partition(array, left_subarray, right_subarray):
    i = left_subarray
    j = right_subarray - 1
    pivot = array[right_subarray]

    while i < j:
        while i < right_subarray and array[i] < pivot:
            i += 1

        while j > left_subarray and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
        
    if array[i] > pivot:
        array[i], array[right_subarray] = array[right_subarray], array[i]

    return i

array = [24, 27, 70, 74, 22, 39, 26, 56, 49, 18]
quick_sort(array, 0, len(array) - 1)

print(array)