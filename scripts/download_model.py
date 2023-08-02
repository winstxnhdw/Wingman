from huggingface_hub import snapshot_download


def download_model():
    """
    Summary
    -------
    download the model from Huggingface Hub
    """
    snapshot_download(
        'winstxnhdw/replit-code-v1-3b-ct2-int8',
        local_dir='bin',
        local_dir_use_symlinks=False
    )


if __name__ == '__main__':
    download_model()
