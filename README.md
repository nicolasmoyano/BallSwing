# BallSwing

Utility to count golf swings from acceleration data.

## Usage

The `swing_counter` module provides a `SwingCounter` class that counts swings
based on acceleration magnitude samples. Swings are detected when the
acceleration exceeds a high threshold and subsequently falls below a low
threshold.

```python
from swing_counter import SwingCounter

samples = [0, 2, 10, 15, 25, 10, 4, 2]
counter = SwingCounter(high_threshold=20, low_threshold=5)
print(counter.count_swings(samples))
```
