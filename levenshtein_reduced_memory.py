import numpy as np


def levenshtein_distance(string1, string2):
    """
    Can save on memory by not creating a whole matrix for the distance, only the last two rows
    """

    if len(string1) < len(string2):
        return levenshtein_distance(string2, string1)

    # len(s1) >= len(s2)
    if len(string2) == 0:
        return len(string1)  # if string2 is null then need to insert string1 to match, len(string1) insertions

    # previous row of edit distances, starts as edit distance for empty string1,
    previous_distances = range(len(string2) + 1)

    for i, value in enumerate(string1):
        # calculate current row distances from the previous row
        current_distances = [i + 1]

        for j, value2 in enumerate(string1):
            # costs for distance_matrix[i+1][j+1]
            insertion_cost = previous_distances[j+1] + 1
            deletion_cost = current_distances[j] + 1
            substitution_cost = previous_distances[j] + (value != value2)

            current_distances.append(min(
                deletion_cost,
                insertion_cost,
                substitution_cost
            ))

        previous_distances = current_distances

    return previous_distances[-1]
