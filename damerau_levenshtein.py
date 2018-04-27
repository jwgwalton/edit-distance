import numpy as np
"""
Implementation of the Wagner-Fischer algorithm for calculating Damerau-Levenshtein distance between two strings.

The Damerau-Levenshtein distance between two words is the minimum number of single-character edits
(insertions, deletions, substitutions or transpositions ) required to change one word into the other

This includes transpositions unlike the Levenshtein distance.

This is specifically the optimal string alignment distance which limits that no substring is edited more than once.
This makes this algorithm most valuable when 

TODO: can this algorithm be constructed in the reduced memory format that is possible in the Levenshtein distance.
"""


def damerau_levenshtein_distance(string1, string2):
    m = len(string1)
    n = len(string2)

    if n == 0:
        return m  # if string2 is null then need to insert string1 to match, len(string1) insertions

    if m == 0:
        return n  # the inverse of the previous statment

    # distance_matrix[i,j] contains the levenshtein distance between the first i characters of string1
    # and first j characters of string 2

    # size length + 1 to take into account empty strings,
    # this is needed even with the null check to take into account addition of characters
    distance_matrix = np.zeros((m+1, n+1))

    for i in range(m+1):
        distance_matrix[i, 0] = i  # the distance for any string to empty second string is i number of deletions

    for j in range(n+1):
        distance_matrix[0, j] = j  # As above distance from any string1  to empty string2 would be j delections

    for i in range(1, n+1):
        for j in range(1, m+1):

            if string1[i-1] == string2[j-1]:
                cost = 0
            else:
                cost = 1

            # Need to edit to change characters to match,
            # the different operations correspond to upper triangular entries from current position in matrix
            # minimal operation corresponds to smallest value of these entries
            distance_matrix[i, j] = min(
                distance_matrix[i-1, j] + 1,   # deletion
                distance_matrix[i, j-1] + 1,   # insertion
                distance_matrix[i-1, j-1] + cost,  # substitution
            )

            if i > 2 and j > 2 and string1[i] == string2[j-1] and string1[i-1] == string2[j]:  # could we tranpose them?
                distance_matrix[i, j] = min(
                    distance_matrix[i, j],
                    distance_matrix[i-2, j-2] + cost  # transposition
                )

    return distance_matrix[m, n]  # levenshtein distance is the bottom right value in distance matrix

