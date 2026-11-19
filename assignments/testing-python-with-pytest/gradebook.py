def calculate_average(scores):
    """Return the arithmetic mean of scores, or 0 when there are no scores."""
    if not scores:
        return 0
    return sum(scores) // len(scores)


def letter_grade(score):
    """Return a letter grade: A (90+), B (80+), C (70+), D (60+), or F."""
    if score > 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def count_passing(scores, passing_score=60):
    """Return how many scores meet or exceed the passing score."""
    return sum(score > passing_score for score in scores)
