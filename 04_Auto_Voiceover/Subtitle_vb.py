import asyncio
import edge_tts
import os

# --- SETTINGS ---
current_folder = os.path.dirname(__file__)
TEXT_FILE = os.path.join(current_folder, "story.txt")
AUDIO_FILE = os.path.join(current_folder, "story_audio_pro.mp3")
SUBTITLE_FILE = os.path.join(current_folder, "story_audio_pro.vtt")

# Let's switch voice momentarily to test if "Prabhat" is the problem
# We will use Aria (very reliable) for this test.
VOICE = "en-US-AriaNeural" 

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:06.3f}"

async def generate_voice():
    print(f"📖 Reading text from: {TEXT_FILE}...")
    try:
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            text = f.read()
            print(f"   (Read {len(text)} characters)")
    except FileNotFoundError:
        print("❌ Error: story.txt not found!")
        return

    print(f"🎙️  Requesting Audio & Timing from {VOICE}...")
    communicate = edge_tts.Communicate(text, VOICE)
    
    sub_data = []
    
    with open(AUDIO_FILE, "wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                # DEBUG: Print a dot for every word found to prove it's working
                print(".", end="", flush=True) 
                sub_data.append(chunk)

    print(f"\n\n📊 Diagnostics:")
    print(f"   - Audio File Created? {os.path.exists(AUDIO_FILE)}")
    print(f"   - Total Words Captured: {len(sub_data)}")

    if len(sub_data) == 0:
        print("❌ CRITICAL: The AI sent audio but ZERO timing data.")
        print("   This usually means the Voice doesn't support timestamps")
        print("   or the text is being filtered.")
        return

    print("✍️  Writing Subtitle File...")
    with open(SUBTITLE_FILE, "w", encoding="utf-8") as vtt:
        vtt.write("WEBVTT\n\n")
        
        start_time = 0
        sentence = ""
        
        for i, word in enumerate(sub_data):
            if sentence == "":
                start_time = word["offset"] / 10000000
            
            sentence += word["text"]
            
            if len(sentence) > 30 or i == len(sub_data) - 1:
                end_time = (word["offset"] + word["duration"]) / 10000000
                vtt.write(f"{format_time(start_time)} --> {format_time(end_time)}\n")
                vtt.write(f"{sentence.strip()}\n\n")
                sentence = ""

    print(f"✅ Saved Subtitles: {SUBTITLE_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_voice())