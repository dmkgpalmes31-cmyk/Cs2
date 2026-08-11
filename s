import math

X1 = float(input("Enter coordinate X:"))
Y1 = float(input("Enter coordinate Y:"))
X2 = float(input("Enter coordinate X:"))
Y2 = float(input("Enter coordinate Y:"))

distance = math.sqrt(math.pow(X2 - X1, 2) + math.pow(Y2 - Y1, 2))
                     
print(f"The Distance between the coordinate is, {distance:.2f}")
