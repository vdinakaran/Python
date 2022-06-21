# Iterator in Python is simply an object that can be iterated upon.
# An object which will return data, one element at a time.
#Python iterator object must implement two special methods, __iter__() and __next__()
# called the iterator protocol.
# An object is called iterable if we can get an iterator from it.
# Most built-in containers in Python like: list, tuple, string etc. are iterables.
# The iter() function returns an iterator from them.

# Iterating Through an Iterator
###################################
# next() function is to manually iterate through all the items of an iterator.
# When we reach the end and there is no more data to be returned, it will raise the StopIteration Exception.

#Working of for loop for Iterators
####################################
#So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.
#for loop is actually an infinite while loop.
#Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value.
# After all the items exhaust, StopIteration is raised which is internally caught and the loop ends.

