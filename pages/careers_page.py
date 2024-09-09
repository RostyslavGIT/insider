from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CareersPage(BasePage):
    LOCATIONS_SECTION = (By.XPATH, "//section//h3[contains(text(),'Our Locations')]")
    TEAMS_SECTION = (By.XPATH, "//section[@id='career-find-our-calling']//a[.='See all teams']")
    LIFE_SECTION = (By.XPATH, "//section//h2[contains(text(),'Life at Insider')]")


    def is_section_displayed(self, locator):
        try:
            elem = self.find_element(locator)
            return elem.is_displayed()
        except Exception as e:
            return False


    def verify_sections_displayed(self):
        assert self.is_section_displayed(self.LOCATIONS_SECTION), "Locations section is not displayed."
        assert self.is_section_displayed(self.TEAMS_SECTION), "Teams section is not displayed."
        assert self.is_section_displayed(self.LIFE_SECTION), "Life at Insider section is not displayed."