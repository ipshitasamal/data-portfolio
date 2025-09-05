import math
num = float(input("Enter a number: "))

sqrt_val = math.sqrt(num)
log_val = math.log(num)   # natural log (base e)
sine_val = math.sin(num)  # sine (num in radians)

print(f"Square root of {num} is: {sqrt_val}")
print(f"Natural logarithm of {num} is: {log_val}")
print(f"Sine of {num} radians is: {sine_val}")
