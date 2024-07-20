# Selenium Automation Testing Project

This project contains automated tests for a web application using Selenium WebDriver and pytest. The tests are designed to verify various functionalities as outlined in the given test cases.

## Project Structure

- `conftest.py`: Contains the setup and teardown code for the Selenium WebDriver instance.
- `Test_cases.py`: Contains the actual test cases that perform actions and assertions on the web application.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Google Chrome browser

### Installation

1. Clone the repository or download the project files.

2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes the following:
    ```
    pytest
    selenium
    webdriver-manager
    ```

### Setup

Ensure you have the local HTML file `QE-index.html` located at `C:/Users/Administrator/Downloads/AutomationChallenge_2022/QE-index.html`.

## Running the Tests

To run the tests, execute the following command in the project directory:

```bash
pytest
Test Case Details
Test Cases
Test 1
Purpose: Assert the presence of email, password inputs, and login button.
Steps:
Locate and assert the presence of email input, password input, and login button.
Enter email and password values.
Test 2
Purpose: Verify the list items in the test-2-div.
Steps:
Assert that there are three values in the list group.
Assert that the second list item's value is "List Item 2".
Assert that the badge value of the second list item is 6.
Test 3
Purpose: Verify the default and selected options in the dropdown menu.
Steps:
Assert that "Option 1" is the default selected value.
Select "Option 3" from the dropdown.
Test 4
Purpose: Verify the state of buttons in test-4-div.
Steps:
Assert that the first button is enabled.
Assert that the second button is disabled.
Test 5
Purpose: Verify the display of a success message upon clicking a button.
Steps:
Wait for a button to be displayed and click it.
Assert that a success message is displayed.
Assert that the button is now disabled.
Test 6
Purpose: Verify the value of a specific cell in a table.
Steps:
Write a method to find the value of any cell.
Use the method to find the value of the cell at coordinates (2, 2).
Assert that the value of the cell is "Ventosanzap".
