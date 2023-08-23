from _pytest.fixtures import fixture
from allure_commons._allure import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class YandexImageCategories:
    def __init__(self, driver):
        self.driver = driver
        self.list_of_categories_xpath = '//*[@class="PopularRequestList"]/*'

    def get_list_of_categories(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(
            (By.XPATH, self.list_of_categories_xpath))
        )

    def choose_category_by_id(self, Id):
        list_of_categories = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(
            (By.XPATH, self.list_of_categories_xpath))
        )
        list_of_categories[Id].click()


class YandexImages:
    def __init__(self, driver):
        self.driver = driver
        self.list_of_images_xpath = '/html/body//div[@role="list"]/div[not(contains(@class, "incut"))]'
        self.search_field_xpath = '//input[@class="input__control mini-suggest__input"]'

    def get_search_field(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.search_field_xpath))
        )

    @step("Выбор изображения по его порядку - Id")
    def choose_image_by_id(self, Id):
        list_of_images = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(
            (By.XPATH, self.list_of_images_xpath))
        )
        list_of_images[Id].click()

    def get_list_of_images(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(
            (By.XPATH, self.list_of_images_xpath))
        )


class YandexImageViewer:
    def __init__(self, driver):
        self.driver = driver
        self.image_viewer_xpath = '/html/body//div[@class="MMImageContainer"]/img'
        self.next_image_button_xpath = '/html/body//div[contains(@class, "CircleButton_type_next")]'
        self.previous_image_button_xpath = '/html/body//div[contains(@class, "CircleButton_type_prev")]'

    def get_current_image(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.image_viewer_xpath))
        )

    @step("Переход к следующему изображению")
    def next_image(self):
        next_image_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.next_image_button_xpath))
        )
        next_image_button.click()

    @step("Переход к предыдущему изображению")
    def previous_image(self):
        previous_image_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.previous_image_button_xpath))
        )
        previous_image_button.click()




