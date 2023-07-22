from ctransformers import AutoModelForCausalLM

from server.features.generator.config import GeneratorConfig
from server.features.generator.prompt_template import PromptTemplate


class Generator:
    """
    Summary
    -------
    a static class for generating text

    Attributes
    ----------
    llm (LLM) : the language model instance

    Methods
    -------
    generate(prompt: str) -> str:
        generate text from a prompt
    """
    prompt_template = PromptTemplate('main')
    llm = AutoModelForCausalLM.from_pretrained('bin', model_type="replit")

    generator_config = GeneratorConfig(
        top_k=50,
        top_p=0.9,
        temperature=0.2,
        repetition_penalty=1.0,
        max_new_tokens=512,
        seed=42,
        stop=["<|endoftext|>"],
        reset=True
    )

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
        formatted_prompt = cls.prompt_template.format_prompt(prompt)

        stream = cls.llm._stream(  # pylint: disable=protected-access
            formatted_prompt,
            **cls.generator_config._asdict()
        )

        return ''.join(stream)
