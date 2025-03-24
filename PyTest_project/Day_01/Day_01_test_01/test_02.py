import pytest

class TestClass1:
    def test_feature1(self, setup_teardown):
        print("This is test feature 1")

    @pytest.fixture()
    def setup_teardown(self):
        print("This will run before the test_feature1 method")
        yield
        print("This will run after the test_feature1 method")


'''
output:
ERROR: When setup_teardown() is created without self argument. Note: self argument is mandatory for any method inside class.
___________________________________________________________________________________________ ERROR collecting Day_01_test_01/test_02.py ____________________________________________________________________________________________ 
invalid method signature

During handling of the above exception, another exception occurred:
Could not determine arguments of <bound method TestClass1.setup_teardown of <Day_01_test_01.test_02.TestClass1 object at 0x000001A8F8813790>>: invalid method signature
===================================================================================================== short test summary info ===================================================================================================== 
ERROR Day_01_test_01/test_02.py::TestClass1 - Failed: Could not determine arguments of <bound method TestClass1.setup_teardown of <Day_01_test_01.test_02.TestClass1 object at 0x000001A8F8813790>>: invalid method signature       
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
======================================================================================================== 1 error in 0.20s ========================================================================================================= 
(.venv) PS C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_01> pytest -v -s .\\Day_01_test_01\\test_02.py
======================================================================================================= test session starts =======================================================================================================
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_01\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_01
configfile: pytest.ini
collected 1 item                                                                                                                                                                                                                   

Day_01_test_01/test_02.py::TestClass1::test_feature1 This will run before the test_feature1 method
This is test feature 1
PASSEDThis will run after the test_feature1 method
'''