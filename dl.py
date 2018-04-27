def levenshtein(s, t):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)

    past_distances = [None] * (len(t) + 1)
    current_distances = [None] * (len(t) + 1)

    for i in range(len(past_distances)):
        past_distances[i] = i

    for i in range(len(s)):
        current_distances[0] = i + 1

        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            insertion_cost = past_distances[j + 1] + 1
            deletion_cost = current_distances[j] + 1
            substitution_cost = past_distances[j] + cost

            current_distances[j + 1] = min(
                deletion_cost,
                insertion_cost,
                substitution_cost
            )


            
        for j in range(len(past_distances)):
            past_distances[j] = current_distances[j]

    return current_distances[len(t)]