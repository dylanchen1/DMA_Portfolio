import sys
import math
def main():
    command = sys.argv[1]
    if command == "add":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x + y)
    if command == "subtract":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x - y)
    if command == "multiply":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x * y)
    if command == "divide":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x / y)
    if command == "exponent":
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(math.pow(x, y))
    if command == "countto":
        x = int(sys.argv[2])
        for i in range(x):
            print(i + 1)
    if command == "hypot":
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        pythagorean(a,b)
    if command == "quadratic":
        a = int(sys.argv[2])
        b = int(sys.argv[3])
        c = int(sys.argv[4])
        quadratic(a, b, c)

def pythagorean(a, b):
    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)
    print math.sqrt(a_squared + b_squared)

def quadratic (a, b, c):

    b_squared = math.pow(b, 2)
    deter = b_squared - (4 * a * c)
    print (((-b) + math.sqrt(deter)) / (2 * a))
    print (((-b) - math.sqrt(deter)) / (2 * a))
if __name__ == '__main__':
    main()