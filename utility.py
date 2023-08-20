from timeit import default_timer as timer
import statistics
import string
import random


####################### TIME TEST #############################

def timetest(lcs_alg, l1, l2):
    experiment_times = []

    for i in range(5):
        start = timer()
        lcs_length = lcs_alg(l1, l2)
        end = timer()
        execution_time = end - start
        experiment_times.append(execution_time)
        print(experiment_times)

    mean = statistics.mean(experiment_times)
    return lcs_length, mean


#####################################################################

####################### STRING CREATION #############################

# creates two random strings with the preferred length
def generate_random_string(length):
    uppercase_alphabet = string.ascii_uppercase
    generated_string1 = ''.join(random.choice(uppercase_alphabet) for _ in range(length))
    generated_string2 = ''.join(random.choice(uppercase_alphabet) for _ in range(length))
    return generated_string1, generated_string2

# creates strings for best case recursive
def bestcase_strings(length):
    bestcase = 'A' * length

    return bestcase, bestcase

# creates srings for worst case recursive
def worstcase_strings(length):
    string1 = 'A' * length
    string2 = 'B' * length

    return string1, string2

############################### ALGORITHMS TESTS ###############################

def testalgo(strings, algorithm):
    results = []

    for length in range(1, algorithm.max_length):
        lcs_lengths = []
        execution_times = []

        for _ in range(strings):
            str1, str2 = algorithm.string_function(length)
            print(str1, str2)

            lcs_length, execution_time = timetest(algorithm.algorithm_function, str1, str2)

            lcs_lengths.append(lcs_length)
            execution_times.append(execution_time)

        mean_lcs_length = statistics.mean(lcs_lengths)
        mean_execution_time = statistics.mean(execution_times)

        item = {
            'algo_name': f"{algorithm.name}{length}",
            'mean_lcs_length': mean_lcs_length,
            'mean_execution_time': mean_execution_time
        }

        results.append(item)

    return results