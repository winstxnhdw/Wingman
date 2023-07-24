from sys import argv

from download_model import download_model
from PyInstaller.__main__ import run


def main():
    """
    Summary
    -------
    download the model from Huggingface Hub
    """
    if len(argv) < 2 or argv[1] != '--skip-download':
        download_model()

    run([
        'main.spec',
        '--noconfirm'
    ])


if __name__ == '__main__':
    main()
