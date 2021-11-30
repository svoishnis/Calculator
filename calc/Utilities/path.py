from pathlib import Path


def path(filepath):
    relative = Path(filepath)
    return relative.absolute()
