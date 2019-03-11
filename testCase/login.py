__author__ = 'wangling'

import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testBLL import appCase as b_app_case
from testMode import appCase as m_app_case
from testRunner.runnerBase import TestInterfaceCase as te
from testBLL import apkBase


class testLogin(te):

        # 单点登陆这里特殊处理,不同的设备调用不同的case
    def home_login(self):
        self.bc = b_app_case.GetAppCase(test_module="登陆模块", GetAppCaseInfo=m_app_case.GetAppCaseInfo,
                                        GetAppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[],
                                        driver=self.driver, package=self.get_apk_pkg(),
                                        devices=self.l_devices["deviceName"])
        home_logon_yaml = ""
        if self.l_devices["deviceName"] == "192.168.199.1:5555":
            home_logon_yaml = PATH("yaml/shouyin/ktxj.yaml")
        if self.l_devices["deviceName"] == "192.168.1.100:5555":
            home_logon_yaml = PATH("yaml/login/login.yaml")
        if self.l_devices["deviceName"] == "MSM8926":
            home_logon_yaml = PATH("yaml/myinfo/home_login1.yaml")
        self.bc.execCase(home_logon_yaml, test_name="登陆", isLast="0")

    # 退出登录
    def close(self):
        self.bc = b_app_case.GetAppCase(test_module="退出模块", GetAppCaseInfo=m_app_case.GetAppCaseInfo,
                                        GetAppCase=m_app_case.GetAppCase, fps=[], cpu=[], men=[],
                                        driver=self.driver, package=self.get_apk_pkg(),
                                        devices=self.l_devices["deviceName"])
        close_yaml=PATH("yaml/login/close.yaml")
        self.bc.execCase(close_yaml, test_name="退出登录", isLast="0")

    def get_apk_pkg(self):
        return apkBase.apkInfo(PATH("../img/erp.apk")).get_apk_pkg()


    def loginRun(self):
        testLogin.home_login(self)
