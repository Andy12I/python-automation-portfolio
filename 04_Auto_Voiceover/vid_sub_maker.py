import os
import subprocess

# --- SETTINGS ---
IMAGE_FILE = "background.jpg"
AUDIO_FILE = "story_audio_pro.mp3"
SUBTITLE_FILE = "story_audio_pro.vtt" # FFmpeg handles SRT content inside .vtt files just fine
OUTPUT_VIDEO = "final_video_with_subs.mp4"
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

def create_video():
    current_folder = os.path.dirname(__file__)
    
    # Define files
    # We use simple filenames for the command (because we set cwd)
    # But we need full paths just to check if they exist first
    image_full_path = os.path.join(current_folder, IMAGE_FILE)
    audio_full_path = os.path.join(current_folder, AUDIO_FILE)
    subtitle_full_path = os.path.join(current_folder, SUBTITLE_FILE)
    video_full_path = os.path.join(current_folder, OUTPUT_VIDEO)

    # 1. Safety Checks
    if not os.path.exists(subtitle_full_path):
        print("❌ Error: Subtitle file not found! Run the wrapper script first.")
        return

    print("🎬 Starting Video Rendering...")

    # 2. PRO STYLE: Yellow Text with a Semi-Transparent Black Box behind it
    # Alignment=2 (Bottom Center), MarginV=20 (Lift it up slightly)
    style = "FontSize=24,PrimaryColour=&H00FFFF,BackColour=&H80000000,BorderStyle=3,Outline=0,Shadow=0,Alignment=2,MarginV=25"

    command = [
        FFMPEG_PATH,
        "-y",
        "-loop", "1",
        "-i", IMAGE_FILE,
        "-i", AUDIO_FILE,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-b:a", "192k",
        
        # 3. The Filter
        # We assume the file is in the current folder (handled by cwd below)
        "-vf", f"scale=trunc(iw/2)*2:trunc(ih/2)*2,subtitles='{SUBTITLE_FILE}':force_style='{style}'",
        
        "-pix_fmt", "yuv420p",
        "-shortest",
        OUTPUT_VIDEO
    ]

    try:
        # Run inside the folder so FFmpeg sees the files directly
        subprocess.run(command, check=True, cwd=current_folder)
        
        print(f"\n✅ SUCCESS! Video saved as: {OUTPUT_VIDEO}")
        print("▶️ Opening video...")
        os.system(f'start "" "{video_full_path}"')
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ FFmpeg Error: {e}")

if __name__ == "__main__":
    create_video()