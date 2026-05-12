Project 1 :

# 🎥 YouTube Audio Transcription with Groq Whisper

An AI-powered Python project that downloads YouTube audio, converts it into MP3 format, transcribes speech using Groq Whisper, and saves the transcript into a CSV file.

---

# 🚀 Features

- Download audio directly from YouTube videos
- Extract only the first 5 minutes of audio
- Convert audio into MP3 format using FFmpeg
- Transcribe speech into text using Groq Whisper
- Process multiple YouTube videos automatically
- Save transcripts into a structured CSV file
- Automatic temporary file cleanup
- File size protection for API upload limits
- Retry handling for stable downloads

---

# 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| yt-dlp | Download YouTube audio |
| FFmpeg | Convert audio to MP3 |
| Groq Whisper | Speech-to-text transcription |
| Pandas | Create CSV output |
| python-dotenv | Load environment variables |

---

# 📂 Project Structure

```text
youtube-transcription/
│
├── main.py
├── README.md
├── requirements.txt
├── .env.example
├── text.csv
└── screenshots/
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/youtube-transcription.git
```

---

## 2. Navigate to Project Folder

```bash
cd youtube-transcription
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Required Packages

Create a `requirements.txt` file with:

```txt
pandas
yt-dlp
groq
python-dotenv
ffmpeg-python
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🔄 Workflow

```text
YouTube URL
    ↓
yt-dlp downloads audio
    ↓
FFmpeg converts audio to MP3
    ↓
Groq Whisper transcribes speech
    ↓
Pandas stores results
    ↓
CSV file generated
```

---

# 🧠 How the System Works

## Step 1 — Download Audio

The application uses `yt-dlp` to extract audio from YouTube videos.

---

## Step 2 — Convert to MP3

Audio is converted into MP3 format using FFmpeg for better compatibility.

---

## Step 3 — Partial Download Optimization

Only the first 5 minutes of the video are downloaded to:

- Reduce file size
- Improve processing speed
- Stay within API upload limits

---

## Step 4 — Transcription

The MP3 audio is sent to Groq Whisper:

```python
model="whisper-large-v3-turbo"
```

The AI converts speech into text.

---

## Step 5 — Save Output

The transcript is stored in a CSV file:

```text
text.csv
```

---

# 📊 Example Output

| title | url | text |
|---|---|---|
| Python Tutorial | youtube.com/... | Welcome to this tutorial... |

---

# 🖥 Example Console Output

```text
Downloading: https://www.youtube.com/watch?v=xxxx

Downloaded: Python Tutorial
File Size: 3.42 MB

Transcribing audio...

Transcription complete.

Saved CSV: text.csv
```

---

# 🔒 Error Handling Included

This project includes:

- Retry handling for failed downloads
- File size validation
- Missing API key validation
- MP3 existence validation
- Exception handling for transcription failures

---

# 📈 Future Improvements

- Streamlit Web UI
- Real-time transcription
- Multi-language transcription
- Video summarization
- RAG-based Q&A system
- Vector database integration
- LangChain integration
- Pinecone embeddings
- AI chatbot over transcripts

---

# 🧪 Sample YouTube URLs

```python
YOUTUBE_VIDEOS = [
    "https://www.youtube.com/watch?v=Z3_PwvvfxIU",
    "https://www.youtube.com/watch?v=DxREm3s1scA"
]
```

---

# 📌 Key Optimizations Used

## Android Client Fix

```python
"player_client": ["android"]
```

Improves YouTube extraction stability.

---

## Audio Size Protection

```python
if file_size_mb > 24:
```

Prevents large uploads exceeding API limits.

---

## Temporary Directory Cleanup

```python
with tempfile.TemporaryDirectory()
```

Automatically removes downloaded files after processing.

---

# 🤝 Contributing

Pull requests and improvements are welcome.

Feel free to fork the repository and submit enhancements.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed as part of AI Engineering / Generative AI learning projects.

---

# ⭐ If You Like This Project

Please consider giving the repository a star ⭐ on GitHub.
