import yt_dlp
import os

def download_video():
    link = input("🔗 Paste the YouTube Link here: ")
    choice = input("Type 'v' for Video or 'a' for Audio only: ").lower()
    
    save_path = os.getcwd()
    
    # Basic Options
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        # We tell it exactly where FFmpeg lives
        'ffmpeg_location': r'C:\ffmpeg\bin', 
    }
    
    if choice == 'a':
        print("🎵 Configuring for Audio Download...")
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        print("🎬 Configuring for Video Download...")
        ydl_opts['format'] = 'best'

    try:
        print(f"🚀 Starting download for: {link}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("\n✅ Done! Check your folder.")
        
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

if __name__ == "__main__":
    download_video()