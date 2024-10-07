import pytest

def test4(precondition):
    print("This is test4 method")
    print("Precondition ", precondition)


@pytest.fixture()
def precondition():
    print("This precondition will execute before the test method")
    yield
    print("This statement will execute after test method execution")


    