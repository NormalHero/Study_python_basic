#TurtleTest.py
import turtle as t

'''
t.speed(1)
t.pensize(10)
t.color("red")
t.forward(100)
t.left(90)
t.color("yellow")
t.forward(100)
t.left(90)
t.color("blue")
t.forward(100)
t.left(90)
t.color("green")
t.forward(100)
t.left(90)
'''
import random as r
t.speed(1)
t.color("green")
t.pensize(10)
t.shape("turtle")
t.penup()
while True:
    go = r.randrange(20,51)
    angle = r.randrange(30,71)
    lr = r.randrange(0,2)

    if lr == 0:
        t.forward(go)
        t.left(angle)
    else:
        t.forward(go)
        t.right(angle)
    





















