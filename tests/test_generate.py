# pylint: disable=missing-function-docstring,redefined-outer-name

from fastapi.testclient import TestClient
from pytest import fixture

from server import initialise


@fixture()
def client():
    return TestClient(next(initialise()))


def test_generate(client: TestClient):
    response = client.post('/v1/generate', json={
        'prompt': 'Create a Python function that returns the sum of two numbers'
    }).json()

    assert "def" in response['text']
