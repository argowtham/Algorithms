def merge_sort(arr_in):
    if len(arr_in) > 1:
        q = len(arr_in)//2
        left_arr = arr_in[: q]
        right_arr = arr_in[q:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        # Iterating through left and right array by each element to check which is greater and sorting it to the input
        # array
        j, k, l = 0, 0, 0
        while j < len(left_arr) and k < len(right_arr):
            if left_arr[j] > right_arr[k]:
                arr_in[l] = right_arr[k]
                k += 1
            else:
                arr_in[l] = left_arr[j]
                j += 1
            l += 1

        while j < len(left_arr):
            arr_in[l] = left_arr[j]
            j += 1
            l += 1

        while k < len(right_arr):
            arr_in[l] = right_arr[k]
            k += 1
            l += 1
        return arr_in


if __name__ == "__main__":
    print("Program to demonstrate Insertion sort")
    n = int(input("Enter the number of elements"))
    print("Enter the elements one by one")
    arr = []
    for i in range(0, n):
        arr.append(int(input()))
    print("Input array: ", arr)
    # Calling merge sort algorithm
    print(merge_sort(arr))
