import turtle as t
t.Screen().bgcolor("orange")
t.Screen().setup(500,500)
hexagon = t.Turtle()
sides = 6
side_len = 70
angle = 360.0/sides
for i in range(sides):
    hexagon.forward(side_len)
    hexagon.right(angle)
t.done()