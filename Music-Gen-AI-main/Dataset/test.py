def Magic(n):
    sum = 0

    while (n > 0 or sum > 9):
        if (n == 0):
            n = sum
            sum = 0
    
        sum = sum + (n % 10)**2
    return True if (sum == 1) else False

n = 24
if (Magic(n)):
    print("Yes")
else: 
    print("No")