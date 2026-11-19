from gradebook import calculate_average, count_passing, letter_grade


def test_average_of_two_scores():
    assert calculate_average([70, 90]) == 80


def test_letter_grade_for_high_score():
    assert letter_grade(95) == "A"


def test_count_scores_above_passing_score():
    assert count_passing([40, 65, 80]) == 2
