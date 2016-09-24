def insert_sort(l):
    """docstring"""
    nl = []
    for x in l:
        for y in nl:
            if x < y:
                nl.insert(nl.index(y), x)
                break
        else:
            nl.append(x)
    return nl
