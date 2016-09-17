def Staircase(n):
    # j = n-1
    # k = 1
    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)

if __name__ == '__main__':
    _n = int(input())
    Staircase(_n)
