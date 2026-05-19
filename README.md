# AI Text-to-Speech with Kokoro-82M

A simple AI Text-to-Speech (TTS) web application built with Python, Streamlit, and the Kokoro-82M model from Hugging Face.

The application converts text into realistic speech locally and allows users to generate and download audio directly from the browser.

---

# Features

* Text-to-Speech generation using AI
* Streamlit web interface
* Local inference (works offline after model download)
* Audio playback inside the browser
* Download generated audio
* Hugging Face model integration
* Simple and clean UI

---

# Technologies Used

* Python
* Streamlit
* PyTorch
* Hugging Face Transformers
* Kokoro-82M
* NumPy
* SoundFile

---

# Project Structure

```bash
project/
│
├── app.py
├── requirements.txt
├── README.md
└── generated_audio/
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/rafaelraah/voiceGenerator_kokoroTTS.git
cd ttsKokoro
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

```bash
streamlit run app.py
```

The application will open in your browser automatically.

---

# Example

Type some text:

```text
Hello! This is an AI generated voice using Kokoro.
```

Click:

```text
Generate Audio
```

The generated speech will be played directly in the browser.

---

# Model Information

This project uses:

* Kokoro-82M
* Hugging Face Hub
* PyTorch backend

The model is downloaded automatically the first time the application runs.

---

# Notes

* The first execution may take longer because the AI model needs to be downloaded.
* After the first download, the model works locally/offline.
* GPU is optional but improves performance.

---

# Requirements

Recommended:

* Python 3.10+
* 8GB RAM minimum
* Internet connection for the first model download

---

# Streamlit application

URL: https://voicegeneratorkokoro.streamlit.app/

---

# Future Improvements

* Multiple voice support
* Language selection
* Audio history
* MP3 export
* GPU optimization
* Docker support

---

# License

This project is for educational purposes.

---

# Author

Rafael Nascimento
