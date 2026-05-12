import os
import glob
import tempfile
import pandas as pd
import yt_dlp

from groq import Groq
from dotenv import load_dotenv, find_dotenv

# ==========================================
# Load Environment Variables
# ==========================================
load_dotenv(find_dotenv())

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found in .env file"
    )

# ==========================================
# Groq Client
# ==========================================
client = Groq(api_key=GROQ_API_KEY)

# ==========================================
# YouTube URLs
# ==========================================
YOUTUBE_VIDEOS = [
    "https://www.youtube.com/watch?v=Z3_PwvvfxIU",
    "https://www.youtube.com/watch?v=DxREm3s1scA"
]

# ==========================================
# Transcribe Function
# ==========================================
def transcribe(youtube_url):

    with tempfile.TemporaryDirectory() as tmpdir:

        output_template = os.path.join(
            tmpdir,
            "audio.%(ext)s"
        )

        # ==========================================
        # yt-dlp Configuration
        # ==========================================
        ydl_opts = {

            # Better compatible audio format
            "format": "bestaudio[ext=m4a]/bestaudio/best",

            # Output template
            "outtmpl": output_template,

            # General settings
            "quiet": False,
            "noplaylist": True,
            "nocheckcertificate": True,

            # Retry handling
            "retries": 10,
            "fragment_retries": 10,
            "socket_timeout": 30,

            # Better stability
            "concurrent_fragment_downloads": 1,

            # IMPORTANT FIX:
            # Android client works better currently
            "extractor_args": {
                "youtube": {
                    "player_client": ["android"]
                }
            },

            # ==========================================
            # Download ONLY first 5 minutes
            # ==========================================
            "download_ranges": lambda info_dict, ydl: [
                {
                    "start_time": 0,
                    "end_time": 300,
                }
            ],

            # Needed for partial downloads
            "force_keyframes_at_cuts": True,

            # ==========================================
            # Convert audio to MP3
            # ==========================================
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",

                    # Smaller output size
                    "preferredquality": "64",
                }
            ],
        }

        try:

            print(f"\nDownloading: {youtube_url}")

            # ==========================================
            # Download Audio
            # ==========================================
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                info = ydl.extract_info(
                    youtube_url,
                    download=True
                )

                title = info.get(
                    "title",
                    "Unknown Title"
                )

            # ==========================================
            # Find Downloaded MP3
            # ==========================================
            downloaded_files = glob.glob(
                os.path.join(tmpdir, "*.mp3")
            )

            if not downloaded_files:

                raise FileNotFoundError(
                    "MP3 file not found."
                )

            file_path = downloaded_files[0]

            # ==========================================
            # File Size Check
            # ==========================================
            file_size_mb = (
                os.path.getsize(file_path)
                / (1024 * 1024)
            )

            print(f"Downloaded: {title}")

            print(
                f"File Size: "
                f"{file_size_mb:.2f} MB"
            )

            # ==========================================
            # File Size Protection
            # ==========================================
            if file_size_mb > 24:

                raise Exception(
                    f"Audio too large: "
                    f"{file_size_mb:.2f} MB"
                )

            # ==========================================
            # Transcription
            # ==========================================
            print("Transcribing audio...")

            with open(file_path, "rb") as audio_file:

                transcription = (
                    client.audio.transcriptions.create(
                        file=audio_file,
                        model="whisper-large-v3-turbo"
                    )
                )

            print("Transcription complete.")

            return (
                title,
                youtube_url,
                transcription.text.strip()
            )

        except Exception as e:

            raise Exception(
                f"\nError processing:\n"
                f"{youtube_url}\n\n{str(e)}"
            )

# ==========================================
# Process Videos
# ==========================================
transcriptions = []

for youtube_url in YOUTUBE_VIDEOS:

    try:

        result = transcribe(youtube_url)

        transcriptions.append(result)

        print(
            f"Finished: {youtube_url}"
        )

    except Exception as e:

        print(
            f"Failed: {youtube_url}"
        )

        print(e)

# ==========================================
# Create DataFrame
# ==========================================
df = pd.DataFrame(
    transcriptions,
    columns=[
        "title",
        "url",
        "text"
    ]
)

# ==========================================
# Save CSV
# ==========================================
output_csv = "text.csv"

df.to_csv(
    output_csv,
    index=False
)

# ==========================================
# Final Output
# ==========================================
print("\n================================")
print("Transcription Complete")
print("================================")

print(f"\nSaved CSV: {output_csv}")

print("\nPreview:\n")

print(df.head())