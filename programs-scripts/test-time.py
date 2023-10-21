import time
from timeit import Timer
from functools import partial


# .......................................................
# start = time.time()
# Code ...
# end = time.time()


# .......................................................
# time = timeit.timeit(function, number=1)

# function_without_parameters = partial(function, parameter)
# time = timeit.timeit(function_without_parameters, number=1)





def format_bytes2(size_bytes):
    gb = size_bytes / 1e9
    mb = size_bytes / 1e6
    kb = size_bytes / 1e3

    if size_bytes >= 1e9:
        return f'{gb:.2f} GB'
    if size_bytes >= 1e6:
        return f'{mb:.2f} MB'
    if size_bytes >= 1e3:
        return f'{kb:.2f} KB'
    return f'{size_bytes} B'


def format_bytes(size_bytes):
    if size_bytes >= 1e9:  # Más de 1 GB
        return f'GB {size_bytes / 1e9:.2f}'
    if size_bytes >= 1e6:  # Más de 1 MB
        return f'MB {size_bytes / 1e6:.2f}'
    if size_bytes >= 1e3:  # Más de 1 KB
        return f'KB {size_bytes / 1e3:.2f}'
    return f'B  {size_bytes}'


