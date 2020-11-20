
import random

from prefect import task, Flow
from prefect.environments.storage import GitHub

@task
def random_number():
    return random.randint(0, 100)

with Flow("test-flow") as flow:
    random_number()

flow.storage = GitHub(
    repo="https://github.com/benson-w/prefect-test",
    path="/flows/flow.py"
)

