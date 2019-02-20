def shortest_string(myArray):
    if myArray == []:
        return ''
    return shortest_string_helper(myArray[1:], myArray[0])

def shortest_string_helper(myArray, short):
    if myArray == []:
        return short
    if len(myArray[0]) < len(short):
        return shortest_string_helper(myArray[1:], myArray[0])
    return shortest_string_helper(myArray[1:], short)

print(shortest_string(["myy", "face", "iss", "aaa", "wreck", "ok", "?"]))
