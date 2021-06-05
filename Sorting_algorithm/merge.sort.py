def merger_sort(list):
    """
    Sort alist in and ascending other
    Returns a new sorted list

    Divide fing the middle point of y=the list  and divde into sublist

    Conquer : Recursively sort the sublist created in previous step

    Combine: Merge the recursive sorted list created in previous step
    takes O(n logn)
    """

    if len(list) <= 1:
        return list

    # Here we calling a split function that divide the list
    left_half, right_half = split(list)
    left = merger_sort(left_half)
    right = merger_sort(right_half)

    return merge(left, right)


def split(list):
    """
    Divde the unsorted list at midpoit into sublists
    Returns two sublists -left and right
    takes O(logn)
    """
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merge two lists(arrays), sorting them in the process
    Returns a new merged list
    """
    l = []
    # Using i and j to keep track of the indexes from both list
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        True
    return list[0] < list[1] and verify_sorted(list[1:])


mylist = [4, 5, 8, 23, 89, 2, 90, 56, 78, 45, 87, 54, 34, 42, 80]
test = merger_sort(mylist)
print(verify_sorted(mylist))
print(test)

# Python Implementaion
print(sorted(mylist))
