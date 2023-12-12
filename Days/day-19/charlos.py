from turtle import Turtle, Screen

charlos = Turtle()
screen = Screen()

def move_forward():
    charlos.forward(10)

def move_backward():
    charlos.back(10)

def move_clockwise():
    charlos.left(10)

def move_counter_clockwise():
    charlos.right(10)

def clear_screen():
    charlos.clear()
    charlos.penup()
    charlos.home() #return to the center
    charlos.pendown()
    
    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_counter_clockwise) 
screen.exitonclick() 

