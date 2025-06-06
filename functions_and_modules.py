#modules
import math

'''Calculate Factorial using a Function'''

n = int(input("Enter a number: "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))


result = factorial(n)
print(f"Factorial of {n} is {result}")

'''Using Math module for calculations'''

n = int(input("Enter a number: "))

square_root = math.sqrt(n)
print(f"Square root: {square_root}")

natural_logarithm = math.log(n)
print(f"Logarithm: {natural_logarithm}")

sine_value = math.sin(n)
print(f"Sine: {sine_value}")