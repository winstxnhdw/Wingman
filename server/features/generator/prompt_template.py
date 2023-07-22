from typing import Literal

from server.helpers import load_file


class PromptTemplate:
    """
    Summary
    -------
    a template for the generator

    Attributes
    ----------
    template (str) : the template

    Methods
    -------
    format_prompt(prompt: str) -> str:
        format a prompt
    """
    def __init__(self, template_name: Literal['main']):

        template_generator = load_file(f'server/features/generator/templates/{template_name}.txt')
        self.template = ''.join(template_generator)


    def format_prompt(self, prompt: str) -> str:
        """
        Summary
        -------
        format a prompt

        Parameters
        ----------
        prompt (str) : the prompt to format

        Returns
        -------
        formatted_prompt (str) : the formatted prompt
        """
        formatted_prompt = self.template.format(prompt)
        return formatted_prompt
