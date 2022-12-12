from turtle import Turtle, Screen

play = Screen()

play.bgcolor("black")
play.screensize(250, 250)
play.title("Turtle Keys")

def position():
    coord = follow.coor()
    coord.color("white")
    coord.setposition(130, 100)

run = Turtle("triangle")
run.speed("fastest")
run.color("white")
run.penup()
run.setposition(250, 250)

print(position)
