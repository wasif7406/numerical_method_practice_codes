#!/bin/python3

# Newton Method for non linear equations

# intialized vatiable
h=0.2
y=-2


def f(w,t):
    """The function is returning value of f(y,t) in y'=f(y,t)"""
    z=(w**2+w)/t
    return z


t0=1

#number of iterations
r=10

for i in range(0,r+1):
    
    p=y
    
    #calculation
    t=t0+h*i
    
    k1=h*f(y,t)
        
    d=y+(h/2)*k1
    n=t+(h/2)
    
    
    
    k2 = h*f(d,n)
    
    e=y-h*k1+2*h*k2
    
    k3=h*f(e,n)
    
    y = y+(1/6)*(k1+4*k2+k3)
    
    #displaying result
    print(f"Result\n{y}")
    
    #error calculation
    err =abs(y-p)
    
    #displaying error
    print(f"Errors\n{err}")

