if __name__ == '__main__':
    array = [-1, 0, 1, 2, 4]
    i = len(array) // 2
    while i < len(array):
        if i > array[i]:
            i += (i // 2)
        elif i < array[i]:
            i -= (i // 2)
        else:
            print(i)
            break
