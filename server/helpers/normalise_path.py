import sys
from pathlib import Path


def normalise_path(path: str) -> str:
    """
    Summary
    -------
    returns the correct path for the current environment

    Parameters
    ----------
    path (str) : the path to normalise

    Returns
    -------
    normalised_path (str) : the normalised path
    """
    path = str(Path(path))

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        path = str(Path(
            f'{sys._MEIPASS}/{path}').resolve() # pylint: disable=protected-access # type: ignore
        )

    return path
