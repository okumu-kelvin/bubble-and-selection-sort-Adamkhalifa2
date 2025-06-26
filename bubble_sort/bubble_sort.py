def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort

    n = len(unsorted_list)


    for i in range(n):

        for j in range(0, n - 1 - i):

            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]


    return unsorted_list
