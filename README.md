### Hexlet tests and linter status:
[![Actions Status](https://github.com/SergeyAnuf/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SergeyAnuf/python-project-50/actions)

https://asciinema.org/a/e9B8ZfyRFvZUCF9Y0ztqjCEAq

https://asciinema.org/a/E4nbkH6IjMVxUqW5C71x3TxKW

https://asciinema.org/a/e3xQEzSLAJpeMkLux2Vb1YAzl

https://asciinema.org/a/Vm3epGYEkJVz7ceAu73a6Rlum

# Difference Calculator (gendiff)

- gendiff is a command-line tool for finding differences between files. This is the second project developed as part of
  the Hexlet course.

***

## Requirements:

[Python 3.12 +] - (https://www.python.org/downloads/)

[UV 0.5.11 +] - (https://astral.sh)
***

## Installation:

``` 
git clone git@github.com:SergeyAnuf/python-project-50.git
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

1. Place the files you want to compare inside the tests/fixtures directory.
2. Run the following command, replacing file1 and file2 with your actual file names:

````
uv run gendiff tests/fixtures/<file1> tests/fixtures/<file2>
````

3. By default, the output is formatted using the stylish formatter.

- To use a different format (json or plain), specify it with the -f flag:

***

### Пример вывода инструмента при использовании разных форматтеров:

- **Default (stylish) formatter:**

````
uv run gendiff tests/fixtures/<file1> tests/fixtures/<file1>
````

- **Using the JSON formatter:**

``````
uv run gendiff -f stylish tests/fixtures/<file1> tests/fixtures/<file1>
``````

- **Using the Plain formatter:**

``````
uv run gendiff -f plain tests/fixtures/<file1> tests/fixtures/<file1>
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
