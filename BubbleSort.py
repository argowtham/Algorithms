def swap(a, b):
    return b, a


def bubble_sort(arr_in):
    for i in range(0, len(arr_in)):
        for j in range(0, len(arr_in)-1-i):
            if arr_in[j] > arr_in[j+1]:
                arr_in[j], arr_in[j+1] = swap(arr_in[j], arr_in[j+1])
    print("Array Sorted by Bubble sort: ", arr_in)


if __name__ == '__main__':
    print("Program to demonstrate Bubble sort")
    n = int(input("Enter the number of elements"))
    print("Enter the elements one by one")
    arr = []
    for element in range(0, n):
        arr.append(int(input()))
    print("Input array: ", arr)
    # Calling Bubble sort algorithm
    bubble_sort(arr)
