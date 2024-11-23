def is_prime(n: int) -> bool:
    """
    Check if a number is prime using optimized trial division.
    
    Optimizations:
    1. Early returns for n <= 3
    2. Even number check
    3. Only checks odd numbers up to square root
    4. Starts checking from 3
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    # Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd numbers up to the square root
    # We can use n ** 0.5 but integer multiplication is faster
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return False
    
    return True
