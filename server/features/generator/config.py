from typing import TypedDict


class GeneratorConfig(TypedDict, total=False):
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
    top_k: int
    top_p: float
    temperature: float
    repetition_penalty: float
    last_n_tokens: int
    seed: int
    max_new_tokens: int
    stop: list[str] | None
    reset: bool
    batch_size: int
    threads: int
