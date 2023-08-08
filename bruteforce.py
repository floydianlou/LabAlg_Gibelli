# function to calculate and save all subsequences
def all_subsequences(string):
    lists = []
    n = len(string)
    for i in range(1, 2 ** n):
        subseq = [string[j] for j in range(n) if (i & (1 << j)) > 0]
        lists.append(subseq)
    return lists

# bruteforce algorithm
def bruteforce_lcs(X, Y):
    if len(X) == 0 or len(Y) == 0:
        return 0

    subX = all_subsequences(X)
    subY = all_subsequences(Y)

    longest = ''
    for i in range(len(subX)):
        for j in range(len(subY)):
            if subX[i] == subY[j]:
                if len(subX[i]) > len(longest):
                    longest = subX[i]

    return len(longest)

