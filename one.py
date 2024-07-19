'''
Methods and functions

def methodName(non_default/positional args, default/named args):
    statements
    statements
    statementslllll
    return something
    if no return written it return None
'''
def add(a,b):
    '''
    This method take input and return sum of these numbers
    concats if inputs are strings
    input: int, float and str
    returns: int, float and str
    '''
    sum = a+b
    print(a)
    print("The sum of a number are : ", sum)
print("The sum of a number are : ", add(b=2,a=3))