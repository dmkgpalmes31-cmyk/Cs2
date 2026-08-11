import math # to make functions exclusive to the math library work

X1 = float(input("Enter coordinate X:")) # coordinate 1
Y1 = float(input("Enter coordinate Y:")) # coordinate 1
X2 = float(input("Enter coordinate X:")) # coordinate 2
Y2 = float(input("Enter coordinate Y:")) # coordinate 2

distance = math.sqrt(math.pow(X2 - X1, 2) + math.pow(Y2 - Y1, 2)) # Equation of the problem
                     
print(f"The Distance between the coordinate is, {distance:.2f}") # Round off to the nearest 2 decimals
