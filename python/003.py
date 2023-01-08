"""
Project Euler Problem 003:
    Largest prime factor of 600851475143
"""
def main():
    largestDivisor = 0
    number = 600851475143
    i = 2
    
    while i < number:
      if number % i == 0:
        number /= i
        largestDivisor = i
      else:
        i += 1
    
    print(largestDivisor if largestDivisor > number else number)
        
        
    
if __name__ == "__main__":
    main()