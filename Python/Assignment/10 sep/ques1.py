import math
def area(side1,side2,side3):
    assert (side1+side2>side3 and side2+side3>side1 and side3+side1>side2),"Sum of the lengths of two sides is less than third side"
    s=(side1+side2+side3)/2
    area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area

side1=int(input("Enter first side of triangle :"))
side2=int(input("Enter second side of triangle :"))
side3=int(input("Enter third side of triangle :"))

a=area(side1,side2,side3)
print("Area of triangle is :",a)


    

          
