import time
import asyncio

# Import the NEW workers we built today
# Note: Ensure the filenames match exactly what you saved!
import voice_bot_wrapper  # The robust CLI wrapper
import vid_sub_maker      # The subtitle-enabled video renderer

def run_studio():
    print("🎬 --- STARTING YOUTUBE AUTOMATION STUDIO (PRO) --- 🎬")
    start_time = time.time()
    
    # STEP 1: GENERATE VOICE & SUBTITLES
    print("\n🗣️  Phase 1: Generating Audio & Subtitles...")
    # We call the CLI wrapper function directly
    voice_bot_wrapper.generate_voice_cli()
    
    print("✅ Phase 1 Complete.")

    # STEP 2: RENDER VIDEO
    print("\n🎞️  Phase 2: Rendering Video with Subtitles...")
    # We call the video maker function
    vid_sub_maker.create_video()
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    print(f"\n✨ DONE! Total process took {duration} seconds.")
    print("🚀 Your viral video is ready for upload!")

if __name__ == "__main__":
    # Since the wrapper isn't async, we don't need asyncio.run() anymore
    run_studio()