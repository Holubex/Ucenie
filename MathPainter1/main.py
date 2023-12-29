from canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

colors = {"black": [0, 0, 0], "white": [255, 255, 255], "red": [255, 0, 0], "green": [0, 255, 0], "blue": [0, 0, 255]}
canvas_color = input('Enter canvas color(white or black): ')
canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

# shape_type = input('What do you want to draw? Enter quit to quit. ')

while True:
    shape_type = input('What do you want to draw? Enter quit to quit. ')
    if shape_type.lower() == 'rectangle':
        rec_x = int(input('Enter x coordinate: '))
        rec_y = int(input('Enter y coordinate: '))
        rec_width = int(input('Enter width: '))
        rec_height = int(input('Enter height: '))
        red = int(input('Enter red: '))
        green = int(input('Enter green: '))
        blue = int(input('Enter blue: '))

        # create rectangle
        rl = Rectangle(x=rec_x, y=rec_y, width=rec_width, height=rec_height, color=[red, green, blue])
        rl.draw(canvas)

    if shape_type.lower() == 'square':
        sq_x = int(input('Enter x coordinate: '))
        sq_y = int(input('Enter y coordinate: '))
        sq_side = int(input('Enter side: '))
        red = int(input('Enter red: '))
        green = int(input('Enter green: '))
        blue = int(input('Enter blue: '))

        #create square
        sq = Square(x=sq_x, y=sq_y, side=sq_side, color=[red, green, blue])
        sq.draw(canvas)

    if shape_type.lower() == 'quit':
        break

canvas.make('image.png')