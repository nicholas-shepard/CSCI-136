def any(boolArray):
    if True in boolArray:
        return True
    else:
        return False

def all(boolArray):
    if False in boolArray:
        return False
    else:
        return True
