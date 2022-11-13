# ptimer
Simple timer context manager for timing sections of python code

## Installation

```bash
pip install git+https://github.com/salomaestro/ptimer.git
```

## Documentation

Provides a `Timer` class:

```python
ptimer.Timer(name=None, **kwargs)

Args:
    name (str, optional): Name of the section of code to be timed. Defaults to None.
        
Keyword Args:
    explainer (str, optional): Explainer text to be printed before the name and time. Defaults to "Elapsed time for ".
    time_fmt (str | Callable, optional): Format of the time to be printed. Defaults to "time_fmt_ms".

Raises:
    AttributeError: If time_fmt is not a valid option.

Examples:
>>> with Timer('test'):
...     for i in range(1000000):
...         pass
...
Elapsed time for test: 0.0ms

>>> with Timer('test', explainer='Time taken: ', time_fmt='time_fmt_s'):
...     for i in range(1000000):
...         pass
...
Time taken: test 0.0s

>>> with Timer('test', explainer='Time taken: ', time_fmt=lambda x: f'{x} seconds'):
...     for i in range(1000000):
...         pass
...
Time taken: test 0.0 seconds
```