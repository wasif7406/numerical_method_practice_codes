#!/bin/python3


# Euler Method for first order differential equtations


# The solution is valid for equ of type y'=f(y,t)
def f(y,t):
    """The function is returning value of f(y,t) """
    z=y-t**2+1
    return z


#defining h (size or width of change in x)
h=0.2

#intializing w as in(   w(i+1) -w(i)   )
w=0.5
#intial value of time
t0=0
#final value of time
tf=2

#number of iterations
n=int((tf-t0)/h)

for i in range(n):
    p=w
    #iterating equation
    t=t0+h*i
    w=w+h*f(w,t)
    #displaying result
    print(f'Result\n {w}')
    #error calculation
    err =abs(w-p)
    #displaying error
    print(f'Errors\n {err}')
