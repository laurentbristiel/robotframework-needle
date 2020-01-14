from needle.cases import NeedleTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestLogo(NeedleTestCase):

    def test_logo(self):
        self.driver.get('http://www.bbc.co.uk/news/')
        try:
                WebDriverWait(self.driver, 20).until(
                    ec.presence_of_element_located((By.ID, "idcta-link"))
            )
        finally:
            pass
        self.assertScreenshot('#idcta-link', 'bbc-masthead')