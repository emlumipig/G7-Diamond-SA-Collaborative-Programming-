def compute_grades(TQ1, TQ2, TQ3, TQ4):
    Q1 = TQ1
    Q2 = (Q1 + 2 * TQ2) / 3
    Q3 = (Q2 + 2 * TQ3) / 3
    Q4 = (Q3 + 2 * TQ4) / 3
    return Q1, Q2, Q3, Q4
