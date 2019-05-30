import pytest
from selenium import webdriver
from time import sleep


class TestWebPage:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        cls.driver.implicitly_wait(40)
        cls.driver.get("https://cdn.clearcode.pl/2019/05/index2.html")

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def test_first_name_initial_value(self):
        self.driver.get("https://cdn.clearcode.pl/2019/05/index2.html")
        if self.driver.find_element_by_xpath('//*[@id="firstname-input"]').get_attribute("value") == 'Mickey':
            assert True
        else:
            assert False

    def test_last_name_initial_value(self):
        self.driver.get("https://cdn.clearcode.pl/2019/05/index2.html")
        if self.driver.find_element_by_xpath('//*[@id="lastname-input"]').get_attribute("value") == 'Mouse':
            assert True
        else:
            assert False

    def test_submit_button_text(self):
        self.driver.get("https://cdn.clearcode.pl/2019/05/index2.html")
        if self.driver.find_element_by_xpath('// *[ @ id = "submit-button"]').get_attribute("value") == 'Submit':
            assert True
        else:
            assert False

    @pytest.mark.parametrize('first_name, last_name',
                             [
                                 ('Peter', 'Parker'),
                                 ('', 'Parker'),  # empty first name
                                 ('Peter', ''),  # empty last name
                                 ('', ''),  # empty strings
                             ]
                             )
    def test_input_data(self, first_name, last_name):
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="firstname-input"]').clear()
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="lastname-input"]').clear()

        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="firstname-input"]').send_keys(first_name)

        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="lastname-input"]').send_keys(last_name)

        sleep(0.5)
        self.driver.find_element_by_xpath('// *[ @ id = "submit-button"]').click()

        if self.driver.find_element_by_xpath('//*[@id="lastname-input"]').get_attribute("value") == 'Mouse' and \
            self.driver.find_element_by_xpath('//*[@id="firstname-input"]').get_attribute("value") == 'Mickey':
            assert True
        else:
            assert False


if __name__ == '__main__':
    pytest.main()
