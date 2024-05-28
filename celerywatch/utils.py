import ast


def convert_args_safely(r: str | None, k: str | None):
    args = None
    kwargs = None
