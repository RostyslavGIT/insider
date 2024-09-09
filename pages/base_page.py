from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from config.logger import logger as log
from pathlib import Path
from time import sleep

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, locator, timeout=10):
        log.debug(f"Finding element with locator: {locator} and timeout: {timeout}")
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))


    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))


    def click(self, locator, timeout=10):
        log.debug(f"Clicking element with locator: {locator} and timeout: {timeout}")
        element = self.find_element(locator, timeout)
        element.click()
        log.debug("Clicked element successfully.")


    def get_text(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        return element.text


    def select_from_dropdown(self, locator, value, timeout=10):
        log.debug(f"Selecting '{value}' from dropdown with locator: {locator}")
        element = self.find_element(locator, timeout)
        select = Select(element)
        option_locator = (By.XPATH, f"//select[@name='{element.get_attribute('name')}']//option[text()='{value}']")
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(option_locator))
        sleep(2)
        select.select_by_visible_text(value)
        log.debug(f"Selected '{value}' successfully.")


    def hover_over_element(self, locator, timeout=10):
        log.debug(f"Hovering over element with locator: {locator}")
        element = self.find_element(locator, timeout)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        log.debug(f"Hovered over element with locator: {locator}")


    def switch_to_new_tab(self):
        log.debug("Switching to the newly opened tab.")
        self.driver.switch_to.window(self.driver.window_handles[-1])
        log.debug("Switched to the new tab.")


    def scroll_to_element(self, locator):
        log.debug(f"Scrolling to the element with locator: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        log.debug(f"Scrolled to the element with locator: {locator}")


    def capture_screenshot(self, name="screenshot"):
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshots_dir = Path('screenshots')
        screenshots_dir.mkdir(parents=True, exist_ok=True)
        screenshot_path = os.path.join(screenshots_dir, screenshot_name)
        self.driver.get_screenshot_as_file(screenshot_path)
        log.info(f"Screenshot captured: {screenshot_path}")

