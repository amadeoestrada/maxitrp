import numpy as np
import func

# Declare arrays
#a = np.array([[1, 0, 2], [0, 3, 0], [4, 0, 5]])
a = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])

# Utilize functions
adj = func.someadj(a)
det = func.determ3x3(a)
inv = func.inversed(a)

# Print results
print('Original matrix: \n', a, '\n\n')
print('Determinant of original matrix: ', det, '\n\n')
print('Adjugate matrix: \n', adj, '\n\n')
print('Inversed matrix: \n', inv, '\n\n')
