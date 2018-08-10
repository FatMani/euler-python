"""
Project Euler Problem 001:
    Sum of numbers smaller than 1000, that are divisible by 3 or 5
"""

def main():
    print(sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0))
        
if __name__ == "__main__":
    main()