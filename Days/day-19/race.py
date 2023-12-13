from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors= ["red","blue","orange","purple","green","yellow"]
y_position = [-100,-50,0,50,100,150]
all_turtles = []

for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:   
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! the {winning_color} turtle is the winner!")
            else:
                print(f"You lose :( the {winning_color} turtle is the winner.") 
                
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
    
    
screen.exitonclick()
