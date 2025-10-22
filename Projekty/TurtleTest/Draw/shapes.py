from turtle import *

screen = Screen()
screen.tracer(0)

class Square:
    x = 0
    y = 0
    size = 0
    turtle = 0
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.turtle = Turtle()
    def draw(self):
        self.turtle.penup()
        self.turtle.home()
        self.turtle.goto(self.x, self.y)
        self.turtle.forward(self.size)
        self.turtle.left(90)
        self.turtle.forward(self.size/2)
        self.turtle.left(90)
        """Start drawing"""
        self.turtle.pendown()

        

        # Draw each side with delay using ontimer
        def draw_side(i):
            if i >= 4:
                return
            self.turtle.forward(self.size)
            self.turtle.left(90)
            screen.update()
            screen.ontimer(lambda: draw_side(i + 1), 50)  # Schedule next step after 50ms

        draw_side(0)

class Circle:
    x = 0
    y = 0
    size = 0
    turtle = 0
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.turtle = Turtle()
    def draw(self):
        self.turtle.penup()
        self.turtle.home()
        self.turtle.goto(self.x, self.y)
        self.turtle.forward(self.size)
        self.turtle.left(90)
        self.turtle.forward(self.size/2)
        self.turtle.left(90)
        """Start drawing"""
        self.turtle.pendown()
        
        def drawCirl(snake):
            screen.ontimer(lambda: snake.circle(self.size), 50)  # Schedule next step after 50ms
        
        drawCirl(self.turtle)

s1 = Square(0, 0, 50)
s2 = Square(100, 0, 50)
s3 = Square(-100, 0, 50)
c1 = Circle(200, 800, 50)
s4 = Square(0, 100, 50)
s5 = Square(0, -100, 50)

s1.draw()
s2.draw()
s3.draw()
c1.draw()
s4.draw()
s5.draw()

done()