import numpy as np
"""
Implementation of the Wagner-Fischer algorithm for calculating Levenstein distance between two strings.

From https://en.wikipedia.org/wiki/Levenshtein_distance
The Levenshtein distance between two words is the minimum number of single-character edits
(insertions, deletions or substitutions) required to change one word into the other
"""


def levenshtein_distance(string1, string2):
    m = len(string1) + 1
    n = len(string2) + 1

    # distance_matrix[i,j] contains the levenshtein distance between the first i characters of string1
    # and first j characters of string 2

    # size length + 1 because that holds if they have
    distance_matrix = np.zeros((m, n))

    for i in range(m):
        distance_matrix[i, 0] = i  # the distance for any string to empty second string is i number of deletions

    for j in range(n):
        distance_matrix[0, j] = j  # As above distance from any string1  to empty string2 would be j delections

    # TODO: Optimised algorithm would exit early on checking for null strings

    for j in range(1, n):
        for i in range(1, m):
            if string1[i-1] == string2[j-1]:
                # same characters so no change needed, levenstein distance is same as at previous character
                distance_matrix[i, j] = distance_matrix[i-1, j-1]
            else:
                # Need to edit to change characters to match,
                # the different operations correspond to upper triangular entries from current position in matrix
                # minimal operation correspons to smallest value of these entries
                distance_matrix[i, j] = min(
                    distance_matrix[i-1, j] + 1,   # deletion
                    distance_matrix[i, j-1] + 1,   # insertion
                    distance_matrix[i-1, j-1] + 1  # substitution
                )

    return distance_matrix[m-1, n-1]  # levenshtein distance is the bottom right value in distance matrix

