#========
#Big O(n) as data increases  directly proportional to time increase
#========
def linear_search(list, targetvalue):
    """
    Return an index postion of a target value from linear search
    Note the runtime for the iteration over the list is constant time => O(1)
    """
    for i in range(0, len(list)):
        if list[i] == targetvalue:
            return i
    return None


def verify_index(index):
    if index is not None:
        print("Target found at:", index)
    else:
        print("Target not found in list")


number = [x for x in range(11)]
result = linear_search(number, 8)
verify_index(result)
