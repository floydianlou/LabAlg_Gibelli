def bottomup_lcs(X, Y):
    lenX = len(X)
    lenY = len(Y)

    # creates a table to store the prefixes' LCSes
    table = [[0] * (lenY + 1) for _ in range(lenX + 1)]

    for i in range(1, lenX+1):
        for j in range(1, lenY+1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # at the bottom of the table we get our LCS length
    return table[lenX][lenY]

