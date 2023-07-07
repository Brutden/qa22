import pytest
import time
import allure
from selenium import webdriver
import selenium.webdriver.chrome.options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.Alert import alert


@pytest.fixture(scope='class')
def setup(request):
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.set_window_size(1920, 1080)
    request.cls.driver = driver
    yield driver
    driver.close()