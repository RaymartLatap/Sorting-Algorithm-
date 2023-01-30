def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temp_var = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp_var

array = [24, 27, 70, 74, 22, 39, 26, 56, 49, 18]
bubble_sort(array)

print(array)