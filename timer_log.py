import time
from collections import Counter
import timeit
import matplotlib.pyplot as plt
import numpy as np

#decorator to measure execution time
def exec_time_decorator(func):
    def wrapper(*args, **kwargs):
        
        #record strat tie
        start_time = time.time()
        #call the original function
        result = func(*args, **kwargs)
        end_time = time.time()
        #record end time
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds")
        return result
    return wrapper

#function read shakesear artwork 
def read_shakespeare(file_path):
    with open(file_path, 'r') as file:

        return file.read()

#count words using a dictionary
@exec_time_decorator
def count_words_dic(text):

    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word]= 1
    return word_count

#count words using Counter function
@exec_time_decorator
def count_words_counter(text):

    words = text.split()
    word_count = Counter(words)
    return word_count


if __name__ == "__main__":

    #path to txt file
    shakespeare_artwork_path = 't8.shakespeare.txt'

    #read txt
    shakespeare_text = read_shakespeare(shakespeare_artwork_path)

    #call the words counting functions 
    word_count_dict = count_words_dic(shakespeare_text)
    word_count_counter = count_words_counter(shakespeare_text)

    nb_experiments = 100

    #we define 2 lists to store execution time
    execution_times_dic = []
    execution_times_counter = []

    for i in range(nb_experiments):

        #execution time for counting words using dictionary (by using timeit)
        dic_time = timeit.timeit(
            lambda: count_words_dic(shakespeare_text),
            number=1
        )
        execution_times_dic.append(dic_time)

        #execution time for counting words using Counter (by using timeit)
        counter_time = timeit.timeit(
            lambda: count_words_counter(shakespeare_text),
            number=1
        )
        execution_times_counter.append(counter_time)

    # Plot the distributions
    plt.figure(figsize=(10, 5))
    plt.hist(execution_times_dic, bins=20, alpha=0.5, label='Dictionary function', color='b')
    plt.hist(execution_times_counter, bins=20, alpha=0.5, label='Counter function', color='r')
    plt.xlabel('execution time (s)')
    plt.ylabel('frequency')
    plt.legend()
    plt.show()

    #mean and variance
    mean_dict = np.mean(execution_times_dic)
    var_dict = np.var(execution_times_dic)
    mean_counter = np.mean(execution_times_counter)
    var_counter = np.var(execution_times_counter)
    print(f"Mean (Dictionary): {mean_dict:.6f} seconds")
    print(f"Variance (Dictionary): {var_dict:.6f}")
    print(f"Mean (Counter): {mean_counter:.6f} seconds")
    print(f"Variance (Counter): {var_counter:.6f}")
    
