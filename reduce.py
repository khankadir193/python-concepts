from functools import reduce;
red = [1,2,3,4,5,6];
def add(a,b):
    return a+b;
result = reduce(add,red);
print('reduceFunction:---',result);

#reduce function with lamda fuction

res = reduce(lambda x,y:x+y,red);

print('res..???',res);