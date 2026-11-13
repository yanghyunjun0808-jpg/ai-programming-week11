from bug3_logic import count_pass


def test_cutoff_score_counts_as_pass():
    assert count_pass([60, 60, 59]) == 2


def test_scores_above_default_cutoff():
    assert count_pass([70, 85, 95]) == 3


def test_custom_cutoff_is_inclusive():
    assert count_pass([69, 70, 71], cutoff=70) == 2


def test_scores_below_cutoff():
    assert count_pass([59, 40, 0]) == 0


def test_empty_scores():
    assert count_pass([]) == 0
