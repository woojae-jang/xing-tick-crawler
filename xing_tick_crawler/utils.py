import os


def make_dir(path: str):
    if path == '.':
        return
    if not is_exist(path):
        os.mkdir(path)


def is_exist(path: str) -> bool:
    return os.path.exists(path)
