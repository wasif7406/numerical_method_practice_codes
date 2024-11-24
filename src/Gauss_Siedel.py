#!/bin/python3

#Solution of System of Linear Simultaneous Equations Using Gauss Seidel Method 
# Gauss Siedel Method
import numpy as np



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

def main():
    """This is main function"""
    #T matrix
    T = np.array([[0,0.25,0.25,0],[0.25,0,0,0.25],[0.25,0,0,0.25],[0,0.25,0.25,0]])
    # c matrix
    c = np.array([[50],[50],[25],[25]])

    #intial value of matrix x
    x = np.array([[87.891],[87.695],[62.695],[62.598]])

    #number of iternations 
    n = 9

    print(f"The Solution of System after {n} iterations is \n{Gauss_Seidel(T,c,n,x)}")
    return None

if __name__=='__main__':
    main()
