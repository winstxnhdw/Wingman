from sys import argv

from huggingface_hub import hf_hub_download
from PyInstaller.__main__ import run


def main():
    """
    Summary
    -------
    download the model from Huggingface Hub
    """
    if len(argv) < 2 or argv[1] != '--skip-download':
        hf_hub_download(
            'winstxnhdw/Replit-v2-CodeInstruct-3B-ggml-4bit',
            'model.bin',
            local_dir='bin',
            local_dir_use_symlinks=False
        )

    run([
        'main.spec',
        '--noconfirm'
    ])


if __name__ == '__main__':
    main()
