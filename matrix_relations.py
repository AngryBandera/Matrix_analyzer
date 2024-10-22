"""
Discrete maths relations lab
"""
import doctest

def read_file(filename: str) -> list[list[int]] | None:
    """
    Reads a matrix from a file and transforms it into a list of lists (matrix).
    Function opens file, reads its content and transforms each line into list of integers.
    File should conatain only 0 and 1.
    
    Args:
        filename (str): The name of the file containing the matrix.
    
    Returns:
        list[list[int]]: The matrix represented as a list of lists of integers.
        None if the file cannot be opened or not found.
    Example:
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = "w",delete=False) as tmp:
    ...     _=tmp.write('001\\n011\\n111')
    >>> read_file(tmp.name)
    [[0, 0, 1], [0, 1, 1], [1, 1, 1]]
    """
    try:
        with open(filename, "r", encoding = "utf-8") as file:
            matrix = []
            # Read each line in the file, strip newline characters,\
            # and convert to a list of integers.
            for line in  file.readlines():
                line = line.replace("\n", "")
                # Convert each character in the line to an integer
                column = [int(num) for num in line]
                matrix.append(column)
            return matrix
    except FileNotFoundError:
        return None

def write_to_file(relation: list[list[int]], filename: str) -> None:
    """
    Writes a matrix (relation) to a file. 
    The function takes a matrix represented as a list of lists of integers and writes it to a file.
    
    Args:
        relation (list[list[int]]): The matrix to write.
        filename (str): The file where the matrix will be written.
    Returns:
        None
    Example:
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
    """
    Converts a matrix to a string for file storage or display.
    
    Args:
        matrix (list[list[int]]): The matrix to convert.
    
    Returns:
        str: The string representation of the matrix, with rows joined by newline.
    """
    # Convert each row to a string, join them with newlines
    return '\n'.join([''.join(map(str, row)) for row in matrix])

def find_symmetrical_closure(matrix: list[list[int]])-> list[list[int]]:
    """
    Computes the symmetrical closure of a binary matrix.
    Symmetrical closure means making sure if matrix[i][j] == 1, then matrix[j][i] is also 1.
    
    Args:
        matrix (list[list[int]]): A square binary matrix (i.e., only contains 0s and 1s).
    
    Returns:
        list[list[int]]: The symmetrical closure of the input matrix.
    
    Example:
    >>> find_symmetrical_closure([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

    >>> find_symmetrical_closure([[0, 1], [1, 0]])
    [[0, 1], [1, 0]]
    
    >>> find_symmetrical_closure([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    [[1, 0, 0], [0, 0, 1], [0, 1, 0]]

    >>> find_symmetrical_closure([[0, 0], [0, 0]])
    [[0, 0], [0, 0]]
    """
    matrix = [row[:] for row in matrix] # Creating deep copy of the matrix

    for row, row_value in enumerate(matrix):
        for column, column_value in enumerate(row_value):
            if column_value:
                matrix[column][row] = 1 # Making parallel element symmetrical
    return matrix

def find_reflexive_closure(matrix: list[list[int]])-> list[list[int]]:
    """
    Computes the reflexive closure of a binary matrix.

    Reflexive closure means ensuring that all diagonal elements `matrix[i][i]` are set to 1.
    
    Args:
        matrix (list[list[int]]): A square binary matrix (i.e., only contains 0s and 1s).
    
    Returns:
        list[list[int]]: The reflexive closure of the input matrix.
    
    Example:
    >>> find_reflexive_closure([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    [[1, 1, 0], [0, 1, 1], [1, 0, 1]]

    >>> find_reflexive_closure([[1, 0], [0, 1]])
    [[1, 0], [0, 1]]

    >>> find_reflexive_closure([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    >>> find_reflexive_closure([[1]])
    [[1]]
    """
    matrix = [row[:] for row in matrix] # Creating deep copy of the matrix

    for index, _ in enumerate(matrix):
        matrix[index][index] = 1
    return matrix

def find_transitive_closure(matrix: list[list[int]])-> list[list[int]]:
    """
    Finds the transitive closure of a given relation matrix using the Floyd-Warshall algorithm.
    
    Args:
        matrix (list[list[int]]): The relation matrix.
    
    Returns:
        list[list[int]]: The transitive closure of the matrix.
    
    Example:
    >>> find_transitive_closure([[1,0,1,0],[1,0,0,0],[0,0,0,1],[0,0,1,1]])
    [[1, 0, 1, 1], [1, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]]
    """
    trans_closure = [row[:] for row in matrix] # creating deep copy of the matrix
    n = len(matrix)

    # Applying Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update the matrix using logical OR
                trans_closure[i][j] = trans_closure[i][j] or \
                                (trans_closure[i][k] and trans_closure[k][j])
    return trans_closure

def get_relation_pairs(matrix: list[list[int]]) -> list[tuple[int, int]]:
    """
    Gets all  relation pairs from a binary matrix. 
    
    Args:
        matrix (list[list[int]]): A binary matrix.

    Returns:
        list[tuple[int, int]]: A list of tuples which contains the pairs
        where the matrix has a 1 at matrix[i][j].
    """
    relations = []
    # Iterate over the matrix and extract the pairs (i, j) where matrix[i][j] == 1.
    for row, row_value in enumerate(matrix):
        for column, column_value in enumerate(row_value):
            if column_value:
                relations.append((row, column))
    return relations

def split_into_classes(matrix: list[list[int]]) -> list[list[int]] | None:
    """
    Splits a relation matrix into equivalence classes.
    
    Args:
        matrix (list[list[int]]): The relation matrix.
    
    Returns:
        list[list[int]]: A list of lists where each inner list represents an equivalence class
                        or None if matrix is not relation of equity.
    
    Example:
    >>> split_into_classes([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
    [[0, 1, 2], [3]]
    >>> split_into_classes([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    [[0], [1], [2], [3]]
    """
    if not all([is_reflexive(matrix), is_symmetrical(matrix), is_transitive(matrix)]):
        return None

    relations = get_relation_pairs(matrix)

    n = len(matrix)
    visited_values = [False] * n

    relation_classes = []
    # getting classes from relation
    for value in range(n):

        # checks if this value is already in class
        if visited_values[value]:
            continue

        visited_values[value] = True

        # if value is new, creating it's class
        relation_class = [value]
        for relation in relations:
            if value in relation:
                new_value = relation[(relation.index(value) + 1) % 1]
                if not new_value in relation_class and not visited_values[new_value]:
                    relation_class.append(new_value)
                    visited_values[new_value] = True

        relation_classes.append(relation_class)

    return relation_classes

def is_reflexive(matrix: list[list[int]])-> bool:
    """
    list[list[int]] -> bool
    Checks if relation is reflexive
    >>> is_reflexive([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
    True
    >>> is_reflexive([[1,0,1,1],[0,0,1,0],[1,1,1,0],[0,0,1,1]])
    False
    """

    # checking if values on diagonal is 1
    for index, row in enumerate(matrix):
        if row[index] != 1:
            return False

    return all(matrix[i][i] == 1 for i in range(len(matrix)))

def is_symmetrical(matrix: list[list[int]])-> bool:
    """
    list[list[int]] -> bool
    Checks if relation is reflexive
    >>> is_symmetrical([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
    True
    >>> is_symmetrical([[1,0,1,1],[0,0,1,0],[1,1,1,0],[0,0,1,1]])
    False
    """
    n = len(matrix)
    # checks if matrix[i][j] == matrix[j][i] for all i and j
    return all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n))

def is_transitive(matrix: list[list])-> bool:
    """
    list[list] -> bool
    Check if given relation is transitive. Returns True if yes and False if no
    >>> is_transitive([[0, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [1, 0, 1, 1]])
    True
    >>> is_transitive([[0,1,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])
    False
    """
    return matrix == find_transitive_closure(matrix)

if __name__ == '__main__':
    print(doctest.testmod())
    
