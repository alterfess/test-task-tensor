import pytest
import selenium.common
import time
from pom.pictures_yandex import PicturesYandex
from report_func.axillary_report_function import update_report_file, failed_test


@pytest.mark.usefixtures('setup')
class TestYandexPictures:

    def test_yandex_pictures(self):

        # Create report file and instance of the PicturesYandex class
        report_file = update_report_file('reports/test_yandex_pictures_report.txt')
        yandex_pictures = PicturesYandex(self.driver)

        # Validation of the pictures link
        try:
            report_file.write('Validating Pictures link...' + '\n')
            pictures_link = yandex_pictures.get_pictures_link()
            report_file.write('Passed: Pictures link is presented on the page' + '\n')
            pictures_link.click()
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'Pictures link is not presented on the page')

        # Validation of the current URL after go to pictures link
        report_file.write('Validating current URL...' + '\n')
        yandex_pictures.handle_new_window()
        url = yandex_pictures.get_current_url()
        expected_link = yandex_pictures.LINK

        assert expected_link in url, failed_test(report_file, f'The current URL is not {expected_link}')
        report_file.write(f'Passed: The current URL is {expected_link}' + '\n')

        # Validation of the First popular category and text of the search bar
        try:
            report_file.write('Validating First popular category...' + '\n')
            first_popular_category = yandex_pictures.get_first_popular_picture()
            first_popular_category_text = first_popular_category.text
            first_popular_category.click()
            time.sleep(1)
            report_file.write('Passed: First popular category is opened' + '\n')

            assert first_popular_category_text in yandex_pictures.get_current_title(), failed_test(report_file, 'In the search bar is not correct text')
            report_file.write('Passed: In the search bar is correct text' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'First popular category is not presented on the page')

        # Validation of the First picture
        try:
            report_file.write('Validating First picture...' + '\n')
            first_picture = yandex_pictures.get_first_picture()
            first_picture.click()
            first_opened_picture = yandex_pictures.get_opened_picture()
            report_file.write('Passed: First picture is opened' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'First picture is not presented on the page')

        # Validation of the Forward button
        try:

            report_file.write('Validating Forward button...' + '\n')
            first_opened_picture_link = first_opened_picture.get_attribute('src')
            forward_button = yandex_pictures.get_forward_key()
            forward_button.click()
            second_opened_picture = yandex_pictures.get_opened_picture()
            second_opened_picture_link = second_opened_picture.get_attribute('src')

            assert first_opened_picture_link != second_opened_picture_link,failed_test(report_file, 'The forward button does not work properly')
            report_file.write('Passed: The forward button works properly, another picture was opened' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'Second picture is not presented on the page')

        # Validation of the Backward button
        try:
            report_file.write('Validating Backward button...' + '\n')
            backward_button = yandex_pictures.get_backward_key()
            backward_button.click()
            first_picture_opened_by_backward = yandex_pictures.get_opened_picture()
            first_picture_opened_by_backward_link = first_picture_opened_by_backward.get_attribute('src')
            assert first_picture_opened_by_backward_link == first_opened_picture_link, failed_test(report_file, 'The Backward button does not properly, the pictures are not matched')
            report_file.write('Passed: The Backward button works properly, the pictures are matched' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'Second picture is not presented on the page')

        # Close report file
        report_file.write('PASSED' + '\n')
        report_file.write(50 * '_' + '\n')
        report_file.close()