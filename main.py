import os
from yt_dlp import YoutubeDL

# Path to your FFmpeg bin folder — update if different
ffmpeg_path = r'your_ffmpeg_bin_path'  # e.g., r'C:\ffmpeg\bin'

# Folder where MP3 files will be saved
output_folder = 'downloads'

# Create downloads folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Path to your text file with YouTube URLs (one per line)
links_file = r'C:\Users\ACER\Documents\VSCode\Python-Files\youtube_links.txt'

# yt-dlp options for mp3 extraction
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': ffmpeg_path,
    'quiet': False,
    'no_warnings': True,
}

def download_mp3_from_links(file_path):
    with open(file_path, 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    with YoutubeDL(ydl_opts) as ydl:
        for url in links:
            print(f'Downloading: {url}')
            try:
                ydl.download([url])
                print('Done!\n')
            except Exception as e:
                print(f'Error downloading {url}: {e}\n')

if __name__ == '__main__':
    download_mp3_from_links(links_file)
# This script downloads MP3 files from YouTube links specified in a text file.
