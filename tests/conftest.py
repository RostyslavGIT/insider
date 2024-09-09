import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
from dotenv import load_dotenv
import shutil
from pathlib import Path
from pages.base_page import BasePage
import logging
from api.crud_api import CRUDAPI

load_dotenv()

# Adding custom markers for API and UI tests
def pytest_configure(config):
    config.addinivalue_line("markers", "api: mark test as API test")
    config.addinivalue_line("markers", "ui: mark test as UI test")

# Custom command-line option to select between API or UI tests and select custom browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests (chrome or firefox)")
    parser.addoption("--tests", action="store", default="all", help="Specify tests to run: api, ui, or all")

# Helper function to get browser driver based on command-line argument
def get_browser_driver(browser):
    if browser == "chrome":
        options = ChromeOptions()
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    return driver


# Fixture to handle browser driver for UI tests
@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    driver = get_browser_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_sessionstart():
    screenshots_dir = Path('screenshots')
    if os.path.exists(screenshots_dir):
        shutil.rmtree(screenshots_dir)
    os.makedirs(screenshots_dir)


def pytest_runtest_makereport(item, call):
    if call.when == 'call' and call.excinfo is not None:
        if 'driver' in item.fixturenames:
            driver = item.funcargs['driver']
            base_page = BasePage(driver)
            base_page.capture_screenshot(name=f"failure_{item.name}")


@pytest.fixture(scope='session')
def api_client():
    base_url = os.getenv('URL_API')
    return CRUDAPI(base_url)


# Hook to skip tests based on the --tests argument
def pytest_collection_modifyitems(config, items):
    selected_tests = config.getoption("--tests")
    if selected_tests == "api":
        skip_ui = pytest.mark.skip(reason="Skipping UI tests")
        for item in items:
            if "ui" in item.keywords:
                item.add_marker(skip_ui)
    elif selected_tests == "ui":
        skip_api = pytest.mark.skip(reason="Skipping API tests")
        for item in items:
            if "api" in item.keywords:
                item.add_marker(skip_api)