import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from pages.application_form_page import ApplicationFormPage
import os
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.ui
def test_navigate_and_verify_careers(driver):
    URL = os.getenv('URL')
    driver.get(URL)
    home_page = HomePage(driver)
    home_page.navigate_to_careers()
    careers_page = CareersPage(driver)
    careers_page.verify_sections_displayed()


@pytest.mark.ui
def test_filter_and_verify_qa_jobs(driver):
    URL = os.getenv('URL_QA')
    driver.get(URL)
    qa_jobs_page = QAJobsPage(driver)
    qa_jobs_page.click_see_all_qa_jobs()
    qa_jobs_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")
    qa_jobs_page.scroll_to_job_listings()
    qa_jobs_page.verify_jobs("Istanbul, Turkey", "Quality Assurance")
    qa_jobs_page.hover_and_click_view_role()
    application_form_page = ApplicationFormPage(driver)
    application_form_page.switch_to_application_tab()
    assert application_form_page.is_lever_in_url(), "The URL does not contain 'lever.co'."
