# Test examples
A repository of some simple testing examples to demo various test cases and
usage of mocking.

## Set up and requirements
Create a virtual environment and install from `requirements.txt`:

    pip install -U -r requirements.txt

Both Python 2 and 3 should work fine for these examples. `mock` is installed as
a requirement rather than standard library to run on Python 2.

## Running tests from console
Helper script:

    ./run.sh

Manually in bash:

    PYTHONPATH=. py.test

## Running independently or from an IDE
Set your `PYTHONPATH` environment variable to the root of the repository.
