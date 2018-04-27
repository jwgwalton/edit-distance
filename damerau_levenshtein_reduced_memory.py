import numpy as np


def damerau_levenshtein_distance(string1, string2):
    """
    Can save on memory by not creating a whole matrix for the distance, only the last two rows
    """

    #  get smallest string to minimize rows
    string1, string2 = (string1, string2) if len(string1) <= len(string2) else (string2, string1)

    n = len(string1)
    m = len(string2)

    if m == 0:
        return n  # if string2 is null then need to insert string1 to match, len(string1) insertions

    if n == 0:
        return m  # the inverse of the previous statement

    # previous row of edit distances, starts as edit distance for empty string1, i.e deletions required to empty string
    previous_distances = [x for x in range(n+1)]

    current_distances = np.zeros(n+1)

    for i in range(m):
        # calculate current row distances from the previous row
        current_distances[0] = i + 1

        #TODO: add the check for the tranpositon being maximal

        for j in range(n):
            # costs for distance_matrix[i+1][j+1]
            deletion_cost = previous_distances[j+1] + 1
            insertion_cost = current_distances[j] + 1

            if string1[j] == string2[i]:
                substitution_cost = previous_distances[j]
            else:
                substitution_cost = previous_distances[j] + 1

            current_distances[j+1] = min(
                deletion_cost,
                insertion_cost,
                substitution_cost
            )

            # Check for transpositon available, need at least 2 characters
            if i > 1 and j > 2:
                if string1[j] == string2[j-1] and string1[j-1] == string2[j]:  # could we tranpose them?
                    current_distances[j] = min(
                        current_distances[j],
                        transposition_distances[j - 2] + 1  # TODO: Does this need to be the substitution cost??
                    )

            transposition_distances = previous_distances
            previous_distances = current_distances
            current_distances = [i+1] + [0] * n

    return current_distances[n]
