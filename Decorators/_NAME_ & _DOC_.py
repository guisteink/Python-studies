"""
    Os caracteres __ , significam Dunder, ou seja __NAME__ -> Dunder name ; __DOC__ -> Dunder doc

    -> Para ser dunder, deve ser __ no início e no fim __

"""

def soma(a,c):
    """isso eh um teste"""
    return a+c


print(soma.__doc__)
print(soma.__name__)