def generator_number(n):
    for i in range(n):
        yield i;

numbers = generator_number(5);
for num in numbers:
    print(num);