
def binary_search(list, target):
    """
    This is a logarithmic runtime as few data a sampled based on the binary splitting
    O(log n) or O(ln n) or Logarithmic or sublinear , = Doubling number of search tries only increases by 1
    """
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify_index(index):
    if index is not None:
        print("Target found at:", index)
    else:
        print("Target not found in list")


numbers = [x for x in range(1000000000)]

result = binary_search(numbers, 10000000)
verify_index(result)
