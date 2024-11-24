#!/bin/python3

# Composite trapozid rule

def f(x):
    y=x**2
    return y


a=1             #starting value(lower limit of integral)
b=2             #ending value(upper limit of integral)

n=200           #number of intervals
h=(b-a)/n       #width of each interval

l=0             #intial value of sum

for i in range(n):
    p=a+i*h

    s=(h/2)*(f(p+h)+f(p))

    l=l+s

print(l)
