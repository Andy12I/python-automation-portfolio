import asyncio
import edge_tts
import os

# --- SETTINGS ---
# The file to read
INPUT_FILE = "story.txt"
# The file to save
OUTPUT_FILE = "story_audio_pro.mp3"

# VOICE SELECTION
# en-IN-PrabhatNeural  -> Indian Male (Natural)
# en-IN-NeerjaNeural   -> Indian Female (Natural)
# hi-IN-MadhurNeural   -> Hindi Male
# hi-IN-SwaraNeural    -> Hindi Female
SELECTED_VOICE = "en-IN-PrabhatNeural"

async def generate_voice():
    # 1. Locate files safely
    current_folder = os.path.dirname(__file__)
    text_path = os.path.join(current_folder, INPUT_FILE)
    audio_path = os.path.join(current_folder, OUTPUT_FILE)

    # 2. Read the story
    if not os.path.exists(text_path):
        print(f"❌ Error: Could not find {INPUT_FILE}")
        return

    print(f"📖 Reading story from {INPUT_FILE}...")
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read()

    if not text.strip():
        print("❌ Error: Story file is empty!")
        return

    print(f"🎙️ Generative Voice: {SELECTED_VOICE}")
    print("⏳ Converting... (This is high quality, give it a moment)")

    # 3. The Magic (Edge TTS)
    communicate = edge_tts.Communicate(text, SELECTED_VOICE)
    await communicate.save(audio_path)

    print(f"✅ Saved high-quality audio: {OUTPUT_FILE}")
    
    # 4. Play it
    print("▶️ Playing...")
    os.system(f'start "" "{audio_path}"')

if __name__ == "__main__":
    # We need a special loop to run 'async' code
    asyncio.run(generate_voice())