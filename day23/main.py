import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

while True:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_all()
    stop = False
    for ind in range(len(car_manager.all_cars) - 1, 0, -1):
        if player.distance(car_manager.all_cars[ind]) < 20:
            stop = True
            scoreboard.game_over()
            break
    if stop == True:
        break
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        scoreboard.update()
        car_manager.level_up()
screen.exitonclick()