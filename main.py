def compute_grades(TQ1, TQ2, TQ3, TQ4):
    Q1 = TQ1
    Q2 = (Q1 + 2 * TQ2) / 3
    Q3 = (Q2 + 2 * TQ3) / 3
    Q4 = (Q3 + 2 * TQ4) / 3
    return Q1, Q2, Q3, Q4
    
def adjectival_grade(grade):
    if grade >= 90:
        return "Outstanding"
    elif grade >= 85:
        return "Very Satisfactory"
    elif grade >= 80:
        return "Satisfactory"
    elif grade >= 75:
        return "Fairly Satisfactory"
    else:
        return "Did not meet Expectations"
    
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
