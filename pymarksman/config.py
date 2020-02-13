import configparser
import os.path


class Config():
    '''store naughtystep config'''

    def __init__(self, create_if_absent=True, debug=False):
        '''load / create conf'''
        self.debug = debug
        conffile = os.path.join(os.path.expanduser("~"), '.config',
                                '.pymarksman')
        self.conf = self.loadconfig(conffile, create_if_absent)

    def loadconfig(self, conffile, create_if_absent):
        '''load conf or create default if it doesn't exist'''
        cfg = configparser.ConfigParser(allow_no_value=True)
        if len(cfg.read(conffile)) == 0:
            # conf empty
            if create_if_absent:
                # empty or non-existent conf file, create default
                cfg = self.default_config(cfg)
                with open(conffile, 'w') as configfile:
                    cfg.write(configfile)
            else:
                raise configparser.Error
        return cfg

    @staticmethod
    def default_config(cfg):
        '''create default config options'''
        cfg['base'] = {}
        cfg['credentials'] = {'username': '',
                              'password': ''}
        cfg['urls'] = {'login': 'https://signin.ebay.co.uk/ws/eBayISAPI.dll?SignIn&UsingSSL=1&pUserId=&co_partnerId=2&siteid=3'}
        return cfg
