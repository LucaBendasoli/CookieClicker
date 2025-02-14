# Cookie Clicker Automation

This project automates the process of playing the Cookie Clicker game using Selenium WebDriver.

## Project Structure

- `main.py`: Main file that orchestrates the whole process of playing the Cookie Clicker game.
- `utils/BaseWebDriver.py`: Contains the base WebDriver class for interacting with the web page.
- `utils/CookieClickerDriver.py`: Extends the base WebDriver class with specific methods for playing Cookie Clicker.
- `utils/locators.py`: Contains the locators for the web elements used in the game.

## Requirements

- Python 3.x
- Selenium

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/LucaBendasoli/cookie-clicker-automation.git
    cd cookie-clicker-automation
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main.py script:
    ```sh
    python main.py
    ```

2. The script will open the Cookie Clicker game, select the language, and start clicking the big cookie, looking for upgrades and buildings to buy as soon as they are available.
