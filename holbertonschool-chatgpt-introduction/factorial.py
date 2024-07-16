#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            f = factorial(int(sys.argv[1]))
            print(f)
        except ValueError:
            print("Please provide a valid integer as an argument.")
    else:
        print("Please provide an integer as an argument.")