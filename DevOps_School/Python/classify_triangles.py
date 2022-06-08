#!/usr/bin/env python3

def classifyTriangles(a, b, c):
    """
    The function returns a string with the type of triangle from three values corresponding to the lengths of the three sides of the Triangle.
    The theorem is: "The sum of the lengths of any two sides of a triangle is greater than the length of the third side of this triangle."
    """
    # check values to zero and negative
    if a <= 0 or b <= 0 or c <= 0:
        exit("The values cannot be zero or negative")
    # check triangles
    elif a + b <= c or a + c <= b or b + c <= a:
        print("The triangle cannot be")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("The triangle is a Right")
    elif a != b and a != c and b != c:
        print("The triangle is a Scalene")
    elif a == b == c:
        print("The triangle is an Equilateral")
    else:  
        print("The triangle is an Isosceles")  #a == b or b == c or a == c
 
def main():
    print("Please enter the length of the sides:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    classifyTriangles(a, b, c)

if __name__ == '__main__':
    main()
