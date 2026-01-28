# 🐍 Python Automation Portfolio

Welcome to my collection of Python automation tools! This repository documents my journey learning software development, featuring practical scripts for data scraping, system maintenance, and media processing.

## 📂 Projects Overview

### 1. 📺 YouTube Media Downloader (CLI)
A command-line tool to download high-quality video or audio from YouTube.
* **Features:**
    * Interactive menu (choose Video vs. Audio).
    * **FFmpeg Integration:** Automatically converts streams to clean MP3s.
    * **4K Support:** Handles high-resolution video formats.
    * Error handling for missing videos or connection drops.
* **Tech Stack:** `yt-dlp`, `ffmpeg`, `os`

### 2. 📰 Automated News Scraper
A bot that gathers real-time headlines from news websites.
* **Features:**
    * Scrapes live data using HTTP requests.
    * Parses HTML content to extract specific headlines and links.
    * Saves summaries to local text files for offline reading.
* **Tech Stack:** `requests`, `beautifulsoup4`
## 🚀 Overview
A collection of professional-grade automation scripts designed to solve real-world data extraction and process automation challenges. This repository demonstrates proficiency in **Python**, **Selenium**, **Data Engineering**, and **Headless Browser Technology**.

## 🛠️ Projects

### 1. E-Commerce Data Pipeline (`web_scraper/`)
**Objective:** Automated extraction of product data (Pricing, Titles, Availability) from dynamic e-commerce platforms.
* **Tech Stack:** Python, Selenium WebDriver, CSV module.
* **Key Features:**
    * **Resilient Logic:** Implements `try/except` blocks to handle network instability and missing elements.
    * **Data Integrity:** Solves complex encoding issues (`UTF-8-SIG`) for seamless Excel integration.
    * **Deep Extraction:** Navigates DOM parent-child relationships to extract hidden attributes (e.g., full book titles).
    * **Headless Operation:** Includes `headless_books.py` for background execution on cloud servers (AWS/Linux).

### 2. Multi-Topic Batch Processor
**Objective:** A scalable scraper that processes lists of keywords to generate aggregated research reports.
* **Key Features:**
    * Iterates through multiple search terms automatically.
    * Generates structured CSV reports with timestamps and source URLs.

## 💻 Technical Skills Demonstrated
* **Web Automation:** Handling dynamic content, explicit waits, and browser options.
* **Data Engineering:** Cleaning, structuring, and serializing data into usable formats (CSV).
* **Version Control:** Professional Git workflow (Feature branching, clean commits).
* **Error Handling:** Robust exception management to prevent script crashes during long-running tasks.

## ⚙️ How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Andy12I/python-automation-portfolio.git](https://github.com/YOUR_USERNAME/python-automation-portfolio.git)
    ```
2.  Install dependencies:
    ```bash
    pip install selenium webdriver_manager
    ```
3.  Run the headless scraper:
    ```bash
    python web_scraper/headless_books.py
    ```

### 3. 🧹 Desktop File Cleaner
An automation script to organize cluttered directories.
* **Features:**
    * Scans a target folder for loose files.
    * Intelligently sorts files into sub-folders based on extension (Images, Docs, Media).
    * Moves files safely using system operations.
* **Tech Stack:** `os`, `shutil`

---

## 🚀 How to Run These Tools

### Prerequisites
You will need Python 3.x installed.
Install the required libraries:

```bash
pip install yt-dlp requests beautifulsoup4

Note: For the YouTube Downloader, you must have FFmpeg installed and added to your system PATH.

Usage
Navigate to the project folder and run the script:

Bash

# Example: Running the Downloader
python 03_Youtube_Downloader/downloader.py
# Python Automation & Scraping Portfolio



---
*Author: [Andy12I] | Open to Remote Python Opportunities*