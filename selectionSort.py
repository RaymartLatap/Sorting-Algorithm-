def selection_sort(array):
    for i in range(9):
        min_position = i
        for j in range(i, 10):
            if array[j] < array [min_position]:
                min_position = j

        temp_var = array[i]
        array[i] = array[min_position]
        array[min_position] = temp_var

array = [24, 27, 70, 74, 22, 39, 26, 56, 49, 18]
selection_sort(array)

print(array)