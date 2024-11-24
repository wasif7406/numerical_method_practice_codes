#!/bin/python3

# Newton Method for non linear equations

# intialized vatiable
h=0.2
y=0

t0=1

#number of iterations
r=10

for i in range(0,r+1):
    p=y
    #calculation
    t=t0+h*i
    f=1+y/t+(y/t)**2
    d=y+h*f
    n=t0+h*(i+1)
    m = 1+d/n+(d/n)**2
    y = y+(h/2)*(f+m)
    #displaying result
    print(f"Result\n{y}")
    #error calculation
    err =abs(y-p)
    #displaying error
    print(f"Errors\n{err}")
