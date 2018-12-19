from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self,radius , color , speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)

ball1 = Ball(50 , "red" , 50)
ball2 = Ball(50 , "green" , 70)
ball2.penup()
ball2.goto(69,69)

def Check_Collisions(ball1 , ball2):
	d = math.sqrt(math.pow(ball1.xcor() - ball2.xcor() , 2) + math.pow(ball1.ycor() - ball2.ycor() , 2))
	r1 = ball1.radius
	r2 = ball2.radius
	if r1 + r2 >= d :
		print("Collisions")


Check_Collisions(ball1 , ball2)
turtle.mainloop()