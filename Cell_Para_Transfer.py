import numpy as np

A = [[1, 0],[-0.5,(3.0**0.5)*0.5]]  ## Old Vector in (U,V)^T

B = [[2,1],[1,2]]  ## New Vector in (U',V')^T

E = np.matmul(B,np.linalg.inv(A)) ## The target transfer matrix in MS as the parameter of U, V
print E,'\n'
