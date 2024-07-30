def my_function(n):
    """
    Returns a lambda function that multiplies its 
argument by n.
    """
    return lambda a: a * n


quadruple = my_function(4)

print(quadruple(10))
