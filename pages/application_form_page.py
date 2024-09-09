from pages.base_page import BasePage


class ApplicationFormPage(BasePage):

    def switch_to_application_tab(self):
        self.switch_to_new_tab()


    def is_lever_in_url(self):
        return "lever.co" in self.driver.current_url