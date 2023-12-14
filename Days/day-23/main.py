import time
from turtle import Screen
from player import FINISH_LINE_Y, STARTING_POSITION, Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #llego al final
    if player.is_at_finish_line():
        player.start()
        car_manager.level_up()
        scoreboard.point()


    
    
screen.exitonclick()
