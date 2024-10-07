import pytest

def test5(precondition):
    print("This is test5 method")
    print("Precondition ", precondition)


@pytest.fixture()
def precondition():
    print("This precondition will execute before the test method")
    yield 4
    print("This statement will execute after test method execution")


    