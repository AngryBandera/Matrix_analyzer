"""
Discrete maths relations lab
"""
import doctest
from typing import List

def read_file(filename: str) -> List[List[int]]:
    """
    str -> list[list]
    Reads matrix from with name {filename} file and transforms it into a list of lists
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...     _=tmp.write('001\\n011\\n111')
    >>> read_file(tmp.name)
    [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    """
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            matrix = []

            for line in  file.readlines():
                line = line.replace("\n", "")
                column = [int(num) for num in line]
                matrix.append(column)
            return matrix
    except FileNotFoundError:
        return None

def write_to_file(relation: List[List[int]], filename: str) -> None:
    """
    List[List[int]], str -> None
    Creates a file with input from {matrix}
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...     _=tmp.write('')
    >>> write_to_file([[0,1,0,0],[1,1,1,1],[1,0,0,0],[1,1,1,1]],tmp.name)
    >>> with open(tmp.name,"r",encoding="utf-8") as file:
    ...     print(file.read())
    0100
    1111
    1000
    1111
    """
    with open(filename, "w", encoding = "utf-8") as file:
        file.write(relation_to_str(relation))

def relation_to_str(matrix: list[list[int]]) -> str:
    '''
    List[list] - > str
    Function which dumps matrix into string

    '''
    return '\n'.join([''.join(map(str, row)) for row in matrix])

# def find_symmetrical_closure(matrix: List[List[int]])-> List[List[int]]:
#     """
#     List[List[int]] -> List[List[int]]
#     Finds symmetrical closure of {matrix}
#     """
#     pass

# def find_reflexive_closure(matrix: List[List[int]])-> List[List[int]]:
#     """
#     List[List[int]] -> List[List[int]]
#     Finds reflective closure of {matrix}
#     """
#     pass

def find_transitive_closure(matrix: List[List[int]])-> List[List[int]]:
    """
    List[List[int]] -> List[List[int]]
    Finds reflexive closure of {matrix}

    >>> find_transitive_closure([[1,0,1,0],[1,0,0,0],[0,0,0,1],[0,0,1,1]])
    [[1, 0, 1, 1], [1, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
    """
    matrix_trans = matrix.copy()
    n = len(matrix)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix_trans[i][j] = matrix_trans[i][j] or \
                                (matrix_trans[i][k] and matrix_trans[k][j])
    return matrix_trans

# def split_into_classes(matrix: List[List[int]])-> List[List[int]]:
#     """
#     List[List[int]] -> List[List[int]]
#     Splits relation into equivalence classes
#     >>> split_into_classes([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
#     [[0, 1, 2], [3]]
#     """
#     # if is_transitive(matrix)


def is_reflexive(matrix: List[List[int]])-> bool:
    """
    List[List[int]] -> bool
    Checks if relation is reflexive
    >>> is_reflexive([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
    True
    >>> is_reflexive([[1,0,1,1],[0,0,1,0],[1,1,1,0],[0,0,1,1]])
    False
    """

    for index, row in enumerate(matrix):
        if row[index] != 1:
            return False

    return True

# def is_symmetrical(matrix: List[List[int]])-> bool:
#     """
#     List[List[int]] -> bool
#     Checks if relation is reflexive
#     >>> is_symmetrical([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
#     True
#     >>> is_symmetrical([[1,0,1,1],[0,0,1,0],[1,1,1,0],[0,0,1,1]])
#     False
#     """

#     for row in matrix:
#         for column in row:
#             if matrix[row][column] != matrix[column][row]:
#                 return False

#     return True

def is_transitive(matrix: list[list])-> bool:
    """
    list[list] -> bool
    Check if given relation is transitive. Returns True if yes and False if no
    >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[0,1,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
    False
    """
    lenth = len(matrix[0])
    result = [[0 for _ in range(lenth)] for _ in range(lenth)]

    # Perform matrix multiplication
    for i in range(lenth):
        for j in range(lenth):
            for k in range(lenth):
                result[i][j] = matrix[i][k] and matrix[k][j]

    return result == matrix

# def find_transitive_number(number: int)-> int:
#     """
#     int -> int
#     Return how many transitive relations are there on relation with n elements.
#     >>> find_transitive_number(0)
#     1
#     >>> find_transitive_number(2)
#     13
#     >>> find_transitive_number(3)
#     171
#     """
#     pass

if __name__ == '__main__':
    print(doctest.testmod())
