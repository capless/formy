from envs import env
from jinja2 import Environment
from jinja2.loaders import ChoiceLoader, PackageLoader


def get_loaders():
    """
    Get the Jinja2 loaders for the project.
    Returns: list
    """
    loaders = [
        PackageLoader('formy', 'templates')
    ]
    for i in env('TEMPLATE_PACKAGES', [], var_type='list'):
        loaders.append(PackageLoader(i))
    return loaders


temp_env = Environment(loader=ChoiceLoader(get_loaders()))