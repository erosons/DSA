def linear_search_ops(list_array,targetValue) -> str:
    for i in range(0, len(list_array)):
        if list_array[i]==targetValue:
            return i
    return None


if __name__=="__main__":
    test_array=[x for x in range(18)]
    print(linear_search_ops(test_array,5))