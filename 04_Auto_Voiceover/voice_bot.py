from gtts import gTTS
import os

def generate_voiceover():
    # --- FIX START ---
    # Get the folder where THIS script is currently living
    current_folder = os.path.dirname(__file__)
    
    # Create the full path to the files (Folder + Filename)
    input_path = os.path.join(current_folder, "story.txt")
    output_path = os.path.join(current_folder, "story_audio.mp3")
    # --- FIX END ---

    # Check if the story file exists using the FULL path
    if not os.path.exists(input_path):
        print(f"❌ Error: Could not find file at: {input_path}")
        return

    print(f"📖 Reading text from: {input_path}")
    
    with open(input_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    if not full_text.strip():
        print("❌ Error: The story file is empty!")
        return

    print("⏳ Sending text to Google (using Indian English accent)...")

    # tld='co.in' -> Uses Google India for the accent
    tts = gTTS(text=full_text, lang='en', tld='co.in', slow=False)

    tts.save(output_path)
    print(f"✅ Voiceover saved as: {output_path}")
    
    print("▶️ Playing audio preview...")
    os.system(f'start "" "{output_path}"')

if __name__ == "__main__":
    generate_voiceover()