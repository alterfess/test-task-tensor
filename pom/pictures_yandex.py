from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class PicturesYandex(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators and links
        self.__picture_xpath = '//a[@href="' + 'https://yandex.ru/images/?utm_source=main_stripe_big' + '"]'
        self.__first_popular_category_css = 'a.Link.PopularRequestList-Preview'
        self.__first_picture_css = 'a.serp-item__link'
        self.__forward_key_css = 'div.CircleButton_type_next'
        self.__backward_key_css = 'div.CircleButton_type_prev'
        self.__opened_picture_css = 'img.MMImage-Origin'
        self.LINK = 'https://yandex.ru/images/'

    def get_pictures_link(self) -> WebElement:
        return self.is_present('xpath', self.__picture_xpath, 'Picture link')

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_current_title(self) -> str:
        return self.driver.title

    def get_first_popular_picture(self) -> WebElement:
        return self.is_present('css', self.__first_popular_category_css)

    def get_first_picture(self) -> WebElement:
        return self.is_present('css', self.__first_picture_css)

    def get_forward_key(self) -> WebElement:
        return self.is_present('css', self.__forward_key_css)

    def get_backward_key(self) -> WebElement:
        return self.is_present('css', self.__backward_key_css)

    def get_opened_picture(self) -> WebElement:
        return self.is_present('css', self.__opened_picture_css)

    def handle_new_window(self) -> None:
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
