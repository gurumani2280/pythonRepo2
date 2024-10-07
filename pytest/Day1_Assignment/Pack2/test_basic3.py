import pytest

def test3(precondition):
    print("This is test2 method")


@pytest.fixture()
def precondition():
    print("This precondition will execute before the test method")
    yield
    print("This statement will execute after test method execution")


    