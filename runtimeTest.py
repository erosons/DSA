import timeit

x = [x for x in range(1000000)]

testcode = """ 
def test(): 
    x=[x for x in range(1000000)]
    
    return x[1]
"""
print(timeit.repeat(stmt=testcode))

testcode1 = """ 
def test1(): 
    x=[x for x in range(1000000)]
    
    return x[1000000]
"""
print(timeit.repeat(stmt=testcode1))
