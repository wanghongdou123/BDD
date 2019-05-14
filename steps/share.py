@when('I click {org}')
def step_impl(self, org):
    self.driver.find_element_by_xpath('//span[contains(text(),org)]').click()
    time.sleep(3)