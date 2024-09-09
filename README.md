1. First, install the necessary libraries:

pip install pytest
pip install allure-pytest
pip install selenium
pip install python-dotenv
pip install selenium
pip install requests

2. 'tests/conftest.py' contains fixtures for setting up and tearing down the WebDriver instance.

3: Running Tests with Allure Reporting:

Run all the tests with Pytest with Allure report:
pytest --alluredir=reports/allure -s

Run tests only in Chrome:
pytest --browser=chrome --alluredir=reports/allure -s

Run tests only in Firefox:
pytest --browser=firefox --alluredir=reports/allure -s

Run all tests (both API and UI):
pytest -v

Run only API tests:
pytest -v --tests=api

Run only UI tests:
pytest -v --tests=ui

Generate Allure report for API tests:
pytest --alluredir=reports/api --tests=api
allure serve reports/api

Generate Allure report for UI tests:
pytest --alluredir=reports/ui --tests=ui
allure serve reports/ui

Generate the Allure report:
allure serve reports/allure
