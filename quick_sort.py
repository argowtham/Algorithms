def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def partition(array, p, r):
    pivot = array[0]
    i = 1
    j = len(array)-1
    while i <= j:
        if array[i] > pivot:
            if array[j] < pivot:
                swap(array, i, j)
            else:
                j -= 1
        else:
            i += 1
    swap(array, 0, j)
    return i+1


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q-1)
        quick_sort(array, q, r)
    print(array)


if __name__ == "__main__":
    input_array = [2, 7, 1, -2, 56, 5, 3]
    quick_sort(input_array, 0, len(input_array))