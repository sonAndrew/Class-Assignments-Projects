""" 
    Andrew Jackson
    Intorduction to Computing and Programming Concepts
    CSCI 1523-92
    Laboratory Program # 2
    01/24/2022
    Zoa Buske
"""

side1 = int(input("Enter side 1 of the triangle: "))
side2 = int(input("Enter side 2 of the triangle: "))
side3 = int(input("Enter side 3 of the triangle: "))

if side1 == side2 == side3: 
    print("This (IS) an Equilateral Triangle.")
else:
    print("This (IS NOT) an Equilateral Triangle.")