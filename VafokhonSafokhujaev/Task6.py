def call_once(f):
    def wrapper_func(*args, **kwargs):
        if wrapper_func.called:
            return wrapper_func.val

        wrapper_func.val = f(*args, **kwargs)
        wrapper_func.called = True
        return wrapper_func.val

    wrapper_func.val = None
    wrapper_func.called = False

    return wrapper_func

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(155, 342))
print(sum_of_numbers(151, 2))
print(sum_of_numbers(856, 232))