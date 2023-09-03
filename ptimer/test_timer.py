from .timer import Timer


def test_ctx_mgr():
    from time import sleep
    with Timer() as t:
        sleep(1)
    assert t.elapsed >= 1
    assert t.name is None


def test_explainer():
    with Timer("test", explainer="Time taken") as t:
        pass
    assert t.name == "test"
    assert t.explainer == "Time taken"


def test_fmt():
    def fmt(x): return f'{x} seconds'
    with Timer(time_fmt=fmt) as t:
        pass

    assert t.time_fmt == fmt
