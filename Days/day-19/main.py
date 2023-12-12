from turtle import Turtle, Screen

charlos = Turtle()
screen = Screen()


def move_forward():
    charlos.forward(10)
    
screen.listen()
screen.onkey(key="space", fun=move_forward) #function as input
screen.exitonclick() #higher order functions