import time
import unittest
import eea.seleniumtests.util as util

from edw.seleniumtesting.common import BrowserTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

FINDER = util.ElementFinder()


def suite(browser, base_url, extra_args):
    """ Call on review folder url providing user mapping and user accounts.\n
    `` seleniumtesting http://localhost/Plone/ \\
        -ea roles manager username \\
        -ea users username "$(< pwd_file)"
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
        """ Add page
        """
        # Accept cookie
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.ID, 'tlspu_cookiepolicy_button'))
        )
        FINDER.css('#tlspu_cookiepolicy_button').click()

        # Add Page page
        self.browser.get(self.url + '/createObject?type_name=Document')

        # Page title
        f_title = FINDER.css('#title')
        f_title.send_keys('Test document.')

        # Categorization tab
        FINDER.css('#fieldsetlegend-categorization').click()

        # Tags
        f_keywords = FINDER.css('#token-input-subject_keywords')
        f_keywords.send_keys('bathing')
        f_keywords.send_keys(Keys.RETURN)

        # Location
        FINDER.css('#location-edit').click()
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.eea-geotags-popup'))
        )
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.geo-results-search input[name="search"]'))
        )
        f_search = FINDER.css('.geo-results-search input[name="search"]')
        f_search.send_keys('Bucharest')
        FINDER.css('.geo-results-search input[name="submit"]').click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.geo-point-view'))
        )
        FINDER.css('.geo-point-view').click()

        # Wait for animations
        time.sleep(3)

        # Save location
        FINDER.xpath('//button[contains(.,"Save geotags")]').click()

        # Wait for overlay to go away
        WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.ui-widget-overlay'))
        )

        # Set Theme
        FINDER.css('#themes_options option[value="default"]').click()
        FINDER.css('input[value=">>"]').click()

        # Save Page
        FINDER.css('input[name="form.button.save"]').click()
