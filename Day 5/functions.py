'''
There are 4 types of functions in python
positopnal arguments
default arguments
keyword arguments
variable length arguments
'''
#----------------------------------------------------------------------------------------------------
'''
#postional arguments
def positionalArguments(a,b) :
    return a+b
#default arguments
def defaultArguments(a=0,b=0) :
    return a+b
#keyword arguments
def KeywordArguments(a=None,b=None) :
    if a is None or b is None :
        return "expected positional arguments"
    return a+b
'''
#---------------------------------------------------------------------------------------------------
'''
#syntax : map(function_object,iterable)
#iterable : list,tuple etc
#map function
def  square(num) :
    return num*num
data= [1,2,3,4,5]
res = list(map(square,data))
print(res)
'''
#----------------------------------------------------------------------------------------------------
'''
#syntax : filter(function_object,iterable)
#iterable : list,tuple etc
#filter function
def verify(age) :
    return age > 18
ages = [12,45,23,54,13,14]
adults = list(filter(verify,ages))
print(adults)
'''
#-----------------------------------------------------------------------------------------------------
'''
#import functools package
#syntax : reduce(function_object,iterable,startingValueIsOptional=0)
#iterable : list,tuple etc
from functools import reduce

def sumOfElements(a,b):
    return a+b
data = [1,2,3,4,5]
res = reduce(sumOfElements,data)
print(res)
'''
#-------------------------------------------------------------------------------------------------------
'''
#sorting the 2d array based on the last element using lambda functions 
arr = [
    [1,2,3,4,5],
    [2,3,4,5,1],
    [3,4,5,1,2],
    [5,1,2,3,4],
    [4,5,1,2,3]
]
arr.sort(key=lambda ele:ele[-1])
print(*arr,sep="\n")
'''
#--------------------------------------------------------------------------------------------------------
#lambda functions
#syntax : var = lambda arguments : returningValue
#example : add = lambda a,b : a+b