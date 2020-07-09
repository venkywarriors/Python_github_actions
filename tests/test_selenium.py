'''
Created on 05-Jul-2020

@author: venkateshwara D
'''
# pytest -ra test_selenium.py -v
import pytest
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.yield_fixture()
def setUp():
    
# chrome_options.headless = True # also works
    global driver
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    print('++++++++++ Set Up +++++++++++')
    yield 
    driver.quit()
    print('++++++++++ quit +++++++++++')
 
@pytest.mark.run(order=1)        
def test_searchForAutomation(setUp): 
    driver.get("http://google.com")
    driver.find_element_by_name("q").send_keys("Automation")
    time.sleep(1)
    driver.find_element_by_name("btnK").click() 
    print('++++++++++ test_searchForAutomation +++++++++++')
 
@pytest.mark.run(order=2)
def test_searchForPython(setUp): 
    driver.get("http://google.com")
    driver.find_element_by_name("q").send_keys("Python")
    time.sleep(1)
    driver.find_element_by_name("btnK").click()  
    print('++++++++++ test_searchForPython +++++++++++')
      
    
    
