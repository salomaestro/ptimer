from .timer import Timer


def test_ctx_mgr():
    from time import sleep
    with Timer() as t:
        sleep(1)
    assert t.elapsed >= 1
    assert t.name is None
