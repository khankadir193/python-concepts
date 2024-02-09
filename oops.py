class Person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
    def greet(self):
        print("Hi My name is :->"+self.name+' and my age is :->'+self.age);

person1 = Person('Abdul Kadir Khan','24');
person1.greet();

#another class
class Employee:
    count = 0;
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
    def disp(self):
        Employee.count +=1;

person1 = Employee('Abdul Kadir Khan','24');
person1 = Employee('Abdul Jabir Khan','18');
person1.disp();
person1.disp();
print('count...?',Employee.count);