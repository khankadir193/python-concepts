#decorator:In Python, a decorator is a design pattern that allows you to modify or 
#extend the behavior of functions or classes without permanently modifying their code. 
#Decorators are essentially functions that wrap another function or method, adding some 
#additional functionality to it.

#Decorators are commonly used for tasks such as logging, caching, authentication, 
#and performance monitoring. They provide a clean and concise way to add cross-cutting 
#concerns to your code without cluttering the original function or class definition.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
