#many value alongwith multiple variables
x,y,z = 10,30,40;
print(x);
print(y);
print(z);

#one value along with multiple variable
x=y=z = 40;
print('x',x,'y',y,'z',z);

#if you have collection of value like list,tuple etc. we can extract those value into
# a variable.

arr = [23,54,53,68];
a,b,c,d = arr;
print('a:',a,'b:',b,'c:',c,'d:',d);

#print() function is often used to output variables.
x = "Python is awesome";
print(x)
#OR
x = "Python"
y = "is"
z = "awesome"
print(x+y+z);

#mathmatical operation
x = 10;
y = 5;
print(x+y);

#if we add num and string in that will give error.
x = 5;
y = 'abdul kadir khan';
print(x,y);# this will give the error x+y unsupported error.