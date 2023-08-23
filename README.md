# Game Price Scraper README

This script allows you to compare game prices across different online stores including Steam, Microsoft Store, and GOG. The script uses Selenium, a web automation framework, to navigate through the websites and extract game price information. The extracted data will help you quickly compare prices and make informed purchasing decisions.

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Supported Stores](#supported-stores)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Introduction

This script demonstrates how to use Selenium for web scraping. It navigates through the Steam, Microsoft Store, and GOG websites to find the price of a game based on user input. By executing this script, you can conveniently compare prices across these platforms.

## Setup

1. Clone this repository to your local machine.
2. Make sure you have Python installed. If not, download and install it from [Python's official website](https://www.python.org/).
3. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

Download the appropriate WebDriver for your browser and operating system (Edge in this case) from Microsoft Edge WebDriver.

## Usage

1. Open the game_price_scraper.py file in a code editor.
2. Modify the "Pesquina" variable with the game title you want to search for.
3. Set up the WebDriver's path in the browser = wd.Edge() line. Provide the path to the downloaded Edge WebDriver.
4. Run the script:
   python game_price_scraper.py
5. The script will navigate through the websites, extract game prices, and display the results.

## Supported Stores
  The script currently supports the following online stores:
    - Steam
    - Microsoft Store
    - GOG
    - Playstation Store
  I´ll be adding more online stores soon!!

## Dependencies

 - 'selenium': A web automation framework for interacting with web pages.
 - 'time': A Python module for adding delays and controlling time-related functions.

## Contributing
  Contributions are welcome! If you have any improvements, bug fixes, or new features to add, feel free to fork this repository and submit a pull request.

---

**Disclaimer:** This project is intended for educational purposes only. Be sure to review and respect the terms of use of any website you scrape. Always follow ethical scraping practices and avoid overloading websites with requests.

---

*This project is being undertaken by a group of colleagues as part of an evaluative project for our technical course. In the near future, we will be developing a GUI to enhance user interaction.*



