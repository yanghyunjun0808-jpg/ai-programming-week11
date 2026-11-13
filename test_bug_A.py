from bug3_logic import find_max


def test_maximum_at_start():
    assert find_max([95, 85, 70, 60]) == 95


def test_maximum_in_middle():
    assert find_max([10, 30, 20, 5]) == 30


def test_maximum_at_end():
    assert find_max([10, 20, 30]) == 30


def test_single_score():
    assert find_max([42]) == 42


def test_all_negative_scores():
    assert find_max([-10, -2, -7]) == -2
