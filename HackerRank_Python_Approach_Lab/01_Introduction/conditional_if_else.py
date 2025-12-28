"""
PROBLEM: HackerRank Python If-Else
GOAL: Categorize an integer 'n' based on parity (odd/even) and range.
STRATEGY: Use a cascading if-elif-else structure to filter numbers.
"""
n = int(input().strip())

    # STEP 1: Check if the number is Odd
if n % 2 != 0:
        print("Weird")
    
    # STEP 2: The number is Even (because it failed the first 'if')
    # Check if even and between 2 and 5
elif 2 <= n <= 5:
        print("Not Weird")
    
    # Check if even and between 6 and 20
elif 6 <= n <= 20:
        print("Weird")
    
    # Check if even and greater than 20
else:
        print("Not Weird")