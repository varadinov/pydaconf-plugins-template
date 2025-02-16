# {{ cookiecutter.short_description }}

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/ci.yaml)
![GitHub last commit](https://img.shields.io/github/last-commit/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
![GitHub](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![downloads](https://static.pepy.tech/badge/{{ cookiecutter.project_slug }}/month)](https://pepy.tech/project/{{ cookiecutter.project_slug }})
![PyPI - Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }})

## Pydaconf 
For more information about Pydaconf see the [Docs](https://varadinov.github.io/pydaconf/).

## Installation
Install using `pip install {{ cookiecutter.project_slug }}`  

## A Simple Example
* Create config file in toml, yaml or json
```yaml
secret: {{ cookiecutter.plugin_prefix }}:///secret_name=my-secret
```

* Create Pydantic Model and load the configuration
```python
from pydaconf import PydaConf
from pydantic import BaseModel


class Config(BaseModel):
    secret: str

provider = PydaConf[Config]()
provider.from_file("config.yaml")
print(provider.config.secret)
```

## Supported parameters
Parameters can be passed in the configuration value in the following format:
```
{{ cookiecutter.plugin_prefix }}:///param1=value1,param2=value2
```

| Parameter | Description                |
|-----------|----------------------------|
| param1    | The description of param 1 |
| param2    | The description of param 2 |