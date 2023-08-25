def string_to_integer(string: str):
    """Converts a string of digits into integer it represents."""
    n = len(string)

    if n == 1:
        return int(string[n-1])
    else:
        return int(string[n-1]) + 10 * string_to_integer(string[:n-1])
    

print(string_to_integer('13531789'))
