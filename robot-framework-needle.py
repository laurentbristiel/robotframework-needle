from needle.cases import NeedleTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class testLogo(NeedleTestCase):
    def test_logo(self):
        self.driver.get('http://www.bbc.co.uk/news/')
        try:
             WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "blq-mast"))
            )
        finally:
            pass
        self.assertScreenshot('#blq-mast', 'bbc-masthead')