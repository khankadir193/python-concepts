#all function accepts iterable objects such as list,tuple,dict etc.
#check wether all items it's true or not.
k = [1,2,4,5];
print(all(k));

k = [False,0];
print(all(k));

k =  [True,0,1];
print(all(k));

k = [];
print(all(k));

#bin:- python bin fun it is return the binary representation of a specified integer.
#A result always start prefix ob.
x = 100;
print('x..',bin(x));

#bool:- checking wether it's true or not.
x = [];
print('[]',bool(x));

x = [4,1];
print('[4,1]',bool(x));

x = [0];
print('[0]',bool(x));

x = '';
print('emptyString..?',bool(x));

x = 'abdul kadir khan';
print('string..',bool(x));

x = True;
print('True...',bool(x));

#bytes:- bytes fun used for returning bytes object.
#it is immutable version of of the bytearray() func.

str = "abdul kadir khan";
array = bytes(str,'utf-8');
print('array...',array);

#exec:this fun is used for dynamic execution of program. 
x = 8;
exec("print(x==8)");
exec("print(x==7)");

#sum:-sum fun is used to get the total sum of the iterable object.
arr = [1,4,7];
print(sum(arr));

#any func:- return true if any item is true in the iterable otherwise false;
x = [1,False,4];
print(any(x));

x = [4,6,3,5];
print(any(x));

x = [0,False,2];
print(any(x));

#eval function:
x = 8;
print(eval('x+1'));

#float:- the float point decimal number
x = 14;
print(float(x));
x=10.454;
print(float(x));

#format function:-return the formatted representation of given value.
print(format(123,'d'));

print(format(1234.4532,'f'));

print(format(10,'b'));