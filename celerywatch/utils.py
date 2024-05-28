import ast


def convert_args_safely(r: str | None, k: str | None):
    args = None
    kwargs = None
    if r:
        args = ast.literal_eval(f"({r},)" if ',' not in r else f"({r})")
    if k:
