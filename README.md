# Sorting-and-Searching-Visualize-method

#### Sorting

- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort

#### Searching

- Linear Search
- Binary Search

### Installing

```bash
$pip3 install algovis
```



### Using the sorting package



#### Visualize method

```python
# import the sorting package from library
from algovis import sorting

# importing random module to shuffle the list
import random

# Making a list of 100 integers from 1-100
# using list comprehension
my_list = [i+1 for i in range(100)]

# shuffling the list
random.shuffle(my_list)

# making a BubbleSort class object by passing the shuffled list
bs_object = sorting.BubbleSort(my_list)

# calling the visualize method
bs_object.visualize(interval= 100)
```
##### Output
<img src="https://media.giphy.com/media/ieb13rrmvVWC02zmI8/giphy.gif" width="700">



#### sort method

```python
# lets work on a shorter example now
my_list = [i + 1 for i in range(10)]

# shuffling the list using random module
random.shuffle(my_list)

#making a quicksort object
qs_object = sorting.QuickSort(my_list)

#sorting in reverse with steps
qs_object.sort(pivot = "first", steps = True, reverse = True)

# you can see the pivot placed correctly in the 'array in consideration' column
# the state of whole array at that iteration is shown in 'array' column
```

##### Output
![qs-sort](img/qs-steps.png)




#### evaluate method
```python
# calling the evaluate method and passing the optional parameter 'iterations'
# the list is sorted 'iterations' number of times and the min, max and average time taken
#to sort the list is returned in form of a formatted table
bs_object.evaluate(iterations = 100)
```
#### search method
```python
#importing searching package
from algovis import searching

# making a list of integers from 1 to 100
# using list comprehension
my_list = [i+1 for i in range(100)]

#making binary search object
bin_search = searching.BinarySearch(my_list)

#calling the search method
bin_search.search(42, steps = True)
```
![searching-img](img/binary_search_steps.png)


#### visualize method

```python
# calling the visualize method
# interval is the time between two different frames of the animation
bin_search.visualize(42, interval = 1000)
```
<img src ="https://media.giphy.com/media/l3Cktj8ULcjHK3c90E/giphy.gif" width ="700">

```python
# or if you want to linear search 42
lin_search = searching.LinearSearch(my_list)

# setting a less interval to make a much faster animation
lin_search.visualize(42, interval = 100)
```

<img src ="https://media.giphy.com/media/lSbSNLD3OPaUZT4NX6/giphy.gif" width ="700">
