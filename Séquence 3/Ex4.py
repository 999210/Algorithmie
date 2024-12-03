# boucle Fibonacci
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        c = a + b
        a, b = b, c 
    return a

# récursive Fibonacci
def fibonacci (n, a=0, b=1):
    if n == 0:
        return a 
    elif n == 1:
        return b 
    else:
        return fibonacci (n-1, b, a+b)
     