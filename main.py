def compute_grades(TQ1, TQ2, TQ3, TQ4):
    Q1 = TQ1
    Q2 = (Q1 + 2 * TQ2) / 3
    Q3 = (Q2 + 2 * TQ3) / 3
    Q4 = (Q3 + 2 * TQ4) / 3
    return Q1, Q2, Q3, Q4
    
def adjectival_grade(grade):
    if 1.00 <= grade <= 1.24:
        return "Excellent"
    elif 1.25 <= grade <= 1.49:
        return "Very Good"
    elif 1.50 <= grade <= 1.74:
        return "Very Good"
    elif 1.75 <= grade <= 1.99:
        return "Good"
    elif 2.00 <= grade <= 2.24:
        return "Good"
    elif 2.25 <= grade <= 2.49:
        return "Satisfactory"
    elif 2.50 <= grade <= 2.74:
        return "Satisfactory"
    elif 2.75 <= grade <= 2.99:
        return "Fair"
    elif 3.00 <= grade <= 3.99:
        return "Fair"
    elif 4.00 <= grade <= 4.99:
        return "Failed on Condition"
    else:
        return "Failed"
    
# User input
TQ1 = float(input("Enter TQ1: "))
TQ2 = float(input("Enter TQ2: "))
TQ3 = float(input("Enter TQ3: "))
TQ4 = float(input("Enter TQ4: "))

# Call Member 1 function
Q1, Q2, Q3, Q4 = compute_grades(TQ1, TQ2, TQ3, TQ4)

# Final grade (Q4 is final output)
final_grade = Q4

# Output results
print("\n--- RESULTS ---")
print(f"Q1: {Q1:.2f}")
print(f"Q2: {Q2:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"Q4: {Q4:.2f}")

print("\nFinal Grade:", f"{final_grade:.2f}")
print("Adjectival:", adjectival_grade(final_grade))
