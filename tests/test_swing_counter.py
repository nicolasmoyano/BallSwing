import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from swing_counter import SwingCounter


def test_basic_swings():
    # Simulated acceleration values with two clear swings
    samples = [0, 2, 10, 15, 25, 10, 4, 2, 0, 0, 5, 18, 22, 8, 3]
    counter = SwingCounter(high_threshold=20, low_threshold=5)
    assert counter.count_swings(samples) == 2


def test_no_false_positive_when_high_not_followed_by_low():
    samples = [0, 21, 22, 23, 25, 30]  # never drops below low_threshold
    counter = SwingCounter(high_threshold=20, low_threshold=5)
    assert counter.count_swings(samples) == 0


def test_invalid_thresholds():
    with pytest.raises(ValueError):
        SwingCounter(high_threshold=10, low_threshold=10)
