Markdown

# 🎬 YouTube Automation Studio (Text-to-Video)

A Python-based automation pipeline that converts text scripts into high-quality AI voiceovers and renders them into ready-to-upload videos.

## 🚀 Features
* **Neural AI Voiceovers:** Uses `edge-tts` to generate natural-sounding speech (Supports Indian accents).
* **Video Rendering:** Automates `FFmpeg` to merge audio and static images.
* **Smart Looping:** Automatically loops background images to match the exact duration of the voiceover.
* **One-Click Studio:** Orchestrates the entire pipeline via a single master script.

## 🛠️ Tech Stack
* **Python 3.13**
* **Libraries:** `edge-tts`, `asyncio`, `subprocess`
* **Engine:** FFmpeg (Video Processing)

## 📋 Setup & Usage

### 1. Install Dependencies
```bash
pip install edge-tts
2. Configure FFmpeg
Ensure FFmpeg is installed. If using a custom path, update the FFMPEG_PATH variable in video_maker.py.

3. Add Content
Story: Paste your script into story.txt.

Visuals: Place a background image named background.jpg in the folder.

4. Run the Studio
Execute the master script to generate both audio and video:

Bash

python main.py
The final output will be saved as final_video.mp4.