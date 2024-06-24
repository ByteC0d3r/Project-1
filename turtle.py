import turtle
from turtle import Screen,Turtle

wn = Screen()
wn.title("Pong by CGGamer")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

class Paddles(Turtle):  
    def __init__(self,position,size):
        super().__init__()
        self.position = position
        self.size = size
        self.speed(0)
        self.shape("square")
        self.shape("square")
        self.color("white")
        self.y = 20
        self.x = 20
        self.shapesize(size,1)
        self.penup()
        self.setposition(position)
    
    def moving_on_y_up(self):
          newy = self.ycor() + self.y
          self.goto(self.xcor(),newy)
   
    def moving_on_x_right(self):
        newx = self.xcor() + self.x
        self.goto(newx,self.ycor())

    def moving_on_y_down(self):
        newy = self.ycor() - self.y
        self.goto(self.xcor(),newy)
    
    def moving_on_x_left(self):
        newx = self.xcor() - self.x
        self.goto(newx,self.ycor())


paddle_a = Paddles((-350,0),5)
wn.listen()
wn.onkeypress(paddle_a.moving_on_y_up, "w")
wn.onkeypress(paddle_a.moving_on_x_right, "d")
wn.onkeypress(paddle_a.moving_on_y_down, "s")
wn.onkeypress(paddle_a.moving_on_x_left, "a")


paddle_b = Paddles((350,0),5)
wn.listen()
wn.onkeypress(paddle_a.moving_on_y_up, "w")
wn.onkeypress(paddle_a.moving_on_x_right, "d")
wn.onkeypress(paddle_a.moving_on_y_down, "s")
wn.onkeypress(paddle_a.moving_on_x_left, "a")



ball = Paddles((0,0),1)



while True:
    wn.update()