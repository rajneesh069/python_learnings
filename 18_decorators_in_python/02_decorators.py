def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"function name: {func.__name__}, args:{args}, kwargs:{kwargs}")
        return result

    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("Rajneesh")
