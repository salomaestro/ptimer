from time import perf_counter


class Timer:
    """Timer context manager.

    Supply a name to a section of code to be timed within a file and this class will time it
    using python-time's perf_counter.

    Attributes:
    name: str
    explainer: str
    time_fmt: str | Callable

    Methods:
    time_fmt_ms: Callable
    time_fmt_s: Callable
    time_fmt_m: Callable

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
    """

    def __init__(self, name: str = None, **kwargs):
        """Timer context manager.

        Supply a name to a section of code to be timed within a file and this class will time it
        using python-time's perf_counter.

        Args:
            name (str, optional): Name of the section of code to be timed. Defaults to None.

        Keyword Args:
            explainer (str, optional): Explainer text to be printed before the name and time. Defaults to "Elapsed time for ".
            time_fmt (str | Callable, optional): Format of the time to be printed. Defaults to "time_fmt_ms".

        Raises:
            AttributeError: If time_fmt is not a valid option.
        """

        self.name = name
        self.elapsed = None

        self._expl = f"Elapsed time for {self.name}: "
        self._fmts = {
            "time_fmt_ms": self.time_fmt_ms,
            "time_fmt_s": self.time_fmt_s,
            "time_fmt_m": self.time_fmt_m
        }

        self.explainer = kwargs.get("explainer", self._expl)
        self.time_fmt = kwargs.get("time_fmt", self._fmts["time_fmt_ms"])

        if type(self.time_fmt) is str:
            if self.time_fmt in self._fmts:
                self.time_fmt = self._fmts[self.time_fmt]
            else:
                raise AttributeError(
                    f"Attribute {self.time_fmt} not found. Pass in either an callable or str")

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, *args):
        self.end = perf_counter()
        self.elapsed = self.end - self.start

        if self.name is None:
            print(f"Elapsed time: {self.time_fmt(self.elapsed)}")
            return

        print(f"{self.explainer}{self.time_fmt(self.elapsed)}")

    @staticmethod
    def time_fmt_s(time):
        return f"{time:.4} s"

    @staticmethod
    def time_fmt_ms(time):
        return f"{time*1e3:.4} ms"

    @staticmethod
    def time_fmt_m(time):
        minutes = time // 60
        seconds = time % 60
        return f"{int(minutes)}m{seconds:.3}s"


if __name__ == "__main__":
    with Timer("my test", time_fmt="time_fmt_m"):
        for i in range(1000000):
            i = i + 1
