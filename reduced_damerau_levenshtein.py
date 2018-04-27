def damerau_levenshtein(s1, s2):
    if len(s1) < len(s2):
        return damerau_levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row[j] = min(insertions, deletions, substitutions))

            if 1 < i <= j: # neeed at least two characters for transposition
                if s1[j-1] == s2[j-2] and s2[j-1] == s1[j-2]: # do the characters match?
                    current_row[j] = min(current_row[j],
            )
        previous_row = current_row

    return previous_row[-1]