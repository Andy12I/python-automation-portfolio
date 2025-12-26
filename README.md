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