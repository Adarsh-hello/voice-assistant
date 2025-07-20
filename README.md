# 🤖 Voice Assistant - Jarvis Using Python

This is a Python-based voice assistant named **Jarvis** that can respond to various voice commands like searching Wikipedia, playing YouTube videos, telling time/date/weather, opening websites, sending emails, and more!

---

## 📌 Features

- 🎙️ Voice Recognition using `speech_recognition`
- 🗣️ Voice Response using `pyttsx3`
- 🌐 Wikipedia Search
- 🕒 Tells Date and Time
- 📺 Plays songs on YouTube
- 📧 Sends Emails
- ☁️ Tells current Weather (via `wttr.in`)
- 🔍 Opens websites like YouTube and Google
- 👤 Greets based on the time of day

---

## 📁 Project Structure

voice-assistant/
│
├── voice_assistant.py # Main assistant script
├── requirements.txt # All Python dependencies
└── README.md # Project description file (this one!)

yaml
Copy code

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Adarsh-hello/voice-assistant.git
   cd voice-assistant
(Optional) Create a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate  # On Windows
Install required packages:

bash
Copy code
pip install -r requirements.txt
▶️ Run the Assistant
bash
Copy code
python voice_assistant.py
Speak commands like:

"What is Python"

"Who is the president of India"

"Play Believer song"

"Open YouTube"

"What's the weather"

"Send email"

"Stop" or "Exit" to quit

🧠 Dependencies
Make sure the following Python libraries are installed:

speechrecognition

pyttsx3

datetime

wikipedia

webbrowser

pywhatkit

requests

smtplib

All are listed in requirements.txt.

📸 Screenshots
Add screenshots of your project here if you have any (optional).

📬 Note on Email
To use the email functionality:

Enable less secure apps or use App Password for Gmail.

Replace the dummy email/password in the code with your actual email credentials (never upload them to GitHub!).

📄 License
This project is open-source and available under the MIT License (add one if needed).

🙋‍♂️ Author
Adarsh Tiwari
GitHub: @Adarsh-hello
