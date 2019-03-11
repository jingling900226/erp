__author__ = 'wangling'

import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase as te
from testBLL import apkBase
from testCase.open import testOpen
from testCase.login import testLogin


class runCase(te):

    def setUp(self):
        super(runCase, self).setUp()
        self.driver.implicitly_wait(20)

    def get_apk_pkg(self):
        return apkBase.apkInfo(PATH("../img/erp.apk")).get_apk_pkg()

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        pass

    @staticmethod
    def tearDownClass():
        pass

    def test_home(self):
        testLogin.loginRun(self)
        self.driver.implicitly_wait(10)
        testOpen.openRun(self)
        self.driver.implicitly_wait(25)
        testLogin.close(self)


