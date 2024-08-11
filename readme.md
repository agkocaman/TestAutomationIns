# Test Automation Project

This is a simple test automation project. It uses Python and Selenium. The project tests the Insider website.

## Project Structure

- **pages/**: Contains page classes
  - `base_page.py`: base page actions
  - `career_page.py`: Careers page actions
  - `home_page.py`: home page actions
  - `open_positions_page.py`: open positions page actions
  - `quality_assurance_page.py`: quality assurance apage actions
- **tests/**: Contains test files
  - `career_test.py`: Career test file
  - `home_test.py`: Home page test file
  - `main.py`: Main test file
  - `open_positions_test.py`: Open Positions test file,
  - `quality_assurance_test.py`: QA page test file

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/agkocaman/TestAutomationIns.git
   ```
2. Install Python.
3. Install Selenium and WebDriver Manager:
   ```bash
   pip install selenium
   pip install webdriver-manager
   ```
4. Download the browser driver (ChromeDriver or GeckoDriver).
5. Set the browser you want to use in `tests/test_insider.py`:
   ```python
   browser = "chrome"  # Change this to "firefox" to use Firefox
   ```
6. Run the test:
   ```bash
   python tests/test_insider.py
   ```

## Notes

- The test pages are written independently and can be executed separately. For example, you can run only the homepage test if desired.
- To run all tests, simply execute the `main.py` file.
- When an assertion error occurs, the error information, along with the date and time, is recorded on the screenshot.

