import time


def cache(func):
    cached_value = {}
    print(cached_value)

    def wrapper(*args, **kwargs):
        if args in cached_value:
            return cached_value[args]
        result = func(*args, **kwargs)
        cached_value[args] = result
        return result

    return wrapper


@cache
def long_running_fn(a, b):
    time.sleep(4)
    return a + b


print(long_running_fn(2, 3))
print(long_running_fn(2, 3))
