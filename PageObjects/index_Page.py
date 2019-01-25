__author__ = 'mucang'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.index_locator import IndexLocator
from common.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

'''
PO模型中的前程贷首页的页面对象类
'''
class IndexPage(BasePage):
    '''
    首页页面类封装了登录页面中的操作
    '''

    '''判断首页中我的账户元素是否存在'''
    def member_is_exist(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_member_is_exist"
        return self.wait_eleVisible(IndexLocator.my_user,model=model)

    '''点击标的抢投标按钮'''
    def click_bid_button(self):
        #方法标识，用来在底层操作出现异常时，定位日志问题
        model = "首页_click_bid_button"
        self.click_element(IndexLocator.bid_button,model=model)




