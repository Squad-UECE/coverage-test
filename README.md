# teste coverage

![coverage badge](./coverage.svg)

This repository is a simple example of how to apply coverage test in your project using `pytest` and `pytest-cov`

## Installation

```shell
poetry install
poetry shell
```

## Run coverage pytest

Run: 
```shell
pytest --cov-config=.coveragerc --cov=coverage_study tests
coverage-badge -f -o coverage.svg
```
or using Makefile:
```shell
make coverage
```
This will create a `.coverage` and `coverage.svg` file.

## Using badge

Put this in your README.md

```md
![coverage badge](./coverage.svg)
```