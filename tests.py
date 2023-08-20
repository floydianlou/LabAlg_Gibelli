import pandas as pd
import utility
from algorithmclass import LCSalgorithm
from bruteforce import bruteforce_lcs
from recursive import recursive_lcs
from memoization import memoization_recursive_lcs
from bottomup import bottomup_lcs

algorithms = [LCSalgorithm('BruteForce', 16, utility.generate_random_string, bruteforce_lcs),
              LCSalgorithm('Recursive Mid Case', 16, utility.generate_random_string, recursive_lcs),
              LCSalgorithm('Memoization', 250, utility.generate_random_string, memoization_recursive_lcs),
              LCSalgorithm('BottomUp', 250, utility.generate_random_string, bottomup_lcs),
              LCSalgorithm('Recursive Best Case', 16, utility.bestcase_strings, recursive_lcs),
              LCSalgorithm('Recursive Worst Case', 16, utility.worstcase_strings, recursive_lcs)]

############### TEST AREA ################

strings_tests = 10
total_results = []

for algo in algorithms:
    total_results.extend(utility.testalgo(strings_tests, algo))

export_df = pd.DataFrame(total_results)

excel_file_path = "C:/Users/acgib/Desktop/univ/algorithms laboratory/NEW TESTS.xlsx"  #TO BE CHANGED FOR OTHER COMPUTERS
export_df.to_excel(excel_file_path, index=False, engine='openpyxl')
