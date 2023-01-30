def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array [j - 1]
            j -= 1
        
array = [24, 27, 70, 74, 22, 39, 26, 56, 49, 18]
insertion_sort(array)

print(array)