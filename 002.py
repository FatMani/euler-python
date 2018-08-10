"""
Project Euler Problem 002:
    Sum of even Fibonacci numbers smaller than 4 million
"""

def main():
    print(sum(x for x in fibonacciSmallerThan(4000000) if x % 2 == 0))
    
def fibonacciSmallerThan(x):
    result = [0, 1]
    i = 2
    while True:
        newNumber = result[i - 1] + result[i - 2]
        if newNumber > x:
            break
        else:
            result.append(newNumber)
            i = i + 1
    return result

if __name__ == "__main__":
    main()