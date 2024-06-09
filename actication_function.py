import math
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def activation_function(func, x):
    if func == 'sigmoid':
        return 1/(1+math.e**(-x))
    elif func == 'relu':
        return max(0,x)
    elif func == 'elu':
        alpha = 0.01
        if x > 0:
            return x
        else:
            return alpha*(math.e**x -1)
    else:
        return 'is not supported'

x = input('x = ')
if is_number(x):
    x = float(x)
    func = input('Input activation Function (sigmoid|relu|elu): ')
    print(f'{func} {activation_function(func, x)}')
else:
    print('x must be a number')