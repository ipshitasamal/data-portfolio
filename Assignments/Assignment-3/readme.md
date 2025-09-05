

## **Task 1: Calculate Factorial Using a Function**  

### Problem Statement  
Write a Python program that:  
1. Defines a function named `factorial` that takes a number as an argument and calculates its factorial using a loop or recursion.  
2. Returns the calculated factorial.  
3. Calls the function with a sample number and prints the output.  

### Expected Output  
For example, if the function is called with `5`, it should return:  

# Task 2: Using the Math Module for Calculations  

## Problem Statement  
Write a Python program that:  
1. Asks the user for a number as input.  
2. Uses the math module to calculate the:  
   - Square root of the number  
   - Natural logarithm (log base *e*) of the number  
   - Sine of the number (in radians)  
3. Displays the calculated results.  

---

## Example Code  
```python
import math

num = float(input("Enter a number: "))

print(f"Square root of {num} is: {math.sqrt(num)}")
print(f"Natural logarithm of {num} is: {math.log(num)}")
print(f"Sine of {num} radians is: {math.sin(num)}")


