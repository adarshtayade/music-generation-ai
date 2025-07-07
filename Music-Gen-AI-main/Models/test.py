
num = int(input("Enter a nnumber: "))
square = 0

if num > 0:
    while square != 1:
        n = num % 10
        square = n*n + square
        print(square)
        n = num // 10

        