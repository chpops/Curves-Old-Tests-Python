import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.ask.com/")

    def test_one_results(self):
        print("☯ Small Selenium World by Chpops ☮\n")
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.ID, "sbut"))) # Синяя кнопка поиска
        assert "Ask.com" in driver.title
        input_field = driver.find_element_by_id("search-box")
        input_field.send_keys("python test")
        input_field.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "PartialSearchResults-item"))) # Результаты поиска
        resultCountOnPage = len(driver.find_elements_by_class_name("PartialSearchResults-item-title"))
        if resultCountOnPage == 9:
            print("[✔] Test One Results Completed! [✔]")
        else:
            print("[✘] Test One Results Failed [✘] :(")

    def test_two_related_search(self):
        driver = self.driver
        wait = WebDriverWait(driver,10)
        wait.until(EC.visibility_of_element_located((By.ID, "sbut")))
        input_field = driver.find_element_by_id("search-box")
        input_field.send_keys("ask tests")
        input_field.send_keys(Keys.ENTER)
        wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "PartialSearchResults-item")))  # Результаты поиска
        relatedSearchList = len(driver.find_elements_by_class_name("PartialRelatedSearch-item"))
        if relatedSearchList == 18:
            print("[✔] Test Two Related Search Completed! [✔]")
        else:
            print("[✘] Test Two Related Search Failed [✘] :(")

    def tearDown(self):
        self.driver.quit()