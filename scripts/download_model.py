from huggingface_hub import hf_hub_download


def download_model():
    """
    Summary
    -------
    download the model from Huggingface Hub
    """
    hf_hub_download(
        'winstxnhdw/Replit-v2-CodeInstruct-3B-ggml-4bit',
        'model.bin',
        local_dir='bin',
        local_dir_use_symlinks=False
    )


if __name__ == '__main__':
    download_model()
