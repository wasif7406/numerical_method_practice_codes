#!/bin/python3
#Power Method to compute dominant EigenValue
# Power method
import numpy as np


def Power_Method(A,n,x):
    """This function computes eigenvalue and eigenvector of matrices using power method."""
    #error matrix intialized
    err_mat = np.zeros((len(A),1))


    for j in range(n):
        #defined so as to calculate error
        x_previous=np.copy(x)

        # solving equations iteratively 
        b=np.matmul(A,x)
        x= b/max(b)

        # displying x matrix in command window
        print(f"The EigenValue after {j+1} iterations is \n{max(b)}")
        print(f"The Eigenvector after {j+1} iterations is \n{x}")

        #error calculation
        for i in range(len(A)):
            err_mat[i] =abs((x[i]-x_previous[i]))

        #displaying error
        print(f"The difference of eigenvectors between {j+1} and {j} iteration is \n{err_mat}")
    return max(b)

def main():
    """This is a main function."""

    # Matrix A
    A = np.array([[-4,14,0],[-5,13,0],[-1,0,2]])
    #intial value of matrix x
    x = np.ones((len(A),1))

    #number of iternations 
    n = 12;

    Power_Method(A,12,x)

if __name__=='__main__':
    main()
