import os
import subprocess

# --- SETTINGS ---
IMAGE_FILE = "background.jpg"
AUDIO_FILE = "story_audio_pro.mp3"
OUTPUT_VIDEO = "final_video.mp4"

# Your correct path
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

def create_video():
    current_folder = os.path.dirname(__file__)
    image_path = os.path.join(current_folder, IMAGE_FILE)
    audio_path = os.path.join(current_folder, AUDIO_FILE)
    video_path = os.path.join(current_folder, OUTPUT_VIDEO)

    if not os.path.exists(image_path):
        print(f"❌ Error: Could not find image at {image_path}")
        return
    if not os.path.exists(audio_path):
        print(f"❌ Error: Could not find audio at {audio_path}")
        return

    # Check for FFmpeg
    if not os.path.exists(FFMPEG_PATH):
        print(f"❌ Error: FFmpeg not found at {FFMPEG_PATH}")
        return

    print("🎬 Starting Video Rendering...")
    print(f"🖼️ Image: {IMAGE_FILE}")
    print(f"🎵 Audio: {AUDIO_FILE}")

    # 3. The FFmpeg Command (With the Fix!)
    command = [
        FFMPEG_PATH,
        "-y",
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        
        # --- NEW FIX: Force width/height to be even numbers ---
        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
        
        "-pix_fmt", "yuv420p",
        "-shortest",
        video_path
    ]

    # 4. Run it
    try:
        subprocess.run(command, check=True)
        print(f"\n✅ SUCCESS! Video saved as: {OUTPUT_VIDEO}")
        print("▶️ Opening video...")
        os.system(f'start "" "{video_path}"')
    except subprocess.CalledProcessError as e:
        print(f"\n❌ FFmpeg Error: {e}")
    except OSError as e:
        print(f"\n❌ System Error: {e}")

if __name__ == "__main__":
    create_video()