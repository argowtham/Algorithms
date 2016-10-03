def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def max_heapify(array, i):
    s = len(array)
    l = 2 * i + 1
    r = 2 * (i + 1)
    big = i
    if l < s and array[l] > array[big]:
        big = l
    if r < s and array[r] > array[big]:
        big = r
    if big != i:
        swap(array, i, big)
        max_heapify(array, big)
    return array


def heap_sort(array):
    s = len(array)
    for i in range(s // 2 - 1, -1, -1):
        max_heapify(array, i)
    print(array)
    for i in range(s-1, -1, -1):
        swap(array, i, 0)
        array[:i] = max_heapify(array[:i], 0)
    print(array)

if __name__ == "__main__":
    input_array = [8, 7, 6, 5, 4, 3, 2, 1]
    heap_sort(input_array)