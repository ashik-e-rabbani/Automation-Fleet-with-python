import pytest
import requests

"""
Fixtures are reusable components that help manage the test environment and provide a convenient way 
to share setup code across multiple tests. They can be used for repetitive tasks such as setting up databases, 
creating temporary files, or initializing objects.
"""

# Global status variable
status = 'Not Started!'

# Fixture definition
@pytest.fixture
def set_up():
    """
    Fixture to set up the environment by checking server activeness.
    It updates the global status variable to 'Started' after a successful request.
    """
    global status
    # Check for the server activeness
    response = requests.get("https://demoqa.com/")
    status = 'Started'
    return response.status_code


# Test using the fixture
def test_set_up(set_up):
    """
    Test function using the set_up fixture.
    It prints the fixture result, global status, and runs the test.
    """
    print(f"\nFixture result: {set_up}")
    print(f"Global status: {status}")
    print("Running test..")

    if set_up == 200:
        assert True
    else:
        assert False


# Fixture Attributes | Scope | name

@pytest.fixture(name="check_server")
def check_server():
    """
    Fixture to check server activeness without modifying the global status variable.
    """
    # Check for the server activeness
    response = requests.get("https://demoqa.com/")
    return response.status_code


def test_check_server(check_server):
    """
    Test function using the check_server fixture.
    It prints the fixture result, global status, and runs the test_check_server.
    """
    print(f"\nFixture result: {check_server}")
    print(f"Global status: {status}")
    print("Running test.. --> test_check_server")

    if check_server == 200:
        assert True
    else:
        assert False


# Fixture Attributes | Scope | params

@pytest.fixture(name="get_param", params=['I', 'Am', "Ashik"])
def get_param():
    """
    Parametrized fixture with three values: 'I', 'Am', 'Ashik'.
    """
    return True


def test_fixture_param(get_param):
    """
    Test function using the parametrized get_param fixture.
    It prints the fixture result, global status, and runs the test_fixture_param.
    """
    print(f"\nFixture result: {get_param}")
    print(f"Global status: {status}")
    print("Running test.. --> get_param")

    assert True


# Parametrize the fixture directly
@pytest.fixture(name="get_param")
def get_param(request):
    """
    Alternative way to parametrize the get_param fixture directly.
    """
    return request.param


@pytest.mark.parametrize("get_param", ['I', 'Am', 'Ashik'])
def test_fixture_param(get_param):
    """
    Test function using the parametrized get_param fixture.
    It prints the parameter value and runs the test_fixture_param.
    """
    print(f"Param value: {get_param}")
