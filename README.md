[![Test Python](https://github.com/tkh/test-examples/actions/workflows/test-python.yml/badge.svg)](https://github.com/tkh/test-examples/actions/workflows/test-python.yml) [![Code Climate](https://codeclimate.com/github/tkh/test-examples/badges/gpa.svg)](https://codeclimate.com/github/tkh/test-examples)

# Test examples
A repository of some simple testing examples to demo various test cases and usage of
mocking.

## Set up and run

```bash
pipenv install
pipenv shell
PYTHONPATH=. pytest --cov --flake8 .
```
