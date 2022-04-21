from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from typing import List


class HomepageYandex(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators and links
        self.__search_bar_id: str = 'text'
        self.__search_bar_text: str = 'Тензор'
        self.__suggest_list_class: str = 'mini-suggest__popup-content'
        self.__main_content_table_class: str = '#search-result>li>div>div>div>a'
        self.__search_bar_enter_key: Keys = Keys.ENTER
        self.LINK = 'https://tensor.ru/'

    def get_search_bar(self) -> WebElement:
        return self.is_present('id', self.__search_bar_id, 'Search bar id')

    def get_suggest_list(self) -> WebElement:
        return self.is_visible('class_name', self.__suggest_list_class, 'Suggest list class')

    def get_main_content_table(self) -> List[WebElement]:
        return self.are_visible('css', self.__main_content_table_class, 'Main content table class')

    def get_links_from_list_of_elements(self) -> List[str]:
        href_links = self.get_main_content_table()
        return [link.get_attribute('href') for link in href_links]

    def send_keys_to_element(self, element: WebElement, report) -> None:
        element.send_keys(self.__search_bar_text)
        report.write(f'Keys are sent to the element' + '\n')

    def send_enter_to_element(self, element: WebElement, report) -> None:
        element.send_keys(self.__search_bar_enter_key)
        report.write(f'Enter is sent to the element' + '\n')
