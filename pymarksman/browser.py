from time import sleep
from pymarksman.utils import die, get_browser_location
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
from enum import Enum


class Status(Enum):
    AUTHORIZED = 1
    NOTAUTHORIZED = 2
    FAILED = 3


class Browser():
    '''launch, manipulate browser'''

    def __init__(self, config):
        self.config = config
        self.authstatus = Status.NOTAUTHORIZED

    def login(self):
        user, pw = self.config.conf.get('credentials', 'username'), \
            self.config.conf.get('credentials', 'password')

        chrome_options = Options()
        if not self.config.debug:
            chrome_options.add_argument("--headless")
            # chrome_options.add_argument('--no-sandbox')
            # chrome_options.add_argument("--start-maximized")
        chrome_options.binary_location = get_browser_location()
        driver = webdriver.Chrome(executable_path=which('chromedriver'),
                                  options=chrome_options)

        if not self.config.debug:
            driver.set_window_size(1024, 768)

        driver.get(self.config.conf.get('urls', 'login'))
        die()

        # TODO: check for label with recaptcha-anchor-label (google captcha)

        username_field = driver.find_element_by_id("inputEmail")
        username_field.clear()
        username_field.send_keys(user)

        pw_field = driver.find_element_by_id("inputPassword")
        pw_field.clear()
        pw_field.send_keys(pw)
        pw_field.send_keys(Keys.RETURN)
        sleep(2)  # TODO: convert sleeps to webdriverwait

        # assert domain in driver.page_source

        # server = driver.find_element_by_partial_link_text(domain)
        # server.click()
        # sleep(2)

        # # TODO: optionally check if server status is Active
        # assert 'Reboot' in driver.page_source

        # if self.config.debug != '2':
        #     # DEBUG: don't click reboot if DEBUG==2
        #     server = driver.find_element_by_partial_link_text('Reboot')
        #     server.click()
        #     sleep(2)
        #     try:
        #         assert 'Action Completed Successfully' in driver.page_source
        #         print('%s rebooted' % domain)
        #     except:
        #         print('%s reboot FAILED' % domain)
        # else:
        #     print('DEBUG mode - no reboot')

        if self.config.debug:
            sleep(10)
        driver.quit()
