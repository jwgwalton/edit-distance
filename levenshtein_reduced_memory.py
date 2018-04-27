import numpy as np


def levenshtein_distance(string1, string2):
    """
    Can save on memory by not creating a whole matrix for the distance, only the last two rows
    """

    #  get smallest string to minimize rows
    string1, string2 = (string1, string2) if len(string1) <= len(string2) else (string2, string1)

    n= len(string1)
    m = len(string2)

    if m == 0:
        return n  # if string2 is null then need to insert string1 to match, len(string1) insertions

    if n == 0:
        return m  # the inverse of the previous statement

    # previous row of edit distances, starts as edit distance for empty string1,
    previous_distances = np.zeros(n+1)

    for i in range(n):
        previous_distances[i] = i  # values are number of additions to string1, or deletions from string2

    # more pythonic
    # previous_distances = [x for x in range(length1+1)]

    current_distances = np.zeros(n+1)

    deletion_cost = None
    insertion_cost = None
    substitution_cost = None
    swap = None

    for i in range(m-1):
        # calculate current row distances from the previous row
        current_distances[0] = i + 1

        for j in range(n-1):
            # costs for distance_matrix[i+1][j+1]
            deletion_cost = previous_distances[j+1] + 1
            insertion_cost = current_distances[j] + 1

            if string1[i] == string2[j]:
                substitution_cost = previous_distances[j]
            else:
                substitution_cost = previous_distances[j] + 1

            current_distances[j+1] = min(
                deletion_cost,
                insertion_cost,
                substitution_cost
            )

            swap = previous_distances
            previous_distances = current_distances
            current_distances = swap

    return current_distances[n]
