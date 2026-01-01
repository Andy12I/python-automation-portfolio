import asyncio
import edge_tts

# --- HARDCODED TEST ---
# We use this simple text to rule out any weird characters in your story.txt
TEXT = "This is a diagnostic test to see if the timestamp logic is working."
VOICE = "en-US-AriaNeural"  # We use Aria because she is 100% reliable for tests
OUTPUT_FILE = "debug_test.vtt"

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:06.3f}"

async def run_test():
    print(f"🔎 Testing with voice: {VOICE}")
    print(f"📝 Text: '{TEXT}'")
    
    communicate = edge_tts.Communicate(TEXT, VOICE)
    
    sub_data = []
    
    # We explicitly print EVERY chunk type to see what the server is sending
    print("\n📡 Connecting to Server stream...")
    
    async for chunk in communicate.stream():
        # Print the type of every single packet we receive
        # We expect: 'audio', 'WordBoundary', etc.
        if chunk["type"] != "audio":
            print(f"   Received Event: {chunk['type']}") 
            
        if chunk["type"] == "WordBoundary":
            sub_data.append(chunk)

    print(f"\n✅ Stream Finished. Total WordBoundaries captured: {len(sub_data)}")
    
    if len(sub_data) > 0:
        print("🎉 SUCCESS! Timestamps received. Writing VTT file...")
        with open(OUTPUT_FILE, "w", encoding="utf-8") as vtt:
            vtt.write("WEBVTT\n\n")
            for word in sub_data:
                start = word["offset"] / 10_000_000
                end = (word["offset"] + word["duration"]) / 10_000_000
                vtt.write(f"{format_time(start)} --> {format_time(end)}\n")
                vtt.write(f"{word['text']}\n\n")
        print(f"📄 Saved: {OUTPUT_FILE}")
    else:
        print("❌ FAILURE: Still no timestamps received.")

if __name__ == "__main__":
    asyncio.run(run_test())