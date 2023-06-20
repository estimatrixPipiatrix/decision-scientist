# estimate pi using a monte carlo process. hint: imagine throwing
# darts at a square and considering how many hit within a circle
# inscribed in the square

# idea: if it's a unit square, it's area is 1; a circle inscribed 
# inside will have area pi*r^2 = pi. the equation of a unit circle 
# centered at the origin is x^2 + y^2 = 1; solving for y gives
# y = +-sqrt(1-x^2). to keep from having to consider multiple cases
# we can restrict attention to the first quadrant, in which case
# circle area to total area will be pi/4. so the fraction of darts
# that hit inside the circle will be pi/4

import numpy as np

def estimate_pi(num_iter):
    in_circle = 0
    for i in range(num_iter):
        x = np.random.random()
        y = np.random.random()
        if y < np.sqrt(1-x**2.0):
            in_circle += 1
    return 4.0*in_circle/num_iter

num_iter = 1000
print(estimate_pi(num_iter))
