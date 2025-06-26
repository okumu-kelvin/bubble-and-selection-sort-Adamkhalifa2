def selection_sort(arr):
    # TODO: Implement selection sort
    n = len(arr)

    # Go through each item in the list
    for i in range(n):
        # Assume the current index is the smallest
        min_index = i

        # Look for a smaller item in the rest of the list
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest item found with the current item
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
