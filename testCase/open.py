__author__ = 'wangling'

import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase as te
from testBLL import apkBase


class testOpen(te):

    # 检查是否有这些open.yaml中的房间
    def check_Room(self):
        self.bc = b_app_case.GetAppCase(test_module="开台", GetAppCaseInfo=m_app_case.GetAppCaseInfo,
                                        GetAppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[],
                                        driver=self.driver, package=self.get_apk_pkg(),
                                        devices=self.l_devices["deviceName"])
        self.bc.execCase(PATH("yaml/shouyin/open.yaml"),test_name="检查收银房间是否存在",isLast="0")

    def get_apk_pkg(self):
        return apkBase.apkInfo(PATH("../img/erp.apk")).get_apk_pkg()

    # 开台-现结-关台-置空闲
    def openCheckNow(self):
        self.bc.execCase(PATH("yaml/shouyin/open_close_xianjie.yaml"), test_name="包房1开台现结关台", isLast="0")
    # 开台-落单后结-置空闲
    def openCheck(self):
        self.bc.execCase(PATH("yaml/shouyin/open_close_luohou.yaml"),test_name="包房12开台落单后结关台",isLast="0")

    # 开台-下单-现结-关台-置空闲
    def openOrderNow(self):
        self.bc.execCase(PATH("yaml/shouyin/open_order_xianjie.yaml"),test_name="包房12开台下单现结",isLast="0")

    def openRun(self):
        testOpen.check_Room(self)
        testOpen.openOrderNow(self)
        testOpen.openCheck(self)
