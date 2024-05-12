# Used on reborg.ca
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# What you need to know

#     The functions move() and turn_left().
#     Either the test 
#       front_is_clear() or 
#       wall_in_front(), 
#       right_is_clear() or 
#       wall_on_right(), and 
#       at_goal().

# wall_in_front(), wall_on_right(), at_goal(), move(), turn_left()

#     How to use a while loop and if/elif/else statements.
#     It might be useful to know how to use the negation of a test (not in Python).

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        
    elif front_is_clear():
        move()
       
    else:
        turn_left()


