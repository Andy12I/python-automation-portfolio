import asyncio
import time

# Import our two workers (the scripts you just built)
# NOTE: The filenames must match exactly what you saved earlier!
import voicebot_pro
import video_maker

async def run_studio():
    print("🎬 --- STARTING AUTOMATION STUDIO --- 🎬")
    
    # STEP 1: GENERATE VOICE
    print("\n🗣️  Phase 1: Generating Voiceover...")
    start_time = time.time()
    
    # We use 'await' because the voice bot is an Async function
    await voicebot_pro.generate_voice()
    
    print("✅ Phase 1 Complete.")

    # STEP 2: RENDER VIDEO
    print("\n🎞️  Phase 2: Rendering Video...")
    
    # This is a normal function, so we just call it
    video_maker.create_video()
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    
    print(f"\n✨ DONE! Total process took {duration} seconds.")
    print("🚀 Your video is ready for upload!")

if __name__ == "__main__":
    # Run the async studio
    asyncio.run(run_studio())