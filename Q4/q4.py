import math
import random

def IsInCircle(x, y):
    l = math.sqrt(x**2 + y**2)
    if l < circle:
        return True
    else:
        return False

def PI(rng):
    num = 0
    for i in range(rng):
        point = [random.uniform(-n/2, n/2), random.uniform(-n/2, n/2)]
        if IsInCircle(point[0], point[1]):
            num += 1
    return num/rng*4

def Find():
    error = 1
    count = 1
    while error > 0.01 :
        error = abs(PI(count) - math.pi)
        count += 1
    return count


if __name__ == '__main__':
    n = 1
    square = [-n/2, -n/2, n/2, n/2]
    circle = n/2
    x = random.uniform(-n/2, n/2)
    y = random.uniform(-n/2, n/2)
    print(f'point { {x}, {y} } is in circle: {IsInCircle(x,y)}')
    print(f'the numbers count to have error < 0.01 is: {Find()}')

    num2 = int(input ("enter a number to: "))
    sum = 0
    for i in range(num2):
        sum += Find()
    print('average of the function:Find() calls to have error < 0.01: {:.7}'.format(sum/num2))
