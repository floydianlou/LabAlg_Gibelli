# recursive algorithm
def recursive_lcs(X, Y):
    if not X or not Y:
        return 0

    if X[-1] == Y[-1]:
        return 1 + recursive_lcs(X[:-1], Y[:-1])
    else:
        return max(recursive_lcs(X, Y[:-1]), recursive_lcs(X[:-1], Y))
