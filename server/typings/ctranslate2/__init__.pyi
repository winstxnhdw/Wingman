# pylint: skip-file

from typing import Callable, Literal, overload

ComputeTypes = Literal[
    'default',
    'auto',
    'int8',
    'int8_float16',
    'int8_bfloat16',
    'int16',
    'float16',
    'bfloat16',
    'float32',
]

Devices = Literal['cpu', 'cuda', 'auto']

class GenerationStepResult:
    batch_id: int
    is_last: bool
    log_prob: float | None
    step: int
    token: str
    token_id: int


class GenerationResult:
    scores: list[float]
    sequences: list[list[str]]
    sequences_ids: list[int]


class AsyncGenerationResult:

    def done(self) -> bool: ...

    def result(self) -> GenerationResult: ...


class Generator:
    device: Devices

    def __init__(
        self,
        model_path: str,
        device: Devices = 'cpu',
        *,
        device_index: int | list[int] = 0,
        compute_type: ComputeTypes = 'default',
        inter_threads: int = 0,
        intra_threads: int = 0,
        max_queued_batches: int = 0,
        files: object = None
    ) -> None: ...


    @overload
    def generate_batch(
        self,
        start_tokens: list[list[str]],
        *,
        max_batch_size: int = 0,
        batch_type: str = 'examples',
        asynchronous: Literal[False] = False,
        beam_size: int = 1,
        patience: float = 1,
        num_hypotheses: int = 1,
        length_penalty: float = 1,
        repetition_penalty: float = 1,
        no_repeat_ngram_size: int = 0,
        disable_unk: bool = False,
        suppress_sequences: list[list[str]] | None = None,
        end_token: str | list[str] | list[int] | None = None,
        return_end: bool = False,
        max_length: int = 512,
        min_length: int = 0,
        static_prompt: list[str] | None = None,
        cache_static_prompt: bool = True,
        include_prompt_in_result: bool = True,
        return_scores: bool = False,
        return_alternatives: bool = False,
        min_alternative_expansion_prob: float = 0,
        sampling_topk: int = 0,
        sampling_topp: float = 0,
        sampling_temperature: float = 1,
        callback: Callable[[GenerationStepResult], bool] | None = None,
    ) -> list[GenerationResult]: ...


    @overload
    def generate_batch(
        self,
        start_tokens: list[list[str]],
        *,
        max_batch_size: int = 0,
        batch_type: str = 'examples',
        asynchronous: Literal[True],
        beam_size: int = 1,
        patience: float = 1,
        num_hypotheses: int = 1,
        length_penalty: float = 1,
        repetition_penalty: float = 1,
        no_repeat_ngram_size: int = 0,
        disable_unk: bool = False,
        suppress_sequences: list[list[str]] | None = None,
        end_token: str | list[str] | list[int] | None = None,
        return_end: bool = False,
        max_length: int = 512,
        min_length: int = 0,
        static_prompt: list[str] | None = None,
        cache_static_prompt: bool = True,
        include_prompt_in_result: bool = True,
        return_scores: bool = False,
        return_alternatives: bool = False,
        min_alternative_expansion_prob: float = 0,
        sampling_topk: int = 0,
        sampling_topp: float = 0,
        sampling_temperature: float = 1,
        callback: Callable[[GenerationStepResult], bool] | None = None,
    ) -> list[AsyncGenerationResult]: ...
