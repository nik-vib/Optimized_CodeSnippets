def is_valid_parentheses(s: str) -> bool:
    """
    Check if a string contains valid parentheses combinations.
    Valid pairs are: (), [], {}
    
    Args:
        s (str): String containing parentheses
        
    Returns:
        bool: True if parentheses are valid, False otherwise
    
    Time Complexity: O(n) where n is length of string
    Space Complexity: O(n) in worst case where all chars are opening brackets
    """
    # Optimization 1: Early return if string length is odd
    if len(s) % 2:
        return False
    
    # Optimization 2: Use dictionary for O(1) lookup
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    # Optimization 3: Use set for O(1) lookup of closing brackets
    closing_brackets = set(brackets.values())
    
    # Optimization 4: Use list as stack for better memory usage
    stack = []
    
    for char in s:
        if char in brackets:  # Opening bracket
            stack.append(char)
        elif char in closing_brackets:  # Closing bracket
            # If stack is empty or brackets don't match
            if not stack or brackets[stack.pop()] != char:
                return False
    
    # Valid only if all brackets are matched
    return len(stack) == 0

# Test cases to verify functionality
def run_tests():
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False),
        ("((()))", True),
        ("((())", False),
        ("{[()]}", True)
    ]
    
    for test_input, expected in test_cases:
        result = is_valid_parentheses(test_input)
        print(f"Input: {test_input:<10} Expected: {expected:<5} Got: {result:<5} {'✓' if result == expected else '✗'}")

if __name__ == "__main__":
    run_tests()