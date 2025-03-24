class TestClass1:
    def test_feature1(self):
        print("This is test feature 1")

'''
commands:
pytest will discover all files, class, methods starting with test
pytest -> gives basic info
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 2 items                                                                                                                                                                                                                  
Day_0_test_0\\test_01.py .                                                                                                                                                                                                    [ 50%] 
Day_0_test_0\\test_02.py . 

pytest -v -> Along with methods and classes
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 2 items                                                                                                                                                                                                                  
Day_0_test_0\\test_01.py .                                                                                                                                                                                                    [ 50%] 
Day_0_test_0\\test_02.py . 

pytest -v -s -> gives output along with methods and classes
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 2 items                                                                                                                                                                                                                  
Day_0_test_0/test_01.py::test_method1 This is my first test method in pytest
PASSED
Day_0_test_0/test_02.py::TestClass1::test_feature1 This is test feature 1
PASSED

pytest -v -s -k "feature" -> This is used for pattern matching. It will search for all methods having text feature
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 2 items / 1 deselected / 1 selected                                                                                                                                                                                      
Day_0_test_0/test_02.py::TestClass1::test_feature1 This is test feature 1
PASSED

pytest -v -s Day_0_test_0\\test_02.py
platform win32 -- Python 3.10.11, pytest-8.3.5, pluggy-1.5.0 -- C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0\\.venv\\Scripts\\python.exe
cachedir: .pytest_cache
rootdir: C:\\Users\\USER\\Desktop\\python_selenium_automation\\PyTest_project\\Day_0
collected 1 item                                                                                                                                                                                                                   
Day_0_test_0/test_02.py::TestClass1::test_feature1 This is test feature 1
PASSED
'''