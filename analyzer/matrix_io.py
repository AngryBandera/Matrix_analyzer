'''
This module manages writing and reading matrix from csv file
'''

def read_matrix(path: str) -> list[list] | None:
    '''
    Function which reads csv file and parses it into matrix
    
    :param path: path to the operated file (str).
    :return: n x n dimension matrix (list[list]) or None if file is not found.
    '''

    try:
        with open(path, "r", encoding = "utf-8") as file:
            matrix = []

            line = file.readline()
            while line != "":
                column = []

                for element in line[:-1]:
                    if element != "\n":
                        column.append(int(element))

                matrix.append(column)
                line = file.readline()
            return matrix
    except FileNotFoundError:
        return None


def write_matrix(path: str, matrix: list[list]) -> bool:
    '''
    Function which reads csv file and parses it into matrix
    
    :param path: path to the operated file (str).
    :param matrix: matrix we need to write (list[list]).
    :return: True if successful, False if not (bool) 
    '''

    with open(path, "w", encoding = "utf-8") as file:
        file.write(matrix_to_str(matrix))

    return True


def matrix_to_str(matrix: list[list]) -> str:
    '''
    Function which dumps matrix into string
    
    :param matrix: matrix we need to dump (list[list]).
    :return: dumped into string matrix (str)
    '''
    return ''.join([''.join(map(str, row)) + "\n" for row in matrix])

if __name__ == "__main__":
    # print(matrix_to_str([[0,0,0,0], [1,1,1,1]]))
    # print(write_matrix("matrix.csv", [[0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 0, 1, 0]]))
    # print(read_matrix("matrix.csv"))
    pass