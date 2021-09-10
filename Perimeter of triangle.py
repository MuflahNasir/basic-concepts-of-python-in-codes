edge1, edge2, edge3 = eval(input("Enter three edges: "))

if (edge1 + edge2 > edge3) and (edge1 + edge3 > edge2) and (edge2 + edge3 > edge1):

    perimeter = edge1 + edge2 + edge3
    print("The perimeter of a triangle is ", perimeter)

else:

    print("The input is invalid")
