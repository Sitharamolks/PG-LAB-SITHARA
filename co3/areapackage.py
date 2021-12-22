from graphics import circle
from graphics import rectangle
from graphics import sphere
from graphics import cuboid

r=int(input("enter the radius:"))
circle.circles(r)

l=int(input("enter the lenght:"))
b=int(input("enter the bredth:"))
rectangle.rectangles(l,b)

r=int(input("enter the radius:"))
sphere.sphere(r)


l=int(input("enter the lenght:"))
b=int(input("enter the bredth:"))
h=int(input("enter the height:"))
cuboid.cuboid(l,b,h)

