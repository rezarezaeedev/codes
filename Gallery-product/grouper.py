def list_grouper(n, iterable):
    args = [iter(iterable)] * n
    return list(([e for e in t if e != None] for t in itertools.zip_longest(*args)))
# 
