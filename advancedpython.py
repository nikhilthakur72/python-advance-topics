#1 question
b=[1,2,3,4]
b=[i**3 for i in b]
print(b)
#2 question
a=[i for i in range(2,20)  for j in range(2,i) if(i%j==0)  ]
b=[i for i in range(2,20) if(i not in a )]
print(b)
#3 question
'''
In terms of syntax, the only difference we use parenthesis instead of square brackets.

The type of data returned by list comprehensions and generator expressions differs.

The generator yields one item at a time — thus it is more memory efficient than a list.'''
#4 question

Celsius = [39.2 ,36.5, 37.3, 37.8]
t=list(map(lambda x: 1.8*x+32,Celsius))
print(t)

#5 question
lst=[1,2,3]
def square_(n):
    return n*n
s=list(map(lambda n:square_(n),lst))
print(s)
#6 question
lst=[1,2,3,4,5,6,7,8,9]
def isprime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
        
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n
    
p=list(filter(lambda n: isprime(n),lst))
print(p)
#7 question
lst=[1,2,3,4,5,5]
from  functools import *
t=reduce(lambda x,y:x*y,lst)
print(t)
    
    
