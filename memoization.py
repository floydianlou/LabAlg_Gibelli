# recursive algorithm with memoization

def memoization_recursive_lcs(X, Y):
    table = {}

    def memoization_procedure(i, j):
        if (i, j) in table:
            return table[(i, j)]

        if i == 0 or j == 0:
            result = 0
        elif X[i - 1] == Y[j - 1]:
            result = memoization_procedure(i - 1, j - 1) + 1
        else:
            maxlcs1 = memoization_procedure(i - 1, j)
            maxlcs2 = memoization_procedure(i, j - 1)
            result = max(maxlcs1, maxlcs2)

        table[(i, j)] = result
        return result

    return memoization_procedure(len(X), len(Y))
