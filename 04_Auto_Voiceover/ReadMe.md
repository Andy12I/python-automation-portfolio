# 🎬 YouTube Automation Studio (Pro Edition)

A full-stack Python automation pipeline that converts text scripts into viral-ready videos with **Neural AI Voiceovers** and **Burned-in Subtitles**.

## 🚀 Features
* **Neural AI Voiceovers:** Uses `edge-tts` to generate human-like speech (Supports multiple accents including Indian English).
* **Auto-Subtitles:** Automatically generates timestamped subtitles (`.vtt`) synced perfectly with the audio.
* **Video Rendering Engine:** Uses `FFmpeg` to merge audio, background visuals, and burn subtitles directly onto the video.
* **Robust CLI Wrapper:** Bypasses library limitations by orchestrating the official `edge-tts` command line tool for 100% reliability.
* **"Shorts" Ready:** Default styling includes high-visibility yellow text with black backgrounds, optimized for mobile viewing.

## 🛠️ Tech Stack
* **Python 3.13**
* **Core Libraries:** `subprocess`, `asyncio`, `edge-tts`
* **Video Engine:** FFmpeg (Must be installed on system)

## 📂 Project Structure
* `main.py` - The "Master Switch" that runs the entire pipeline.
* `voice_bot_wrapper.py` - Generates audio and subtitle files using the CLI method.
* `vid_sub_maker.py` - Renders the final video with subtitle burning filters.
* `story.txt` - Input file for your script (Not uploaded to Git).
* `background.jpg` - Input background image (Not uploaded to Git).

## 📋 Setup & Usage

### 1. Install Dependencies
```bash
pip install edge-tts
That is the final professional touch. A good README explains what the software does now that it has evolved.

Here is the updated README.md that highlights your new Subtitle Engine and Robust Wrapper architecture.

Update Instructions
Open 04_Auto_Voiceover/README.md.

Delete everything currently in there.

Paste this new version:

Markdown

# 🎬 YouTube Automation Studio (Pro Edition)

A full-stack Python automation pipeline that converts text scripts into viral-ready videos with **Neural AI Voiceovers** and **Burned-in Subtitles**.

## 🚀 Features
* **Neural AI Voiceovers:** Uses `edge-tts` to generate human-like speech (Supports multiple accents including Indian English).
* **Auto-Subtitles:** Automatically generates timestamped subtitles (`.vtt`) synced perfectly with the audio.
* **Video Rendering Engine:** Uses `FFmpeg` to merge audio, background visuals, and burn subtitles directly onto the video.
* **Robust CLI Wrapper:** Bypasses library limitations by orchestrating the official `edge-tts` command line tool for 100% reliability.
* **"Shorts" Ready:** Default styling includes high-visibility yellow text with black backgrounds, optimized for mobile viewing.

## 🛠️ Tech Stack
* **Python 3.13**
* **Core Libraries:** `subprocess`, `asyncio`, `edge-tts`
* **Video Engine:** FFmpeg (Must be installed on system)

## 📂 Project Structure
* `main.py` - The "Master Switch" that runs the entire pipeline.
* `voice_bot_wrapper.py` - Generates audio and subtitle files using the CLI method.
* `vid_sub_maker.py` - Renders the final video with subtitle burning filters.
* `story.txt` - Input file for your script (Not uploaded to Git).
* `background.jpg` - Input background image (Not uploaded to Git).

## 📋 Setup & Usage

### 1. Install Dependencies
```bash
pip install edge-tts
Ensure FFmpeg is installed and added to your System PATH.

2. Prepare Your Assets
Create a file named story.txt and paste your video script inside.

Add an image named background.jpg to the folder.

3. Run the Studio
Execute the master script to generate the full video automatically:

Bash

python main.py
4. Output
The tool will generate:

story_audio_pro.mp3 (Audio)

story_audio_pro.vtt (Subtitles)

final_video_with_subs.mp4 (Final Output)

🐛 Troubleshooting
No Subtitles? The system uses a wrapper to ensure timestamps are captured correctly. Ensure voice_bot_wrapper.py is present.

FFmpeg Error? Check that the path to ffmpeg.exe in vid_sub_maker.py matches your installation.