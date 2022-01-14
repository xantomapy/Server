from math import cos, sqrt


x = 0

try:
    x = float(input())
except ValueError:
    print('nepravilno')

x *= cos(sqrt(x))

print(f'x: {x}')
