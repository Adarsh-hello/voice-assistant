import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import requests

# 🎙️ Initialize 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = male, 1 = female
engine.setProperty('rate', 165)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning Sir!")
    elif hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis. How can I assist you today?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("🧠 Recognizing...")
        query = r.recognize_google(audio)
        print("You said:", query)
    except:
        speak("Sorry, I could not understand. Please say that again.")
        return ""
    return query.lower()

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_app_password")  # App password needed
    server.sendmail("your_email@gmail.com", to, content)
    server.quit()

def get_weather():
    city = "Delhi"
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        response = requests.get(url)
        speak(f"The current weather in {city} is {response.text}")
    except:
        speak("Unable to fetch weather info right now.")

def run_assistant():
    greet()
    while True:
        query = take_command()

        # 🎓 Wikipedia block
        if 'who is' in query or 'what is' in query or 'tell me about' in query or 'define' in query or 'information about' in query:
            speak("Searching Wikipedia...")
            try:
                topic = query.replace("wikipedia", "").replace("who is", "").replace("what is", "").replace("tell me about", "").replace("define", "").strip()
                results = wikipedia.search(topic)
                if results:
                    page_title = results[0]
                    result = wikipedia.summary(page_title, sentences=2)
                    speak("According to Wikipedia")
                    speak(result)
                else:
                    speak("Sorry, I couldn't find anything related to that.")
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"Your query was too broad. Did you mean {e.options[0]}?")
            except Exception as e:
                speak("Sorry, something went wrong.")

        # 🕒 Time
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {current_time}")

        # 📅 Date
        elif 'date' in query:
            today = datetime.date.today().strftime('%B %d, %Y')
            speak(f"Today is {today}")

        # 📺 YouTube
        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        # 🌍 Google
        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        # 🎵 Play song
        elif 'play song' in query or 'play' in query:
            song = query.replace("play song", "").replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        # 📧 Email
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "someone@example.com"
                send_email(to, content)
                speak("Email has been sent successfully.")
            except Exception as e:
                print("Email error:", e)
                speak("Sorry, I couldn't send the email.")

        # ☁️ Weather
        elif 'weather' in query:
            get_weather()

        # 🤖 Identity
        elif 'who are you' in query or 'what is your name' in query:
            speak("I am Jarvis, your personal AI assistant, created with Python to help you.")

        # 🛑 Exit
        elif 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Goodbye Sir. Shutting down.")
            break

        # ❓ Fallback
        else:
            print("Query received (unhandled):", query)
            speak("I'm sorry, I can't perform that action yet.")

# 🚀 Start
if __name__ == "__main__":
    run_assistant()
