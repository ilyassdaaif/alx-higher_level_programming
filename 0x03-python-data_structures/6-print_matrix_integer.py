#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submatrix in matrix:
        if len(submatrix) == 0:
            print()
        for i in range(len(submatrix)):
<<<<<<< HEAD
            print("{:d}".format(submatrix[i]),
                    end="\n" if i is len(submatrix) - 1 else " ")
=======
            print("{:d}".format(submatrix[i]), end=" " if i < len(submatrix) - 1 else "\n")
>>>>>>> 604a861dd7c81f29b761e5bd52436fe91b6b0ef8
