import pandas as pd
import utility
from bruteforce import bruteforce_lcs
from recursive import recursive_lcs
from memoization import memoization_recursive_lcs
from bottomup import bottomup_lcs

# list of algorithms to test
algorithms = [bruteforce_lcs, recursive_lcs, memoization_recursive_lcs, bottomup_lcs]
algo_names = ["Brute Force", "Recursive", "Memoization", "Bottom-Up", "Best Recursive", "Worst Recursive"]

# test area 1 : BRUTEFORCE AND RECURSIVE

# choosing the min and max length of our test strings
strings_min_length = 0
strings_max_length = 16

# Generate two lists of strings from min to max length for l1 and l2
l1 = utility.listofstrings(strings_min_length, strings_max_length)
l2 = utility.listofstrings(strings_min_length, strings_max_length)

print(l1)  # TO REMOVE FOR EXAM
print(l2)

# testing Brute Force and Recursive within the selected range
time_results1 = utility.test_algorithms(algorithms[:2], algo_names[:2], l1, l2)

# test area 2 : MEMOIZATION AND BOTTOM UP

strings_min_length = 17
strings_max_length = 250

l1 += utility.listofstrings(strings_min_length, strings_max_length)
l2 += utility.listofstrings(strings_min_length, strings_max_length)

print(l1)  # TO REMOVE FOR EXAM
print(l2)

# testing Memoization and Bottom Up with a larger range
time_results2 = utility.test_algorithms(algorithms[2:], algo_names[2:4], l1, l2)

# test area 3 : WORST AND BEST CASE FOR RECURSIVE

l1 = l2 = utility.bestcase_strings(17)

singlelist = [algorithms[1]]
namesinglelist = [algo_names[4]]

time_results3 = utility.test_algorithms(singlelist, namesinglelist, l1, l2)

l1, l2 = utility.worstcase_strings(16)

singlelist = [algorithms[1]]
namesinglelist = [algo_names[5]]

time_results4 = utility.test_algorithms(singlelist, namesinglelist, l1, l2)

# combining the two results in a single dictionary to export
final_results = {**time_results1, **time_results2, **time_results3, **time_results4}

# Create a list of (algorithm name, LCS length, execution time) tuples
result_tuples = [(name, result[0], result[1]) for (name, _), result in final_results.items()]

# Convert the list of tuples to a DataFrame
columns = ["Algorithm", "LCS Length", "Execution Time"]
df_results = pd.DataFrame(result_tuples, columns=columns)

# Export the DataFrame to an Excel file
file_path = "C:/Users/acgib/Desktop/univ/algorithms laboratory/ALL_ALGORITHMS_TEST.xlsx"
df_results.to_excel(file_path, index=False, header=True)