def make_it_count(func, counter_name):
	""" Returning a new function which:
	- has the same behavior as a behavior of the function set as argument,
	- increments value of 'counter_name' global variable when calling
	the function.
	"""

    def new_func(*args, **kwargs):
        global counter_name
        counter_name += 1
        func(*args, **kwargs)

    return new_func