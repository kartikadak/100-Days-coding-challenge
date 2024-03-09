#!/usr/bin/python2
import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return float(a) / b

def calc(choice, a, b):
    if choice == 1:
        return add(a, b)
    elif choice == 2:
        return sub(a, b)
    elif choice == 3:
        return mul(a, b)
    elif choice == 4:
        return div(a, b)
    else:
        print("Invalid choice")

# Number of arguments should be 3 (script name + 2 arguments)
if len(sys.argv) != 3:
    print("Usage: {} <arg1> <arg2>".format(sys.argv[0]))
    sys.exit(1)

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

try:
    choice = int(raw_input("Enter your choice (1: add, 2: subtract, 3: multiply, 4: divide): "))
except ValueError:
    print("Invalid choice")
    sys.exit(1)

result = calc(choice, arg1, arg2)
print("Result:", result)
