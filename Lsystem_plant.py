import turtle

# define the plant parameter
generations = 5
line_size = 5
drawing_angle = 40
axiom = "YYY"
initial_count = 0
state_stack = []

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


# method to create multiple generations of the plant string
# print the string for each generatíon
def applyRule(generationX, generation_count):
    generation_count += 1
    newGen=""   
    if generation_count > generations:
        return generationX
    else:
        for l in generationX:
            newGen = newGen.__add__(str("YFX[+Y][-Y]" if l == "Y" else "X[-FFF][+FFF]FX" if l == "X" else l))
        print("plant in generation",generation_count,":",newGen)
        return applyRule(newGen, generation_count)


# method to draw the plant string with turtle
def draw(plant_string):
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


# now generate the plant system
the_plant = applyRule(axiom, initial_count)
draw(the_plant)