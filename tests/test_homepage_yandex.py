import pytest
import selenium.common
import time
from pom.homepage_yandex import HomepageYandex
from report_func.axillary_report_function import update_report_file, failed_test


@pytest.mark.usefixtures('setup')
class TestHomepageYandex:

    def test_yandex_home_page(self):

        # Create report file and instance of the HomepageYandex class
        report_file = update_report_file('reports/test_home_page_yandex_report.txt')
        homepage_yandex = HomepageYandex(self.driver)

        # Validation of the search bar
        try:
            report_file.write('Validating Search bar...' + '\n')
            search_bar = homepage_yandex.get_search_bar()
            report_file.write('Passed: Search bar is presented on the page' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'Search bar is not presented on the page')

        # Validation of the suggested list
        try:
            report_file.write('Validating Suggested list...' + '\n')
            homepage_yandex.send_keys_to_element(search_bar, report_file)
            time.sleep(1)
            suggest_list = homepage_yandex.get_suggest_list()
            report_file.write('Passed: Suggested list is visible on the page' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'Suggested list is not visible on the page')

        # Validation of the content table
        try:
            report_file.write('Validating content table...' + '\n')
            homepage_yandex.send_enter_to_element(search_bar, report_file)
            actual_links = homepage_yandex.get_links_from_list_of_elements()
            report_file.write('Passed: Content table is visible on the page' + '\n')
        except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.InvalidSelectorException):
            failed_test(report_file, 'Content table is not visible on the page')

        # Validation of first 5 result consisting of the tensor.ru
        expected_link = homepage_yandex.LINK
        report_file.write(f'Validating {expected_link}...' + '\n')
        assert expected_link in actual_links[:5], failed_test(report_file, f'{expected_link} is not in the first 5 results')
        report_file.write(f'Passed: {expected_link} is in the first 5 results' + '\n')

        # Close report file
        report_file.write('PASSED' + '\n')
        report_file.write(50 * '_' + '\n')
        report_file.close()
