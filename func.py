"""
    Version 1:
    This module has functions to calculate 3x3 and 2x2 matrix operations.
    This module calculates the determinant of a 3x3 and a 2x2 matrix.
    This module calculates the adjugate of a 3x3 matrix.
    This module calculates the inverse of a 3x3 matrix.
    This module calculates the cofactors matrix. It is in the format of a list.
    It is still work in progress. It does not correct erroneous inputs yet.
"""
__author__ = "Amadeo Estrada"
__date__ = "15 / Jul / 2020"


def signs3x3(a):
    """ 'a' is a 3x3 matrix. The return of this function is a 3x3 'a' matrix multiplied
        by a 3x3 sign matrix
    """
    import numpy as np  # import numpy modules
    ones = np.ones((1, 9), np.float32)  # declare a 'ones' 1x9 matrix
    for i in range(ones.size):  # for each of the 9 elements...
        if ((i + 1) % 2) == 0: ones[0][i] *= -1  # if index is even, assign a negative
    ones = ones.reshape((3, 3))  # reshape as a 3x3 matrix
    ones = a * ones  # multiply parameter 'a' times 'ones' sign matrix
    return ones


def determ2x2(a):
    """ 'a' is a 2x2 matrix. The return of this function is the determinant of a
        2x2 'a' matrix
        """
    det = a[0][0] * a[1][1]  # determinant calculation
    det -= a[1][0] * a[0][1]  # determinant calculation
    return det


def determ3x3(a):
    """ 'a' is a 3x3 matrix. The return of this function is the determinant of a
        3x3 'a' matrix. The function determ2x2 is called recursively
        """
    import numpy as np  # multiply parameter 'a' times 'ones' sign matrix
    det = 0  # create a determinant integer
    for j in range(3):  # iterate another 3 times
        b = a.copy()  # make a copy of the 'a' parameter
        c = np.delete(b, 0, 0)  # delete the 'i' column
        c = np.delete(c, j, 1)  # delete the '0' row
        if (j % 2) == 0:
            x = 1
        else:
            x = -1
        det += a[0][j] * determ2x2(c) * x  # multiply times anchor
    return det


def cho3x3(a):
    """ 'a' is a 3x3 matrix. The return of this function is the cofactor LIST of
        2x2 'a' matrices.
        """
    import numpy as np  # import numpy module
    L = []              # create an empty list
    for i in range(3):  # iterate 3 times
        L.append([])  # create a new list on each iteration
        for j in range(3):  # iterate another 3 times
            b = a.copy()  # make a copy of the 'a' parameter
            c = np.delete(b, i, 0)  # delete the 'i' column
            c = np.delete(c, j, 1)  # delete the 'j' row
            L[i].append(c)  # append the resulting object
    return L


def someadj(a):
    """ 'a' is a 3x3 matrix. The return of this function is the adjugate matrix of a
        3x3 'a' matrix. This functions uses the functions: cho3x3, determ2x2 and signs
    """
    import numpy as np
    mat3x3 = np.zeros((3, 3), np.float32)           # Define a zeroes 3x3 matrix
    L = cho3x3(a)                                   # Get a cofactors list of 'a'
    for i in range(len(L)):                         # For each of the list's rows
        for j in range(len(L[i])):                  # For each of the list's columns
            mat3x3[i][j] = determ2x2(L[i][j])       # Calculate the determinant of each cof.
    mat3x3 = signs3x3(mat3x3)                       # Apply signs matrix
    mat3x3 = mat3x3.T                               # Transpose
    return mat3x3


def inversed(a):
    """ 'a' is a 3x3 matrix. The return of this function is the inverse matrix of a
        3x3 'a' matrix. This function uses: determ3x3 and someadj functions
    """
    adj = someadj(a)                # Calculate the adjugate matrix of 'a'
    det_inv = 1 / determ3x3(a)      # Get the inverse determinant of 'a'
    inv = det_inv * adj             # Calculate the inverse matrix
    return inv
