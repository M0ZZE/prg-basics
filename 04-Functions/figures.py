import turtle

def main():
    figure()
    
def figure():
    window = turtle.Screen()
    window.bgcolor('cornflowerblue')
    pen=turtle.Turtle()
    pen.speed(5)
    side_lenght=None
    figure=input('chose figure: ')
    match figure:
        case 'square':
            square(side_lenght, pen)
        case 'triangle':
            triangle(side_lenght, pen)
        case 'rectangle':
            rectangle(side_lenght, pen)
        case 'other':
            other(side_lenght, pen)
        case _:
            print(f'No presset for {figure}, "other" choosen instead')
            other(side_lenght, pen)
    pen.hideturtle()
    window.mainloop()

def square(side_lenght, pen: turtle.Turtle):
    side_lenght=input('chose lenght of sides:  ')
    for i in range(4):
        pen.forward(int(side_lenght))
        pen.right(90)
        

def triangle(side_lenght, pen: turtle.Turtle):
    type=input('what typpe of triangle?: ').lower()
    match type:
        case 'equaliteral':
            side_lenght=input('input side lenght: ')
            for i  in range(3):
                pen.forward(int(side_lenght))
                pen.right(120)
        case _: 
            pass
            

def rectangle(side_lenght, pen: turtle.Turtle):
    side_lenght=input('chose lenght of first pair of sides:  ')
    temp=side_lenght
    side_lenght=input('chose lenght of second pair of sides:  ')
    for i in range(2):
        pen.forward(int(side_lenght))
        pen.right(90)
        pen.forward(int(temp))
        pen.right(90)

def other(side_lenght):
    pass


if __name__ == '__main__':
    main()