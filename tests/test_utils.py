from celerywatch.utils import convert_args_safely


def test_convert_args_none():
    args, kwargs = convert_args_safely(None, None)
    assert args is None
    assert kwargs is None


def test_convert_single_arg():
    args, kwargs = convert_args_safely("1", None)
    assert args == (1,)
    assert kwargs is None


def test_convert_multiple_args():
    args, kwargs = convert_args_safely("1, 'x'", None)
    assert args == (1, "x")
    assert kwargs is None


def test_convert_kwargs():
    args, kwargs = convert_args_safely(None, "a=2, b='ok'")
    assert args is None
    assert kwargs == {"a": 2, "b": "ok"}


def test_convert_args_and_kwargs():
    args, kwargs = convert_args_safely("True", "n=3")
    assert args == (True,)
    assert kwargs == {"n": 3}
