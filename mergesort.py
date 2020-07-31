# importing the sorting module
from algovis import sorting

#importing the random module for shuffling the list
import random

# creating a list of integers from 1 to 100
my_list = [i + 1 for i in range(100)]

# shuffling the list using random module
random.shuffle(my_list)

# creating an oject of the MergeSort class and passing
# the list
bs_object = sorting.MergeSort(my_list)
#calling the visualize method
bs_object.visualize(interval=100)

