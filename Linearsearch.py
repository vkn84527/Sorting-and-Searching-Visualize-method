#importing searching package
from algovis import searching

# making a list of integers from 1 to 100
# using list comprehension
my_list = [i+1 for i in range(100)]

#making Linear search object
bin_search = searching.LinearSearch(my_list)

#calling the search method
bin_search.search(42, steps = True)

# calling the visualize method
bin_search.visualize(42, interval = 1000)
