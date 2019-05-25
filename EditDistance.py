
def levenstein(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1
    distance = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        distance[i][0] = i

    for i in range(1, cols):
        distance[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if word1[row - 1] == word2[col - 1]:
                cost = 0
            else:
                cost = 1
            distance[row][col] = min(distance[row -1][col] + 1,      # deletion
                                 distance[row][col -1] + 1,          # insertion
                                 distance[row -1][col -1] + cost)    # substitution

    return distance[rows-1][cols-1]



