import numpy as np
from sicpy.optimize import linear_sum_assignment
cost_matrix = np.array([[6,13,3,11,15],
                       [4,2,7,1,10],
                       [8,11,10,7,11],
                       [16,19,12,23,21],
                       [9,5,7,6,10]])
row_ind,col_ind = linear_sum_assignment(cost_matrix)
opt_ass = col_ind
tc = cost_matrix[row_ind,col_ind].sum()