from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class QAJobsPage(BasePage):
    QA_JOBS_BUTTON = (By.XPATH, "//a[.='See all QA jobs']")
    LOCATION_FILTER = (By.XPATH, "//select[@id='filter-by-location']")
    DEPARTMENT_FILTER = (By.XPATH, "//select[@id='filter-by-department']")
    JOB_LIST = (By.XPATH, "//div[@id='jobs-list']/div")
    JOB_TITLE = (By.XPATH, "//p[contains(@class, 'position-title')]")
    VIEW_ROLE_BUTTON = (By.XPATH, "//a[.='View Role']")


    def click_see_all_qa_jobs(self):
        self.click(self.QA_JOBS_BUTTON)


    def filter_jobs(self, location, department):
        self.scroll_to_element(self.LOCATION_FILTER)
        self.select_from_dropdown(self.LOCATION_FILTER, location)
        self.select_from_dropdown(self.DEPARTMENT_FILTER, department)


    def verify_jobs(self, expected_location, expected_department):
        jobs = self.find_elements(self.JOB_LIST)
        for job in jobs:
            position = job.find_element(By.XPATH, "//p[contains(@class, 'position-title')]").text
            department = job.find_element(By.XPATH, "//span[contains(@class, 'position-department ')]").text
            location = job.find_element(By.XPATH, "//div[contains(@class, 'position-location')]").text
            assert "Quality Assurance" in position
            assert expected_department in department
            assert expected_location in location


    def hover_and_click_view_role(self):
        self.hover_over_element(self.JOB_TITLE)
        self.click(self.VIEW_ROLE_BUTTON)


    def scroll_to_job_listings(self):
        self.scroll_to_element(self.JOB_LIST)

