def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint + 1 :], target)
        else:
            return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found", result)


number = [x for x in range(100)]


result = recursive_binary_search(number,90)
verify(result)
