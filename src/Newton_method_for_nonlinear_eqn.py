#!/bin/python3

# Newton Method for non linear equations
import numpy as np
import sympy as sym
from sympy.abc import x,y,z

#intializing the answer matrix
answer_matrix = np.array([1,4,5])

# number of rows of x matrix
matrix_rows = len(answer_matrix)

#error matrix intialized
err_mat = np.zeros((matrix_rows,1))



#syms  x y z function w
symbolix_variable = sym.Matrix([x, y, z])

function = [0,0,0]

#define functions

function[0] = x+y+z
function[1] = x**2+y**2+z**2
function[2] = x**3+y**3+z**3
#function[0] = y-2*x+2-0.125*x**3+0.375*x+0.125*(1.25)**3
#function[1] = z-2*y+x-0.125*y**3+0.375*y+0.125*(1.5)**3
#function[2] = 2.5-2*z+y-0.125*z**3+0.375*z+0.125*(1.75)**3
#


#F function matrix
function_matrix = sym.lambdify(symbolix_variable,function)
print(f"The function matricx is \n{function_matrix(x,y,z)}")

#Jacobian
Jacobian_symbolic = sym.Matrix(function).jacobian(symbolix_variable)
print(f"The Jacbian Matrix is \n{Jacobian_symbolic}")
Jacobian = sym.lambdify(symbolix_variable, Jacobian_symbolic)


#number of iternations
iteration_number =9

def Jacobian_matrix(function,evaluation_array):
    jacobian_rows=len(function)
    diff=np.zeros((jacobian_rows,1))
    for j in range(jacobian_rows):
        diff
        diff_array=1*10**-8*diff[j,1]
        J[:,j]=(function(evaluation_array+diff_array)-function(evaluation_array-diff_array))/(2*diff)

def newton_method(Jacobian,function_matrix,answer_matrix,iteration_number):
    for i in range(0,iteration_number):
        #answer matrix of previous iteration
        answer_matrix_previous_iteration = np.copy(answer_matrix)

        #Numerical Value of Jacobian for this Iteration
        jacobian_numerical=Jacobian(*answer_matrix.transpose())
        print(f"The Value of jacobian is \n{jacobian_numerical}")

        #Numerical Value of function matrix for this Iteration
        funtion_numerical = function_matrix(*answer_matrix. transpose())
        print(f"The Value of function matrix is \n{funtion_numerical}")

        #iterative eqation
        answer_matrix = answer_matrix - np.matmul(np.linalg.inv(jacobian_numerical), funtion_numerical)
        print(f"Result is \n{answer_matrix}")

        #error calculation
        for j in range(0,matrix_rows):
            err_mat[j] =abs(answer_matrix[j]-answer_matrix_previous_iteration[j])

        print(f"Errors Matrix is \n{err_mat}")

newton_method(Jacobian,function_matrix,answer_matrix,iteration_number)
