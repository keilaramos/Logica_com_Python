# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)       
print(fibonacci(6))
    
