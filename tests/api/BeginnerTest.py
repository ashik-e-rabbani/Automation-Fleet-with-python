import requests

"""
Overview of How Pytest Discovers Test Functions:

1. Default Naming Convention:
   - Pytest looks for functions whose names start with "test_" or end with "_test".
     For example, test_function() or my_test_function().

2. In Test Modules:
   - Pytest looks for test functions in Python modules.
   - Test modules are files named with the pattern test_*.py or *_test.py.
     For example, test_my_module.py.

3. In Test Classes:
   - Pytest identifies test methods within test classes.
   - Test classes should be named with the "Test" prefix or suffix.
     For example, TestClass or MyClassTest.

4. Custom Markers:
   - Custom markers can tag specific functions or classes as tests.
   - Markers can be defined in test code or configuration files.

5. Command-Line Options:
   - You can use command-line options to select specific tests or directories for discovery.
     For example: pytest test_directory.

6. Configuration Files:
   - Pytest can use configuration files (e.g., pytest.ini) to specify additional discovery rules.

7. Plugins:
   - Pytest has a rich ecosystem of plugins that extend or customize test discovery.
   - Plugins may provide additional markers, fixtures, or discovery mechanisms.

8. Recursion:
   - By default, pytest recursively searches for test modules and functions in subdirectories.
   - Control the depth of recursion using command-line options.

During the test discovery phase, pytest builds a collection of test items, including test functions, classes, and fixtures.
This collection is used for executing the tests.

Example Directory Structure:
project/
|-- tests/
|   |-- test_example.py
|-- src/
|   |-- module.py

In this example, running pytest in the tests directory will automatically discover and run the test functions in test_example.py.
"""

# Define the base URL for your API
BASE_URL = "https://demoqa.com/"


def test_get_request():
    # Send a GET request to the API endpoint
    response = requests.get(BASE_URL + "books")

    # Assert the response status code
    assert response.status_code == 200, "Success"


def test_get_request_multi_assertions():
    response = requests.get(BASE_URL + "books")

    # Assert the response status code and show a message
    assert response.status_code == 200, "Success"
    assert isinstance(response.status_code, str), "Result shouldn't be an string"


# As this function doesn't follow the naming convention test will not be executed by default by pytest.
def improperTest_function():
    response = requests.get(BASE_URL + "books")
    assert response.status_code == 200, "Success"

