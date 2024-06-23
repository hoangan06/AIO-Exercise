def giai_thua(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

def approx_sin(x, n):
    result = 0
    for i in range(n+1):
        result += ((-1)**i)*(x**(2*i+1))/giai_thua(2*i+1)
    return result

def approx_cos(x, n):
    result = 0
    for i in range(n+1):
        result += ((-1)**i)*(x**(2*i))/giai_thua(2*i)
    return result

def approx_sinh(x, n):
    result = 0
    for i in range(n+1):
        result += (x**(2*i+1))/giai_thua(2*i+1)
    return result

def approx_cosh(x, n):
    result = 0
    for i in range(n+1):
        result += (x**(2*i))/giai_thua(2*i)
    return result

print(approx_sin(x=3.14, n=10))
print(approx_sinh(x=3.14, n=10))
print(approx_cos(x=3.14, n=10))
print(approx_cosh(x=3.14, n=10))