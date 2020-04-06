# xqdm

tqdm wrapper for multiprocessing

## Usage

- Usage and parameters are similar with `tqdm`.
- There are additional new parameters `func` and `num_workers`. `func` parameter is necesary.
- `iterable` parameter became necessary.

Because of Python's multiprocessing problem, `func` parameter could not accept `lambda` type.

## Usage Example

```python
import time
import xqdm

def square(x):
  time.sleep(0.5)
  return x**2

xqdm(square, range(10), num_workers=2, desc='hello world')
```

the result is

```
hello world: 100%|██████████████████████████████████████████████████| 10/10 [00:02<00:00,  3.99it/s]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Since `squre()` have `0.5sec` runtime and there are two worker, progressbar have approximately ideal speed of `4.00it/s`.

## Installation

There is no pip installation support.
