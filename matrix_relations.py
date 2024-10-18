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

def relation_to_str(matrix: list[list]) -> str:
    '''
    Function which dumps matrix into string
    
    :param matrix: matrix we need to dump (list[list]).
    :return: dumped into string matrix (str)
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

# def find_transitive_closure(matrix: List[List[int]])-> List[List[int]]:
#     """
#     List[List[int]] -> List[List[int]]
#     Finds reflexive closure of {matrix}
#     """
#     pass


# def split_into_classes(matrix: List[List[int]])-> List[List[int]]:
#     """
#     List[List[int]] -> List[List[int]]
#     Splits relation into equivalence classes
#     >>> split_into_classes([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
#     [[0, 1, 2], [3]]
#     """
#     pass

# def is_transitive(matrix: list[list])-> bool:
#     """
#     list[list] -> bool
#     Check if given relation is transitive. Returns True if yes and False if no
#     >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
#     True
#     >>> is_transitive([[0,1,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
#     False
#     """
#     pass

# def find_transitive_number(number: int)-> int:
#     """
#     int -> int
#     Return how many transitive relations are there on relation with n elements.
#     (number<=4)
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
