perimeter = int(input())     # perimeter of rectangle
diff = int(input())         # difference between lenght and breadth
b = int((perimeter - 2*diff)/4)
a = diff + b
print(a*b)
print ("the area of rectangle",a*b)
