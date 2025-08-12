"""Utility for counting golf swings from acceleration samples."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass
class SwingCounter:
    """Counts golf swings based on acceleration magnitude samples.

    The algorithm tracks when the acceleration crosses above a high
    threshold and then falls below a low threshold (hysteresis). Each
    such cycle is counted as one swing.
    """

    high_threshold: float = 20.0
    low_threshold: float = 5.0

    def __post_init__(self) -> None:
        if self.low_threshold >= self.high_threshold:
            raise ValueError("low_threshold must be less than high_threshold")
        self._seen_high = False
        self.count = 0

    def process_sample(self, value: float) -> None:
        """Process a single acceleration sample."""
        if not self._seen_high:
            if value > self.high_threshold:
                self._seen_high = True
        else:
            if value < self.low_threshold:
                self.count += 1
                self._seen_high = False

    def count_swings(self, samples: Iterable[float]) -> int:
        """Count swings in an iterable of samples.

        Parameters
        ----------
        samples:
            Iterable of acceleration magnitudes.
        """
        for value in samples:
            self.process_sample(value)
        return self.count
