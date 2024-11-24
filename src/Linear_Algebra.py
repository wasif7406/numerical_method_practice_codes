#!/bin/python3

#This Mosule is for certain linear algebra manipulation

import numpy as np

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




def Gauss_Seidel(T,c,n,x):
    """This function Solves System of Linear Simultaneous Equations Using Gauss Seidel Method for the input values of T ,c , number of iterartions and starting iteration"""

    #error matrix intialized
    err_mat = np.zeros((len(T),1))

    for j in range(n):
        #defined so as to calculate error
        p=np.copy(x)

        # solving equations iteratively 
        for i in range(len(T)):
            x[i] = np.matmul(T[i],x)+c[i]

        # displying x matrix in command window
        print(f"Solution of System of Equation after {j+1} iterations is:\n{x}")

        #error calculation
        for i in range(len(T)):
            err_mat=abs(x-p)

        #displaying error
        print(f"Difference between {j+1} and {j} iteration is:\n{err_mat}")
    return x




def Power_Method(A,n,x):
    """This function computes eigenvalue and eigenvector of matrices using power method."""
    #error matrix intialized
    err_mat = np.zeros((len(A),1))


    for j in range(n):
        #defined so as to calculate error
        x_previous=np.copy(x)

        # solving equations iteratively 
        b=np.matmul(A,x)
        print(b)
        x= b/max(b,key=abs)

        # displying x matrix in command window
        print(f"The EigenValue after {j+1} iterations is \n{max(b,key=abs)}")
        print(f"The Eigenvector after {j+1} iterations is \n{x}")

        #error calculation
        for i in range(len(A)):
            err_mat[i] =abs((x[i]-x_previous[i]))

        #displaying error
        print(f"The difference of eigenvectors between {j+1} and {j} iteration is \n{err_mat}")
    return max(b,key=abs),x




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
    x = np.ones((len(T),1))

    (eigenvalue,eigenvector) = Power_Method(T,n,x)

    print(f"The Solution of System after {n} iterations is \n{Jacobi(T,c,n,x)}")
    print(f"The Solution of System after {n} iterations is \n{Gauss_Seidel(T,c,n,x)}")
    print(f"The Eigenvalue after {n} iteration is \n{eigenvalue} \n and corresponding Eigenvector is\n{eigenvector}")
    return None

if __name__=='__main__':
    main()
