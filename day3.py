## Recursion
#  recursion is a process where a funcyion call itself
## fcatorial

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print("enter the n value: ")
n = int(input())
print(f"the factorial for the entered value is {fact(n)}")

'''
->in recusrion we have 2 cases 
1. base case: when the function does not call itself
2. recursive case: when the function calls itself

->if we didnt use the base case the fuction will call itself infinite times and it will give us a stack overflow error
->in python the default recursion limit is 1000, if we call the function more than 1000 times it will give us a recursion error

-> stack has 2 operations push and pop
push: when we call a function it will be pushed to the stack
pop: when the function is executed it will be popped from the stack
-> stack is a data structure which follows LIFO(last in first out) principle

'''