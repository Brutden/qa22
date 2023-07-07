from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
from selenium.webdriver.common.by import By
import allure
import time
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.Alert import Alert
from selenium.webdriver import ActionChains


@pytest.mark.usefixtures('setup')
class TestLUMA:
    driver = None

    @allure.feature('Тест магазина одежды')
    @allure.story('Возврат на главную страницу')
    @allure.description('')
    def test_store1(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Нажать кнопку '):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/span').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать на логотип LUMA'):
            self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Whats New')
    @allure.description('')
    def test_store2(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Whats New'):
            self.browser.find_element(By.XPATH, '//*[@id="ui-id-3"]/span').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Women')
    @allure.description('')
    def test_store3(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Women'):
            self.browser.ind_element(By.XPATH, '//*[@id="ui-id-4"]/span[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Men')
    @allure.description('')
    def test_store4(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Men'):
            self.browser.ind_element(By.XPATH, '//*[@id="ui-id-5"]/span[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Gear')
    @allure.description('')
    def test_store5(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Gear'):
            self.browser.ind_element(By.XPATH, '//*[@id="ui-id-6"]/span[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Training')
    @allure.description('')
    def test_store6(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Training'):
            self.browser.ind_element(By.XPATH, '//*[@id="ui-id-7"]/span[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Sale')
    @allure.description('')
    def test_store7(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Sale'):
            self.browser.ind_element(By.XPATH, '//*[@id="ui-id-8"]/span').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Write for use')
    @allure.description('')
    def test_store8(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Write for use'):
            self.browser.ind_element(By.XPATH, '/html/body/div[1]/footer/div/div[2]/div/ul/li/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Search Terms')
    @allure.description('')
    def test_store9(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Search Terms'):
            self.browser.ind_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Privacy and Cookie Policy')
    @allure.description('')
    def test_store10(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Privacy and Cookie Policy'):
            self.browser.ind_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[1]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Advanced Search')
    @allure.description('')
    def test_store11(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Advanced Search'):
            self.browser.ind_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Orders and Returns')
    @allure.description('')
    def test_store12(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Orders and Returns'):
            self.browser.ind_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[4]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Contact Us')
    @allure.description('')
    def test_store13(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Contact Us'):
            self.browser.ind_element(By.XPATH, '/html/body/div[1]/footer/div/ul/li[5]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Fusion Backpack')
    @allure.description('')
    def test_store14(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Fusion Backpack'):
            self.browser.ind_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[3]/div/div/ol/li[5]/div/a/span/span/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Тест магазина одежды')
    @allure.story('тест кнопки Push It Messenger Bag')
    @allure.description('')
    def test_store15(self):
        with allure.step('открыть ссылку'):
            self.browser.get('https://magento.softwaretestingboard.com/')
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('нажать кнопку Push It Messenger Bag'):
            self.browser.ind_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div[2]/div[3]/div/div/ol/li[6]/div/div/strong/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)