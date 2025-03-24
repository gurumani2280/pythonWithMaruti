import pytest

def test_method1(teardown_tearup):
    print("This is my first test method in pytest")

@pytest.fixture()
def teardown_tearup():
    print("This will run before the test method")
    yield
    print("This will run after the test method")

#Note: pytest will automatically search for any program file starting or ending with test and methods with test and execute those testcases.

'''
output:
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_01\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_01
configfile: pytest.ini
collected 1 item                                                                                                                                                                                                                   

Day_01_test_01/test_01.py::test_method1 This will run before the test method
This is my first test method in pytest
PASSEDThis will run after the test method
'''