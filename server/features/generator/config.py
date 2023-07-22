from typing import NamedTuple


class GeneratorConfig(NamedTuple):
    """
    Summary
    -------
    the generator config

    Attributes
    ----------
    top_k (int) : the top-k value to use for sampling
    top_p (float) : the top-p value to use for sampling
    temperature (float) : the temperature to use for sampling
    repetition_penalty (float) : the repetition penalty to use for sampling
    last_n_tokens (int) : the number of last tokens to use for repetition penalty
    seed (int) : the seed to use for sampling tokens
    max_new_tokens (int) : the maximum number of new tokens to generate
    stop (list[str]) : a list of sequences to stop generation when encountered
    reset (bool) : whether to reset the model state before each generation
    batch_size (int) : the batch size to use for evaluating tokens
    threads (int) : the number of threads to use for evaluating tokens
    """
    top_k: int = 40
    top_p: float = 0.95
    temperature: float = 0.8
    repetition_penalty: float = 1.1
    last_n_tokens: int = 64
    seed: int = -1
    max_new_tokens: int = 256
    stop: list[str] | None = None
    reset: bool = True
    batch_size: int = 8
    threads: int = -1
