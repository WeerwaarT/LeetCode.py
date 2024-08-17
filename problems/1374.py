def generateTheString(n):
    if n % 2 == 0:
        return (n - 1) * 'a' + 'b'
    else:
        return n * 'a'
