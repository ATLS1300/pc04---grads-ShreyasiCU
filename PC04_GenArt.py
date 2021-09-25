#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 15:17:29 2021

@author: shreyasimandal
"""
from turtle import *
import math

import random
random.randint(1,10)

color("light grey")
begin_fill()
pu()
goto(-185,250)
pd()


for i in range(2):
    forward(300)
    right(90)
    forward(250)
    right(90)
end_fill()


#for "Z"
pu()
goto(-250,250)
pd()

speed(0)

pencolor("red")
for i1 in range(0,10):
    for i2 in range(0,3):
        fd(5)
        rt(360/3)
    pu()
    fd(5)
    pd()
       
for i1 in range(0,20):
    for i2 in range(0,3):
        fd(5)
        rt(360/3)
    pu()
    rt(360/3)
    fd(5)
    lt(360/3)
    pd()

for i1 in range(0,10):
    for i2 in range(0,3):
        fd(5)
        rt(360/3)
    pu()
    fd(5)
    pd()

#For random shape polygon
color("cyan")
begin_fill()
penup()
goto(100, 220)
pendown()
sides=random.randint(3,10)
for a in range(0,sides):
    fd(50)
    rt(360/sides)
end_fill()

#For "O"
pencolor("orange")
pu()
goto(-150,220)
pensize(2)
pd()
speed(2000)



for i1 in range(0,12):
    for i2 in range(0,10):
        fd(6*math.sin(i2))
        rt(360/10)    
        #t2.bk(6)
        #t2.lt(360/10)
    pu()
    rt(360/12)
    fd(5)
    pd()
   

pencolor("green")
pu()
goto(-30,240)
pensize(1)
pd()
for i1 in range(0,36):
    circle(15)        
    pu()
    rt(10)
    fd(5)
    pd()

#Spiraling star
spiral=Turtle()
spiral.pencolor("red")
pu()
goto(220,220)
pensize(1)
pd()



for i in range(30):
    spiral.forward(i * 10)
    spiral.right (144)


# Using two turtles


t1 = Turtle()
t2= Turtle()
t1.up()
t1.goto(200,200)
t2.up()
t2.goto(200,-200)
t1.down()
t2.down()

for j in range(4):
    for i in range(4):
        t1.forward(30)
        t1.right(90)
        t2.forward(30)
        t2.right(90)
    t1.up()
    t2.up()
    t1.forward(50)
    t2.forward(50)
    t1.down()
    t2.down()
    
end_fill()

