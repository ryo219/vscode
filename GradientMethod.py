# 勾配法

import random
import math

def sum_of_squares_gradient(x): 
    return [2 * x_i for x_i in x]

def step(x, direction, step_size):
    return [x_i + step_size * direction_i for x_i, direction_i in zip(x, direction)]

def sum_of_squares(x):
    return sum(x_i ** 2 for x_i in x)

def vector_subtract(x, w):
    return [x_i - w_i for x_i, w_i in zip(x,w)]

def distance(x, w):
    return math.sqrt(sum_of_squares(vector_subtract(x, w)))

# 初期値設定
x = [random.randint(-10,10) for i in range(3)]
tolerance = 0.0000001   # ループを止める閾値

while True:
    gradient = sum_of_squares_gradient(x)
# 探索
    next_x = step(x, gradient, -0.01)

    if distance(next_x, x) < tolerance:
        break
    x = next_x
        
print("\r\nmin. x_i", x)
print("minumum value = ", sum_of_squares(x))