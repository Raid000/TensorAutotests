import json

from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class YandexHome:
    def __init__(self, driver, avoidCaptchaWithCookies=False):
        self.driver = driver
        self.driver.get("https://ya.ru/")
        self.search_input_xpath = '//input[@id="text"]'
        self.services_menu_xpath = '/html/body/main/div[@class="body__content"]/form//div[@class="services-suggest__icons-more"]'
        self.images_service_xpath = '/html/body/main/div[4]/div/div[1]/div/div[3]/div[1]/span[9]/a[@aria-label="Картинки"]'
        self.suggest_table_xpath = '//ul[@class="mini-suggest__popup-content"]'

        if avoidCaptchaWithCookies:
            with open('ya_cookies.json', 'r') as f:
                cookies = json.load(f)
            for i in cookies:
                driver.add_cookie(i)
            driver.refresh()

    @step("Ввод данных в строку поиска")
    def search_typing(self, query):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.search_input_xpath))
        )
        search_input.send_keys(query)

    def search_field_click(self):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.search_input_xpath))
        )
        search_input.click()

    def get_search_field(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.search_input_xpath))
        )

    def get_suggest_table(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.suggest_table_xpath))
        )

    @step("Начать поиск результатов в Yandex")
    def search_enter(self):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.search_input_xpath))
        )
        search_input.send_keys(Keys.ENTER)

    def get_services_menu(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.services_menu_xpath))
        )

    @step('Открытие сервиса "Картинки"')
    def open_image_service(self):
        services_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.services_menu_xpath))
        )
        services_menu.click()
        images_service = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.images_service_xpath))
        )
        images_service.click()
