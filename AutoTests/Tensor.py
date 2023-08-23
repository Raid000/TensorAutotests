import time
import chromedriver_autoinstaller
from selenium import webdriver
from PageObjects.YandexImages import YandexImageCategories, YandexImages, YandexImageViewer
from PageObjects.YandexResults import YandexResults
from PageObjects.YandexHome import YandexHome


chromedriver_autoinstaller.install() # Текущий selenium для python содержит chromedriver, который не поддерживает
# Chrome 116, поэтому придётся ставить свежий chromedriver отдельно этим методом

driver = webdriver.Chrome()

def test_FirstTask(): # Задание первое - "Поиск в яндексе"
    ya_home = YandexHome(driver, avoidCaptchaWithCookies=True)
    assert ya_home.get_search_field().is_displayed(), "Поле поиска НЕ отображается"
    ya_home.search_typing("Тензор")
    assert ya_home.get_suggest_table().is_displayed(), "Таблица с подсказками НЕ отображается"
    ya_home.search_enter()

    ya_results = YandexResults(driver)
    ya_results.recommendation_banner_skip()
    assert ya_results.get_result_table().is_displayed(), "Страница с результатами НЕ открыта"
    assert ya_results.get_list_of_results()[0].get_attribute("href") == "https://tensor.ru/", "Первая ссылка не ведёт на tensor.ru"

# def test_SecondTask(): # Задание второе - "Картинки на яндексе"
#     ya_home = YandexHome(driver, avoidCaptchaWithCookies=True)
#     ya_home.search_field_click()
#     assert ya_home.get_services_menu().is_displayed(), "Кнопка меню НЕ присутствует на странице"
#     ya_home.open_image_service()
#
#     driver.switch_to.window(driver.window_handles[-1]) # Так как открылась новая вкладка после перехода на "Картинки", то переводим driver на открывшуюся вкладку
#     ya_image_categories = YandexImageCategories(driver)
#     assert driver.current_url == "https://ya.ru/images/", "Текущий URL не https://ya.ru/images/"
#     first_category_name = ya_image_categories.get_list_of_categories()[0].get_attribute("data-grid-text")
#     ya_image_categories.choose_category_by_id(0)
#
#     ya_images = YandexImages(driver)
#     assert ya_images.get_search_field().get_attribute("value") == first_category_name, "Название выбранной категории НЕ отображается в поле поиска"
#     preview_image_src = ya_images.get_list_of_images()[0].get_attribute("data-bem")
#     ya_images.choose_image_by_id(0)
#
#     ya_image_viewer = YandexImageViewer(driver)
#     current_image_src = ya_image_viewer.get_current_image().get_attribute('src').split('//')[-1] # берём адрес без указания протокола для большей гибкости
#     assert current_image_src in preview_image_src, "Картинка не открылась или открылась не та картинка"
#     first_opened_image = ya_image_viewer.get_current_image().get_attribute('src')
#     ya_image_viewer.next_image()
#     assert first_opened_image != ya_image_viewer.get_current_image().get_attribute('src'), "Картинка не сменилась"
#     ya_image_viewer.previous_image()
#     assert first_opened_image == ya_image_viewer.get_current_image().get_attribute('src'), "Текущая картинка не соответсвует изначально открытой"


















