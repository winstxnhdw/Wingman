from typing import Generator


def load_file(path: str) -> Generator[str, None, None]:
    """
    Summary
    -------
    load a file from a path

    Parameters
    ----------
    path (str): path to file

    Yields
    ------
    content (str): content of file
    """
    with open(path, encoding='utf-8') as file:
        yield from file
