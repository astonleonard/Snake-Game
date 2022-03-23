import random
import turtle as turtle_module

tim = turtle_module.Turtle()
color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

turtle_module.colormode(255)

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num = 0
for i in range(100):
    tim.speed("fastest")
    num += 1
    random_color = random.choice(color_list)
    tim.dot(20, random_color)
    tim.penup()
    tim.forward(50)

    if num % 10 == 0:
        tim.backward(500)
        tim.setheading(90)
        tim.forward(50)
        tim.right(90)

screen = turtle_module.Screen()
screen.exitonclick()
