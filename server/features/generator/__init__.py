from typing import Literal

from ctranslate2 import Generator as CTranslateGenerator
from transformers import AutoTokenizer

from server.helpers import normalise_path


class Generator:
    """
    Summary
    -------
    a static class for generating text

    Attributes
    ----------
    generator (Generator) : the CTranslate2 generator
    tokeniser (AutoTokenizer) : the HuggingFace tokeniser

    Methods
    -------
    generate(prompt: str) -> str:
        generate text from a prompt

    toggle_device():
        toggle between `cpu` and `cuda` devices
    """
    model_path = normalise_path('bin')
    generator = CTranslateGenerator(model_path, compute_type='auto')
    tokeniser = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

    @classmethod
    def generate(cls, prompt: str) -> str:
        """
        Summary
        -------
        generate text from a prompt

        Parameters
        ----------
        prompt (str) : the prompt to generate text from

        Returns
        -------
        generated_text (str) : the generated text
        """
        if isinstance(tokens := cls.tokeniser.convert_ids_to_tokens(cls.tokeniser.encode(prompt)), str):
            tokens = [tokens]

        results = cls.generator.generate_batch([tokens], max_length=100, sampling_topk=10)

        return cls.tokeniser.decode(results[0].sequences_ids[0])


    @classmethod
    def toggle_device(cls) -> Literal['cpu', 'cuda', 'auto']:
        """
        Summary
        -------
        toggle between `cpu` and `cuda` devices

        Returns
        -------
        device (Devices) : the device that the generator is now using
        """
        cls.generator = CTranslateGenerator(cls.model_path, device='cuda' if cls.generator.device == 'cpu' else 'cpu')
        return cls.generator.device
