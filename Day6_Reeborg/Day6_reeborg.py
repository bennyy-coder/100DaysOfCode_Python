
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not wall_on_right():
    turn_right()
    while front_is_clear():
        move()
    
while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
        
    