def shortString(a):
    if a == []:
        return None
    return shortStringHelper(a, a[0])

def shortStringHelper(a, b):
    if a == []:
        return b
    if len(a[0]) < len(b):
        return shortStringHelper(a[1:], a[0])
    return shortStringHelper(a[1:], b)
