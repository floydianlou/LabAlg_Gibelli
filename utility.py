from timeit import default_timer as timer
import statistics
import string
import random


####################### TIME TEST #############################

def timetest(lcs_alg, l1, l2):
    experiment_times = []

    for i in range(10):
        start = timer()
        lcs_length = lcs_alg(l1, l2)
        end = timer()
        execution_time = end - start
        experiment_times.append(execution_time)
        print(experiment_times)  # TO REMOVE FOR EXAM

    mean = statistics.mean(experiment_times)
    return lcs_length, mean


#####################################################################

####################### STRING CREATION #############################

# creates a random string with the preferred length
def generate_random_string(length):
    uppercase_alphabet = string.ascii_uppercase
    generated_string = ''.join(random.choice(uppercase_alphabet) for _ in range(length))
    return generated_string


# creates a list of strings ranging from min_length to max_length

def listofstrings(min_length, max_length):
    list_strings = [generate_random_string(length) for length in range(min_length, max_length + 1)]
    return list_strings

# creates strings for best case recursive

def bestcase_strings(length):
    l1 = []
    for i in range(length):
      string = 'A' * i
      l1.append(string)

    return l1

def worstcase_strings(max_length=16):
    strings_list1 = []
    strings_list2 = []

    for length in range(max_length + 1):
        string1 = 'A' * length
        string2 = 'B' * length
        strings_list1.append(string1)
        strings_list2.append(string2)

    return strings_list1, strings_list2

#####################################################################


def test_algorithms(algorithms, algorithm_names, l1, l2):
    # dictionary: stores test results to then export to excel
    result_data = {}

    for i, algorithm in enumerate(algorithms):
        for j in range(len(l1)):
            length_key = len(l1[j])
            result, mean_execution_time = timetest(algorithm, l1[j], l2[j])
            result_data[(algorithm_names[i], length_key)] = (result, mean_execution_time)

    print("Test Results:", result_data)

    return result_data
