from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YandexResults:
    def __init__(self, driver):
        self.driver = driver
        self.results_table_xpath = '//ul[@id="search-result"]'
        self.list_of_results_xpath = '//ul[@id="search-result"]/li//a[@href and @role]'
        self.recommendation_banner_xpath = "/html/body/main/div[3]/div/button"

    def get_result_table(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.results_table_xpath))
        )

    def get_list_of_results(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.list_of_results_xpath))
        )

    def recommendation_banner_skip(self):
        try:
            recommendation_banner = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, self.recommendation_banner_xpath))
            )
            recommendation_banner.click()
        except TimeoutException:
            # Баннер не найден, ничего не делаем
            pass
