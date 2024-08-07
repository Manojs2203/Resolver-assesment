import pytest
from selenium import webdriver

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def browser():
    
    driver = webdriver.Chrome()
     # Navigate to the main HTML file
    driver.get('file:///C:/Users/Administrator/Downloads/AutomationChallenge_2022/QE-index.html')
    driver.implicitly_wait(10)
    yield driver
    
    driver.quit()
