import os
import subprocess
import sys

# --- SETTINGS ---
# 1. Get current folder (GPS)
current_folder = os.path.dirname(__file__)

# 2. Define Files
TEXT_FILE = os.path.join(current_folder, "story.txt")
AUDIO_FILE = "story_audio_pro.mp3"       # Relative path for the command
SUBTITLE_FILE = "story_audio_pro.vtt"    # Relative path for the command
VOICE = "en-IN-PrabhatNeural"            # Back to your Indian accent!

def generate_voice_cli():
    print("🎬 --- STARTING AUDIO ENGINE (WRAPPER MODE) ---")

    # 1. Read the text
    print(f"📖 Reading text from: story.txt")
    try:
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            text_content = f.read().replace('"', '').replace("'", "") 
            # ^ Cleanup: Remove quotes from story so they don't break the command line
    except FileNotFoundError:
        print("❌ Error: story.txt not found!")
        return

    print(f"🎙️  Generating Audio & Subtitles using {VOICE}...")

    # 2. Construct the Magic Command
    # This is exactly what you ran manually that worked!
    # "python -m edge_tts --text '...' --write-media ... --write-subtitles ..."
    command = [
        sys.executable, "-m", "edge_tts",
        "--voice", VOICE,
        "--text", text_content,
        "--write-media", AUDIO_FILE,
        "--write-subtitles", SUBTITLE_FILE
    ]

    # 3. Execute!
    try:
        # We run this inside the folder so the output files appear right there
        result = subprocess.run(
            command, 
            cwd=current_folder, 
            capture_output=True, 
            text=True, 
            encoding="utf-8"
        )
        
        if result.returncode == 0:
            print("✅ Success! The CLI tool finished.")
            print(f"   - Audio: {AUDIO_FILE}")
            print(f"   - Subtitles: {SUBTITLE_FILE}")
        else:
            print("❌ The tool failed.")
            print("Error details:", result.stderr)
            
    except Exception as e:
        print(f"❌ System Error: {e}")

if __name__ == "__main__":
    generate_voice_cli()