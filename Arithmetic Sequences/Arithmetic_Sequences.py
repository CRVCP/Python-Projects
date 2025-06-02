import random

# Helper function for subscript formatting
def to_subscript(n):
    """Convert a number or 'n' to its subscript representation using Unicode characters."""
    # Handle the special case of 'n' directly
    if n == 'n':
        return 'ₙ'  # Unicode subscript n
    
    # For numbers, translate each digit to its subscript equivalent
    sub_map = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    return str(n).translate(sub_map)


def find_common_difference(a_n, a_m, n, m):
    """Calculate the common difference (d) of an arithmetic sequence
    given two terms and their positions."""
    return (a_n - a_m) / (n - m)

def find_a0(a_k, k, d):
    """Find the initial term (a₀) of an arithmetic sequence
    given any term, its position, and the common difference."""
    return a_k - k * d

def get_general_formula(a0, d):
    """Generate the general formula string for an arithmetic sequence."""
    # Use the subscript n directly
    return f"a{to_subscript('n')} = {a0} {'+' if d >= 0 else '-'} {abs(d)}·{to_subscript('n')}"

def generate_arithmetic_problem():
    """Generate a random arithmetic sequence problem and its answer.
    
    Returns:
        tuple: (question string, answer string)
    """
    problem_type = random.randint(1, 8)

    if problem_type == 1:
        # Find a specific term given first term and common difference
        a1 = random.randint(-20, 20)
        d = random.randint(1, 10)
        n = random.randint(5, 15)
        an = a1 + (n - 1) * d
        question = f"(Type 1) Given a{to_subscript(1)} = {a1}, d = {d}, find a{to_subscript(n)}."
        answer = f"a{to_subscript(n)} = {an}"

    elif problem_type == 2:
        # Find the common difference given two terms
        m = random.randint(2, 5)
        n = m + random.randint(2, 5)
        am = random.randint(10, 30)
        # Calculate an based on a random d
        d = random.randint(1, 10)
        an = am + (n - m) * d
        # Use the helper function to verify the calculation
        calculated_d = find_common_difference(an, am, n, m)
        question = f"(Type 2) Given a{to_subscript(m)} = {am}, a{to_subscript(n)} = {an}, find the common difference d."
        answer = f"d = {d}"

    elif problem_type == 3:
        # Find the initial term given a term and common difference
        k = random.randint(3, 7)
        d = random.randint(2, 6)
        # Calculate a0 using a random ak
        ak = random.randint(20, 50)
        a0 = find_a0(ak, k, d)
        question = f"(Type 3) Given a{to_subscript(k)} = {ak} and d = {d}, find a{to_subscript(0)}."
        answer = f"a{to_subscript(0)} = {a0}"

    elif problem_type == 4:
        # Write the general formula
        a0 = random.randint(-10, 10)
        d = random.randint(1, 5)
        question = f"(Type 4) Given a{to_subscript(0)} = {a0}, d = {d}, write the general formula for a{to_subscript('n')}."
        answer = f"{get_general_formula(a0, d)}"

    elif problem_type == 5:
        # Determine if a number is in the sequence
        a1 = random.randint(0, 10)
        d = random.randint(2, 10)
        max_n = 20
        all_terms = [a1 + (i - 1) * d for i in range(1, max_n + 1)]
        # Either pick a term from the sequence or a random number outside it
        candidate = random.choice(all_terms + [random.randint(100, 200)])
        is_in_sequence = candidate in all_terms
        question = f"(Type 5) Is {candidate} part of the sequence starting with a{to_subscript(1)} = {a1} and d = {d}?"
        answer = "Yes, it's part of the sequence." if is_in_sequence else "No, it's not in the sequence."

    elif problem_type == 6:
        # Find the position of a term
        a1 = random.randint(1, 10)
        d = random.randint(2, 6)
        n = random.randint(5, 15)
        an = a1 + (n - 1) * d
        question = f"(Type 6) In the sequence with a{to_subscript(1)} = {a1} and d = {d}, what is n if a{to_subscript('n')} = {an}?"
        answer = f"n = {n}"

    elif problem_type == 7:
        # Find a missing term given surrounding terms
        a1 = random.randint(0, 10)
        d = random.randint(2, 6)
        # Calculate a4 and a5 based on the arithmetic sequence formula
        a4 = a1 + 3 * d
        a5 = a1 + 4 * d  # This ensures a5 = a4 + d
        question = f"(Type 7) In the sequence a{to_subscript(1)} = {a1}, a{to_subscript(4)} = ?, a{to_subscript(5)} = {a5}, find a{to_subscript(4)}."
        answer = f"a{to_subscript(4)} = {a4}"

    elif problem_type == 8:
        # Real-world application problem
        a1 = random.randint(50, 100)
        d = -random.randint(1, 5)
        n = random.randint(5, 15)
        an = a1 + (n - 1) * d
        question = f"(Type 8) A staircase has {a1} bricks in the first row, with {abs(d)} fewer in each next row. How many bricks in row {n}?"
        answer = f"{an} bricks"

    return question, answer

# Main loop
if __name__ == "__main__":
    print("Arithmetic Sequence Problem Generator")
    print("====================================")
    print(f"Example formula: a{to_subscript('n')} = a₁ + (n-1)·d")
    print("====================================")
    print("This program generates random arithmetic sequence problems.")
    print("Press Enter to see the answer after each question.")
    print("Type 'n' to quit or any other key to continue.\n")
    
    while True:
        question, answer = generate_arithmetic_problem()
        print("\n" + question)
        input("Press Enter to see the answer...")
        print("Answer:", answer)
        again = input("\nTry another? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for practicing arithmetic sequences!")
            break
