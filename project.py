#!/usr/bin/env python3
"""
Demo Python project created through OpenClaw integration
"""

def hello_world():
    """Print a greeting message"""
    print("Hello from GitHub Demo Project!")
    return "Hello World"

def calculate_sum(a, b):
    """Calculate the sum of two numbers"""
    return a + b

def main():
    """Main function to demonstrate the project"""
    hello_world()
    
    # Example usage
    result = calculate_sum(5, 7)
    print(f"5 + 7 = {result}")
    
    # Create a simple list
    numbers = [1, 2, 3, 4, 5]
    print(f"Numbers: {numbers}")
    print(f"Sum: {sum(numbers)}")

if __name__ == "__main__":
    main()