
def remember_result(f):
    def wrapper_func(*args, **kwargs):
        print(f"Last result = {wrapper_func.last_res!r}")
        val = f(*args, **kwargs)
        wrapper_func.last_res = val

        return val

    wrapper_func.last_res = None
    return wrapper_func

@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
sum_list("dwna", "daw")
sum_list("Abc", "Def")