import os
from pymarksman.config import Config
from pymarksman.browser import Browser


def main():
    '''log in navigate and reboot'''
    config = Config(create_if_absent=True, debug=bool(os.getenv('DEBUG')))
    if config.debug:
        print('DEBUG mode')
    browser = Browser(config)
    browser.login()


if __name__ == "__main__":
    main()
