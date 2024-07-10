from graphics import Canvas
import random

CANVAS_WIDTH = 420      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    
#to move the brick by 1 block, (x=10 , y , x+10 , y)
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    mov1 = 0
    BRICK_WIDTH = 30
    hei1 = 288
    hei2 = 300
    num = 0
    count = 10  # or whatever initial value you need
    while count != 0:
    
        
        for i in range(count):
            print(str(hei1) + "|" + str(hei2) + "|" + str(mov1) + "|" + str(BRICK_WIDTH))

            
#brick initialized
    #for i in range(BRICKS_IN_BASE): 
        brick = canvas.create_rectangle(mov1,hei2,BRICK_WIDTH,hei1,"yellow","black")
        mov1+=30
        BRICK_WIDTH+=30

    #resets value
    mov1 = 0 + (15 * num)
    BRICK_WIDTH = 30 + (15 * num)
    print("---")
    print("NEW LINE")
    print("mov1 =" + str (mov1))
    print("BRICK_WIDTH =" + str(BRICK_WIDTH))
    print("---")


    num += 1

    hei1 -= 14
    hei2 -= 14

    #problem is here,find a way to increment mov1 and brick width by 15 
    #the problem here is that i keep resetting the value

    mov1 += 15
    BRICK_WIDTH +=15 




    
    mov1+=30
    BRICK_WIDTH+=30

   


    # TODO, your code here
    

if __name__ == '__main__':
    main()