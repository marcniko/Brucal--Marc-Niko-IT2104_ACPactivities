def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).
    """
    if n < 1:
        return False  
    
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    
    return divisors_sum == n

def main():
    try:
        num = int(input("Enter a positive integer: "))
        
        if num <= 0:
            print("Please enter a positive integer.")
        else:
            if is_perfect_number(num):
                print(f"{num} is a perfect number.")
            else:
                print(f"{num} is not a perfect number.")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
