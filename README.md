## How to run

First, create a folder called `instance` in the project root directory.

Then:

- Method 1: Use Poetry
    1. Enter a poetry shell by `poetry shell`
    2. `poetry install`
- Method 2: Use pip
    1. Create a virtualenv by `python -m venv venv`
    2. Enter the virtualenv by `source venv/bin/activate`
    3. `pip install -e .`

Finally:

```
flask --app interview_inco init-db
flask --app interview_inco run
```
