from collections.abc import Callable
from pydaconf.plugins.base import PluginBase


class {{ cookiecutter.plugin_name }}Plugin(PluginBase):
    """{{ cookiecutter.project_name }} plugin. Loads variables based on prefix {{ cookiecutter.plugin_prefix.upper() }}:///"""

    PREFIX='{{ cookiecutter.plugin_prefix.upper() }}'

    def run(self, value: str, on_update_callback: Callable[[str], None]) -> str:
        return value

