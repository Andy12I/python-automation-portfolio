import yt_dlp
import os

def download_video():
    # 1. Ask the user for the link
    link = input("🔗 Paste the YouTube Link here: ")
    
    # 2. Ask if they want just Audio (for podcasts) or Video
    choice = input("Type 'v' for Video or 'a' for Audio only: ").lower()
    
    # Save in the current folder
    save_path = os.getcwd()
    
    # 3. Configure options based on choice
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
    }
    
    if choice == 'a':
        # Audio Settings (Convert to MP3)
        print("🎵 Configuring for Audio Download...")
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    else:
        # Video Settings
        print("🎬 Configuring for Video Download...")
        ydl_opts['format'] = 'best' # Get best single file available

    # 4. Run the download
    try:
        print(f"🚀 Starting download for: {link}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("\n✅ Done! Check your folder.")
        
    except Exception as e:
        print(f"\n❌ Something went wrong: {e}")

# This line makes the script run
if __name__ == "__main__":
    download_video()