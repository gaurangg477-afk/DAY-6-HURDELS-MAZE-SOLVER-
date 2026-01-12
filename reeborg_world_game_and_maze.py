#HURDEL NUMBER 1
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_reeborg():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
i=0  
while i<6:
    move_reeborg()
    i=i+1    


#HURDEL NUMBER 2
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not wall_in_front():
    if not wall_in_front():
        while front_is_clear():
            if at_goal():
                break
            move()
while wall_in_front():
    jump_wall()
    if not wall_in_front():
        while front_is_clear():
            if at_goal():
                break
            move()

#HURDEL NUMBER 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not wall_in_front():
    if not wall_in_front():
        while front_is_clear():
            if at_goal():
                break
            move()
while wall_in_front():
    jump_wall()
    if not wall_in_front():
        while front_is_clear():
            if at_goal():
                break
            move()

#MAZE SOLVER
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
    