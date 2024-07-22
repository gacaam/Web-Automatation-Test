# Test Automation Project
This is an automated script to test features of this demo [website](https://www.demoblaze.com/index.html). The script are built in Python using the Selenium WebDriver framework.

## System Set Up
### Prerequisites
- Python 3.6 or later
- Google Chrome browser
- [ChromeDriver executable](https://sites.google.com/chromium.org/driver/downloads?authuser=0) (make sure it matches your Chrome version)

## Steps to Run the Project
Execute these commands in the terminal.

1. **Clone the repository**:
    ```sh
    git clone https://github.com/gacaam/Web-Automatation-Test.git
    cd Web-Automatation-Test
    ```

2. **Create and activate virtual environment**:
    ```sh
    python -m venv automatedtest
    .\automatedtest\Scripts\activate # Windows
    source automatedtest/bin/activate  # macOS/Linux
    ```
3. **Install required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the test**:
- To run all test cases:
    ```sh
    python main.py
    ```
- To run a specific test case:
    ```sh
    python -m unittest tests.[test_file_name]
    ```

## Additional Notes
Ensure ChromeDriver PATH in each test setup is correctly specified according to its location in your device.
