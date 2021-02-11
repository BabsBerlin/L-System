import turtle

def initializeTurtleDrawer():
    # initialize the screen for drawing
    s = turtle.Screen()
    s.bgcolor("#CCCCCC")
    s.title("l-system plant")

    # initialize the turtle class
    t = turtle.Turtle()
    t.pensize(1)
    drawingColor="white"
    t.pencolor(drawingColor)
    t.setheading(90)
    t.penup()
    t.goto(0,-250)
    # t.speed(10)
    t._tracer(0)     
    return t

# method to draw the plant string with turtle
def draw(t, plant_string, line_size, drawing_angle):
    state_stack = []
    for letter in plant_string:   
        if letter == "F":
            t.pendown()
            t.forward(line_size)
            t.penup()
        elif letter == "+":
            t.left(drawing_angle)
        elif letter == "-":
            t.right(drawing_angle)
        elif letter == "[":
            oldState = t.heading(), t.position()
            state_stack.append(oldState)
        elif letter == "]":
            newState = state_stack.pop()
            t.setheading(newState[0])
            t.setposition(newState[1][0], newState[1][1])
    turtle.done()
