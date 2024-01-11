#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][item]), end=endspace)
            print()
<<<<<<< HEAD
<<<<<<< HEAD

=======
        for i in range(len(submatrix)):
            print("{:d}".format(submatrix[i]),
                    end="\n" if i is len(submatrix) - 1 else " ")
>>>>>>> 3edcae50c63441019cc3994286d6bd70a944d933
=======
>>>>>>> 0629beae1d4ef38b1bfe300c916c412ef90f4845
