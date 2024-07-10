from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    x1 = 0
    y1 = 100
    

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    for i in range(N_BOXES):
        in_rec = canvas.create_rectangle(x1,200,y1,100,"white","black")

    x1 += 100
    y1 += 100
    

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    