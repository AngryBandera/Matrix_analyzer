"""
Discrete Mathematics Relations Lab presentation file.
"""

from matrix_relations import read_file, write_to_file, find_reflexive_closure, \
    find_symmetrical_closure, find_transitive_closure, is_reflexive, \
    is_symmetrical, is_transitive, split_into_classes


if __name__ == "__main__":
    # Define file names
    INPUT_FILE = 'matrix.csv'
    OUTPUT_FILES = {
        "symmetrical_closure" : 'output_relation_symmetrical.csv',
        "reflexive_closure" : 'output_relation_reflexive.csv',
        "transitive_closure" : 'output_relation_transitive.csv'
    }

    outs = []

    # 1. Read the matrix from a file
    print(f"Reading matrix from '{INPUT_FILE}'...")
    matrix = read_file(INPUT_FILE)

    if matrix is None:
        print(f"Error: Could not read the file '{INPUT_FILE}'.")
    print(f"Matrix read successfully: {matrix}")
    print()

    # 2. Compute the closures
    reflexive_closure = find_reflexive_closure(matrix)
    outs.append(reflexive_closure)
    print(f"Reflexive closure: {reflexive_closure}")

    symmetrical_closure = find_symmetrical_closure(matrix)
    outs.append(symmetrical_closure)
    print(f"Symmetrical closure: {symmetrical_closure}")

    transitive_closure = find_transitive_closure(matrix)
    outs.append(transitive_closure)
    print(f"Transitive closure: {transitive_closure}")
    print()

    # 3. Check properties of the original matrix
    print("Original Matrix Properties:")
    print(f"Reflexive: {is_reflexive(matrix)}")
    print(f"Symmetrical: {is_symmetrical(matrix)}")
    print(f"Transitive: {is_transitive(matrix)}")
    print()

    # 4. Writing reflexive, symmetrical, and transitive closures to the output file
    i = 0
    for key, value in OUTPUT_FILES.items():
        print(f"Writing closures to '{key}'...")
        write_to_file(outs[i], value)
        print(f"Closures written to '{value}' successfully.")
        print()

    # 5. Checking if the matrix can be split into equivalence classes
    equivalence_matrix = find_transitive_closure(find_reflexive_closure(
                                                find_symmetrical_closure(matrix))
                                                )
    equivalence_classes = split_into_classes(matrix)

    if equivalence_classes is None:
        print("Original matrix is not equivalent. Finding it's equivalent closure...")
        equivalence_matrix = find_transitive_closure(find_reflexive_closure(
                                            find_symmetrical_closure(matrix))
                                            )
        print(f"Equivalent closure: {equivalence_matrix}")
        equivalence_classes = split_into_classes(equivalence_matrix)

    print(f"Equivalence classes found: {equivalence_classes}")
