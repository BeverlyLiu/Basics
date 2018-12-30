''' Display the fibonacci sequence up to n-th term where n is provided by the user '''

n = int(input("How many terms? "))

a, b = 0, 1
for i in range(0, n):
    print(a)
    a, b = b, a + b