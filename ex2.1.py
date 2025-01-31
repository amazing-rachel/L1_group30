# i. The following code is a quadratic formula calculator, taking in three inputs (a, b, c) as floating point numbers.
# Then, it uses the mathematical formula b^2 +- 4ac to calculate delta, the sqrt of delta is then used to find the roots using the
# equation (-b +- sqrt(delta)) / 2a. The program then outputs whether it has real roots or imaginary roots.

# ii. The error is that the program does not account for a denominator of 0, for instance if a is being inputted as 0,
# then the calculation of the roots will fail in the following code. The solution we created is using raise an exception.

import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    if a == 0:
        raise Exception("Sorry, a must not be equal to zero. Cannot divide by zero.")

    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f"The solutions are: {root1}, {root2}")
    elif d == 0:
        root = -b / (2*a)
        print(f"The solution is: {root}")
    else:
        print("There are no real solutions.")

do_stuff()
