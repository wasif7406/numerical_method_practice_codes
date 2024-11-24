#!/bin/python3

# Newton Method for non linear equations

# intialized vatiable
h=0.25
y=2


def f(w,t):
    """The function is returning value of f(y,t) in y'=f(y,t)"""
    z=1+(w/t)
    return z

t0=1

#number of iterations
r=4

for i in range(0,r+1):
    
    p=y
    
    #calculation
    t=t0+h*i
    
    k1=h*f(y,t)
    
    
    d=y+k1/2
    n=t+(h/2)
    
    
    
    k2 = h*f(d,n)
    
    
    e=y+k2/2
    
    k3=h*f(e,n)
    
    
    g=y+k3
    l=t+h
    
    k4=h*f(g,l)
    
    
    y = y+(1/6)*(k1+2*k2+2*k3+k4)
    
    #displaying result
    print(f"Result\n{y}")
    
    #error calculation
    err =abs(y-p)
    
    #displaying error
    print(f"Errors\n{err}")

