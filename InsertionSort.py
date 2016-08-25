def insertion_sort(arr_in):
    for j in range(1, len(arr_in)):
        key = arr_in[j]
        k = j - 1
        while k >= 0 and arr_in[k] > key:
            arr_in[k+1] = arr_in[k]
            k -= 1
        arr_in[k+1] = key
    print("Array sorted using Insertion sort: ", arr_in)

if __name__ == "__main__":
    print("Program to demonstrate Insertion sort")
    n = int(input("Enter the number of elements"))
    print("Enter the elements one by one")
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    print("Input array: ", arr)
    # Calling insertion sort algorithm
    insertion_sort(arr)


