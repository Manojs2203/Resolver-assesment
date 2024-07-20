import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_1(browser):
    wait = WebDriverWait(browser, 15)
    
    
    # Assert that both the email address and password inputs are present as well as the login button
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
    
    assert email_input is not None
    assert password_input is not None
    assert login_button is not None
    time.sleep(10)
    email_input.send_keys("Resolvertest@example.com")
    password_input.send_keys("Resolver")
    # login_button.click()  # Uncomment if you want to actually perform the login

def test_2(browser):
    wait = WebDriverWait(browser, 15)  # Increased timeout

    try:
        # Locate the list items in the test 2 div
        list_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, '//div[@id="test-2-div"]//ul[@class="list-group"]//following::li')
            )
        )
        
        print(f"Found {len(list_items)} list items")
        assert len(list_items) == 3

        # Assert that the second list item's value is set to "List Item 2"
        second_item_text = list_items[1].text
        print(f"Second item text: {second_item_text}")
        assert "List Item 2" in second_item_text

        # Use following-sibling to locate the badge value of the second list item
        badge_value = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@id="test-2-div"]//ul[@class="list-group"]/li[2]//span[@class="badge badge-pill badge-primary"]')
            )
        ).text
        
        print(f"Badge value: {badge_value}")
        assert badge_value == "6"
    
    except Exception as e:
        print(f"Error occurred: {e}")
        raise



def test_3(browser):
    wait = WebDriverWait(browser, 10)
    
    # In the test 3 div, assert that "Option 1" is the default selected value
    select_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="dropdownMenuButton"]')))
    select_element.text
    
    # # Wait for all options to be present
    # options = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//select/option')))
    # default_option = select_element.find_element(By.XPATH, './option[@selected]')
    
    assert select_element.text == "Option 1"
    
    # Select "Option 3" from the select list
    select_element.click()
    option_3 = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="test-3-div"]/div/div/a[3]')))
    option_3.click()


def test_4(browser):
   
    
    # In the test 4 div, assert that the first button is enabled and that the second button is disabled
    first_button = browser.find_element(By.XPATH, '//button[1]')
    second_button = browser.find_element(By.XPATH, '//button[2]')
    
    assert first_button.is_enabled()
    assert not second_button.is_enabled()
@pytest.mark.xfail
def test_5(browser):
    wait = WebDriverWait(browser, 10)
    
    
    # In the test 5 div, wait for a button to be displayed (note: the delay is random) and then click it
    button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="test5-button"]')))
    button.click()
    
    # Assert that a success message is displayed
    success_message = browser.find_element(By.XPATH, '//*[@id="test5-alert"]')
    assert success_message.is_displayed()
    
    # Assert that the button is now disabled
    assert not button.is_enabled

def test_6(browser):
    
    
    def get_cell_value(row, col):
        cell = browser.find_element(By.XPATH, f'//table//tr[{row + 1}]//td[{col + 1}]')
        return cell.text
    
    # Use the method to find the value of the cell at coordinates 2, 2 (starting at 0 in the top left corner)
    cell_value = get_cell_value(2, 2)
    
    # Assert that the value of the cell is "Ventosanzap"
    assert cell_value == "Ventosanzap"
