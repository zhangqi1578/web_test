__author__ = 'mucang'

import time
import unittest
from selenium import webdriver
from PageObjects.login_Page import LoginPage
from PageObjects.index_Page import IndexPage
from PageUrl import page_url
from Test_datas import login_case_data
import ddt


'''
登录测试用例类，第一个版本，每条用例重新启动chrome，较慢，但是用例间独立原则
'''
@ddt.ddt
class TestLogin(unittest.TestCase):
    '''包含了login模块所有测试用例'''


    '''每条用例执行前的初始化准备工作（通用前置条件）'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(page_url.login_page_url)

        self.lp = LoginPage(self.driver)
        self.ip = IndexPage(self.driver)

    '''每条用例执行后的收尾工作（关闭浏览器会话）'''
    def tearDown(self):
        self.driver.quit()


    def test_login_success(self):
        '''正常登录'''
        '''步骤:18684720553/python'''
        self.lp.login(login_case_data.success_data["username"],login_case_data.success_data["pwd"])
        '''断言'''
        try:
            self.assertTrue(self.ip.member_is_exist())
            test_result = "PASS"
        except Exception as e:
            test_result = "FAIL"
            raise e
        finally:
            '''excel中写回测试结果'''
            pass

    @ddt.data(*login_case_data.error_data_form)
    def test_login_error_form(self,data):
        '''异常登录【from错误提示】，测试用例步骤及断言实现一样的可以通过ddt来执行'''
        '''步骤:n'''
        self.lp.login(data["username"],data["pwd"])
        '''断言'''
        try:
            self.assertEqual(data["check"],self.lp.error_from_text())
            test_result = "PASS"
        except Exception as e:
            test_result = "FAIL"
            raise e
        finally:
            '''excel中写回测试结果'''
            pass

    @ddt.data(*login_case_data.error_data_pageCenter)
    def test_login_error_pageCenter(self,data):
        '''异常登录【错误提示pageCenter-totast】，测试用例步骤及断言实现一样的可以通过ddt来执行'''
        '''步骤:'''
        self.lp.login(data["username"],data["pwd"])
        '''断言'''
        try:
            self.assertEqual(data["check"],self.lp.error_pageCenter_text())
            test_result = "PASS"
        except Exception as e:
            test_result = "FAIL"
            raise e
        finally:
            '''excel中写回测试结果'''
            pass

if __name__ == '__main__':
    unittest.main()



