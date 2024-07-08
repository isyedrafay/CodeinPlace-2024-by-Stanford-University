from karel.stanfordkarel import *

# ----------------------------
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    build_column()
	
    while front_is_clear():
        for _ in range(4):
            move()
        build_column()

def build_column():
    turn_left()
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

if __name__ == '__main__':
    main()