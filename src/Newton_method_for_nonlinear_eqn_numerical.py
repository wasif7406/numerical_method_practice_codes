#!/bin/python3


# Newton Method for non linear equations
import numpy as np

def Jacobian_matrix(function_mat, X, x_diff=1*10**-4):
    """This function calculates numerical value of Jacobian given array of function matrix and the coordinates where jacobian is to be evaluated. One can also specify difference in the coordinate we are take derivative with respect to."""
    #length of rows or column of jacobian matrix
    jacobian_rows = len(X)
    #intializing jacobian matrix
    Jacobian = np.zeros((jacobian_rows, jacobian_rows))

    for j in range(jacobian_rows):
        #intializing difference matrix it is then used to calculate x k+1 and x k-1
        diff_array = np.zeros(jacobian_rows)
        diff_array[j] = x_diff

        #x k+1
        #print(X)
        x_plus_1 = X+diff_array
        #print(x_plus_1)

        #x k-1
        x_minus_1 = X-diff_array
        #print(x_minus_1)
        #print(j)
        #Calculating jacobian matrix column
        Jacobian[:, j] = (function_mat(x_plus_1) -
                          function_mat(x_minus_1))/(2*x_diff)

        #np.save('Jacobian.result', Jacobian)

    #print(Jacobian)

    return Jacobian


#print(Jacobian_matrix(function_matrix, answer_matrix, 1*10**-4))


def newton_method(Jacobian, function, answer_matrix, iteration_number, x_diff=1*10**-4):
    """This function solves system of nonlinear equations using newton method"""
    #error matrix intialized
    #print(f"iteration_number={iteration_number}")
    err_mat = np.zeros(len(answer_matrix))
    for i in range(iteration_number):
        #print(f"i={i}")
        #answer matrix of previous iteration this is stored to calculate error between two iterations
        answer_matrix_previous_iteration = np.copy(answer_matrix)

        #Numerical Value of Jacobian for this Iteration
        jacobian_numerical = Jacobian(function, answer_matrix, x_diff)
        print(f"The Value of jacobian is \n{jacobian_numerical}")

        #Numerical Value of function matrix for this Iteration
        funtion_numerical = function(answer_matrix)
        print(f"The Value of function matrix is \n{funtion_numerical}")

        #iterative equation
        answer_matrix = answer_matrix - \
            np.linalg.solve(jacobian_numerical, funtion_numerical)
        print(f"Result is \n{answer_matrix}")

        #error calculation
        for j in range(len(answer_matrix)):
            err_mat[j] = abs(answer_matrix[j] -
                             answer_matrix_previous_iteration[j])

        print(f"Errors Matrix is \n{err_mat}")

    return answer_matrix


if __name__ == "__main__":
    #intializing the answer matrix
    answer_matrix = np.linspace(0,3)


    #number of iternations
    iteration_number = 9


    def function_matrix(X):
        x = X[0]
        y = X[1]
        z = X[2]

        len_fun_mat = len(X)
        function = np.zeros(len_fun_mat)

        #define functions
        function[0] = x+y+z
        function[1] = x**2+y**2+z**2
        function[2] = x**3+y**3+z**3

        return function

    print(Jacobian_matrix(function_matrix,answer_matrix))

    #newton_method(Jacobian_matrix, function_matrix,answer_matrix, iteration_number, 1*10**-8)
