def extraLongFactorials(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)
    
# time complexity: O(n)