import unittest
import eea.test.util as util

from edw.seleniumtesting.common import BrowserTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

FINDER = util.ElementFinder()


def suite(browser, base_url, extra_args):
    """ Call on review folder url providing user mapping and user accounts.\n
    `` seleniumtesting http://localhost/Plone/ \\
        -ea roles manager username \\
        -ea users username password
    ``
    """
    FINDER.set_browser(browser)

    params = dict(
        browser=browser,
        base_url=base_url,
        extra_args=extra_args
        )

    test_suite = util.TestFactory(
        unittest.TestSuite(),
        **params
        )

    test_suite.add_tests(Sandbox)

    return test_suite()


class Sandbox(BrowserTestCase):

    def setUp(self):
        self.browser.get(self.url)

    @util.runas('manager')
    def test_add_page(self):
        """ Test sector expert can add question.
        """
        # Add questions
        FINDER.css('#document').click()
        f_title = FINDER.css('#title')
        f_title.send_keys('Test document.')

        FINDER.css('#fieldsetlegend-categorization').click()
        f_keywords = FINDER.css('#subject_keywords')
        f_keywords.send_keys('bathing')

        FINDER.css('#location-edit').click()
        f_search = FINDER.css('.geo-results-search input[name="search"]')
        f_search.send_keys('Bucharest')
        FINDER.css('.geo-results-search input[name="submit"]').click()
        FINDER.css('.geo-point-view').click()

        FINDER.xpath('//button[contains(.,"Save geotags")]')

        FINDER.css('#themes_options option[value="default"]').click()
        FINDER.css('input[value=">>"]').click()

        FINDER.css('input[name="form.button.save"]').click()
