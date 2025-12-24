# Python Automation Portfolio

This repository contains a collection of Python scripts demonstrating skills in **Web Scraping**, **Browser Automation (Selenium)**, and **Data Processing (CSV)**.

## 📂 Projects

### 1. The Quote Scraper (`scraper2.py`)
A script that scrapes quotes from a test website and saves them into a structured format.
* **Libraries:** `requests`, `beautifulsoup4`, `csv`
* **Key Features:**
    * Connects to a live URL and parses HTML content.
    * Extracts specific data points (quotes) using CSS selectors.
    * Cleans data and exports it to a **CSV file** automatically.

### 2. The Login Bot (`login_bot3.py`)
An automated testing bot that navigates a secure e-commerce environment.
* **Libraries:** `selenium`, `webdriver-manager`
* **Key Features:**
    * **Headless Mode:** Runs invisibly in the background for efficiency.
    * **Explicit Waits:** Uses `WebDriverWait` to handle dynamic page loading and network latency.
    * **Assertion Logic:** Verifies successful login by checking URL redirections (`try/except` block).
    * **Negative Testing:** Capable of handling and reporting login failures gracefully.

## 🛠️ How to Run

1.  **Install Dependencies:**
    ```bash
    pip install selenium beautifulsoup4 requests webdriver-manager
    ```

2.  **Run the Scraper:**
    ```bash
    python scraper2.py
    ```

3.  **Run the Bot:**
    ```bash
    python login_bot3.py
    ```

## 🚀 Skills Demonstrated
* **Python 3**: Scripting, Loops, File I/O.
* **QA Automation**: Creating robust test cases (Positive & Negative paths).
* **DOM Manipulation**: Locating elements via ID, Class, and Name.
* **Version Control**: Git & GitHub.
