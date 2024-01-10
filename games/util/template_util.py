"""
Jinja2 templating utilities.
"""
from jinja2 import Environment, FileSystemLoader
from jinja2.environment import Template


def get_template(file_name: str) -> Template:
    """
    Get jinja2 template

    :param file_name: jinja2 template file name
    :return: jinja2 template
    """
    env = Environment(
        loader=FileSystemLoader("games/templates"),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    return env.get_template(file_name)

