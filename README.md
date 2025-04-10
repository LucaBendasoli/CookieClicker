# Cookie Clicker Automation

This project automates the process of playing the Cookie Clicker game using Selenium WebDriver.
Even though it's simple, I used this opportunity to re-build my first automation project but this time using object-oriented programming, abstracting Selenium functions into classes.

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

## Features

- Start a Cookie Clicker run

## Usage

1. Run the main.py script:
    ```sh
    python main.py
    ```

2. The script will open the Cookie Clicker game, select the language, and start clicking the big cookie, looking for upgrades and buildings to buy as soon as they are available.

## Contribution

1. Fork the project.
2. Create a new branch: `git checkout -b my-new-feature`
3. Make your changes and commit: `git commit -m 'feat: add new functionality'`
4. Push to the remote repository: `git push origin my-new-feature`
5. Open a pull request.
