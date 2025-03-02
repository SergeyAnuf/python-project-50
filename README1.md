### Hexlet tests and linter status:

[![Actions Status](https://github.com/lyovaparsyan94/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/lyovaparsyan94/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/211f3fb05430bee114cc/maintainability)](https://codeclimate.com/github/lyovaparsyan94/python-project-50/maintainability)
[![my_check](https://github.com/lyovaparsyan94/python-project-50/actions/workflows/my_workflow.yml/badge.svg)](https://github.com/lyovaparsyan94/python-project-50/actions/workflows/my_workflow.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/211f3fb05430bee114cc/test_coverage)](https://codeclimate.com/github/lyovaparsyan94/python-project-50/test_coverage)

# Difference Calculator (gendiff)

- gendiff is a command-line tool for finding differences between files. This is the second project developed as part of
  the Hexlet course.

***

## Requirements:

[Python 3.13 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)
***

## Installation:

``` 
git clone git@github.com:lyovaparsyan94/python-project-50.git
```

````
cd python-project-50
````

`````
uv build
``````

````````
uv tool install dist/*.whl
````````

***

## Supported File Formats

#### - JSON (.json)

#### - YAML (.yaml, .yml)

***

## Usage

1. Place the files you want to compare inside the tests/test_data directory.
2. Run the following command, replacing file1 and file2 with your actual file names:

````
uv run gendiff tests/test_data/<file1> tests/test_data/<file2>
````

3. By default, the output is formatted using the stylish formatter.

- To use a different format (json or plain), specify it with the -f flag:

***

### Пример вывода инструмента при использовании разных форматтеров:

- **Default (stylish) formatter:**

````
uv run gendiff tests/test_data/<file1> tests/test_data/<file1>
````

- **Using the JSON formatter:**

``````
uv run gendiff -f stylish tests/test_data/<file1> tests/test_data/<file1>
``````

- **Using the Plain formatter:**

``````
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file1>
``````

## Development and Testing
### Linting
Run ruff to check for linting issues:
```
make lint
```
Running Tests
```
make test-coverage
```