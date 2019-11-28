import inspect

def modified_func(func, *fixated_args, **fixated_kwargs):
    
    def new_func(*args, **kwargs):

        nonlocal fixated_args
        nonlocal fixated_kwargs
        args = fixated_args
        kwargs = fixated_kwargs

        if not fixated_args or not fixated_kwargs:
            func(fixated_args, fixated_kwargs)

        elif fixated_args or fixated_kwargs:
    	    fixated_args += fixated_args
    	    fixated_kwargs += fixated_kwargs
    	    func(fixated_args, fixated_kwargs)

        new_func.__name__ = f'func_{func.__name__}'
        new_func.__doc__ = \
        """
        A func implementation of {}
        with pre-applied arguments being:
        {}
        source_code:
        {}
        """.format(func.__name__, inspect.getcallargs(new_func), \
                   inspect.getsource(new_func))

    return new_func      