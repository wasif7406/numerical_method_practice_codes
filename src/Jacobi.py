#!/bin/python3
#Jacobi Method for the solution of system of linear equations
# write system of linear equation as x(n+1)=T*x(n)+c



import numpy as np

#defing Jacobi
def Jacobi(T,c,n,x):
    """This functions calculate solution of system of linear simultaneous equation using Jacobi iterative technique for input values of T, c and number of iterations"""

    #intializing error matrix 
    err_mat = np.zeros((len(T),1))

    for j in range(n):

        #defined so as to calculate error
        x_previous = x

        # solving equations  
        x = np.matmul(T,x)+c

        #displying x matrix in command window
        print(f"Solution of System of Equation after {j+1} iterations is:\n{x}")

        #error calculation

        for i in range(len(T)):
            err_mat[i,:] =abs((x[i]-x_previous[i]))
        print(f"Difference between {j+1} and {j} iteration is:\n{err_mat}")
    return x

def main():
    """This is main function"""
    #T matrix
    T=np.array([[0,1/10,-1/5,0],[1/11,0,1/11,-3/11],[-1/5,1/10,0,1/10],[0,-3/8,1/8,0]])

    # c matrix
    c =np.array([[3/5],[25/11],[-11/10],[15/8]])


    #number of iternations 
    n = 10

    # number of rows of T matrix

    #intial value of matrix x
    x = np.zeros((len(T),1))

    print(f"The Solution of System after {n} iterations is \n{Jacobi(T,c,n,x)}")
    return None

if __name__=='__main__':
    main()
