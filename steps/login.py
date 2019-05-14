from selenium import webdriver
from behave import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@given('Access bss website')
def step_impl(self):
    self.driver = webdriver.Chrome()
    url = 'https://newbss.aishuaiche.com/'
    self.driver.get(url)
    time.sleep(3)

@when('Input {username} enter {passwords}')
def step_impl(self,username,passwords):
    self.driver.find_element_by_id('username').send_keys(username)
    time.sleep(2)
    self.driver.find_element_by_id('passwords').send_keys(passwords)

@when('Click button {button}')
def step_impl(self,button):
    self.driver.find_element_by_xpath('//button[contains(text(),button)]').click()
    time.sleep(2)

@given('login success')
def step_impl(self):
    pass

@when('I click the {operating}')
def step_impl(self,operating):
    self.driver.find_element_by_xpath('//span[contains(text(),operating)]').click()

@then('I can see {result}')
def step_impl(self, result):
    assert '//span[contains(text(),result)]' in self.driver.page_source,"未登录找到result"




# @when('click button {button}')
# def step_impl(self,button):
#     self.driver.find_element_by_xpath('//button[contains(text(),button)]').click()
#     time.sleep(15)
#
# @when('I click {org}')
# def step_impl(self, org):
#     self.driver.find_element_by_xpath('//span[contains(text(),org)]').click()
#     time.sleep(3)
#
#
# @Then('I can see {personnel}')
# def step_impl(self,personnel):
#     Personnel_management=self.driver.find_element_by_xpath('//a[contains(text(),personnel)]')
#     assert Personnel_management in self.driver.page_source,"人员管理未搜索成功"
#
# @when('I click {personnel}')
# def step_impl(self,personnel):
#     self.driver.find_element_by_xpath('//a[contains(text(),personnel)]').click()
#     time.sleep(5)



# @Then('I can see "新增人员"')
# def step_impl(self):
#     assert "新增人员" in self.driver.page_source,"新增人员未搜索成功"
#
# @when('Input right username')
# def step_impl(self):
#     self.driver.find_element_by_xpath('(//input[@type="text"])[2]').send_keys('13500000001')
#     time.sleep(5)
#
#
# @when('press enter key')
# def step_impl(self):
#     self.driver.find_element_by_xpath('(//input[@type="text"])[2]').send_keys(Keys.ENTER)
#     time.sleep(3)
#
# @then('I can see "测试金融销售01"')
# def step_impl(self):
#     assert "测试金融销售01" in self.driver.page_source,"未搜索成功"
#
#
# @when('I click logout')
# def step_impl(self):
#     logout1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/ul/li/div')
#     ActionChains(self.driver).move_to_element(logout1).perform()
#     self.driver.find_element_by_xpath('//*[@id="item_0$Menu"]/li[2]').click()
#     time.sleep(3)
#
# @then('I can see "手机号"')
# def step_impl(self):
#     time.sleep(3)
#     assert '手机号' in self.driver.page_source,"未退出成功"
#     time.sleep(3)

















