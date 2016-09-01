if __name__ == '__main__':
    n = eval(input("Enter the number of elements"))
    print("Enter the elements one by one")
    array = []
    for i in range(0, n):
        array.append(eval(input()))
    print("Input array: ", array)
    i = len(array) // 2
    while i < len(array):
        if i > array[i]:
            i += (i // 2)
        elif i < array[i]:
            i -= (i // 2)
        else:
            print(i)
            break
