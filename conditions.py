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

#typeof operator
a=9;
b=4;
print('performing arithmetic operation...')
add = a+b;
sub = a-b;
mult = a*b;
div = a/b;
mod = a%b;
pow = a**b;

print(add);
print(sub);
print(mult);
print(div);
print(mod);
print(pow);

#comprison operator
a=4;
b=3;
print('comprison operator');

print(a>b);
print(a<b);
print(a==b);
print(a!=b);
print(a>=b);
print(a<=b);

#logical && operator
a = 6;
b = 5;
c = 4;
#And operator practice
if(a>b and b>c):
    print('a greater than b and b greater than c');
#Or operatror practice.
if(b>a or b>c):
    print('b not greater than a or b greater than c');

#logical not operator  
a = 10;
if not a:
    print('a is true..');
if not (a%3 or a%5):
    print('10 is not divisible by 3 or 5');
else:
    print('10 is divisible by either 3 or 5');

#order of precedence of logical operator.
def order(x):
    print('method has been called..',x);
    return True if x>0 else False;

a = order;
b = order;
c = order;

if a(-1) or b(-10) or c(2):
    print('Atleast one method should be positive...');

#for loop
fruits = ['apple','mango','onion'];
for x in fruits:
    print(x,end=' ');

#while loop
i=0;
while i<5:
    print(i,end=' ');
    i = i+1;

