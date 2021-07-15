import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morningggg!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoonnn!")
    else:
        speak("Good Eveninggg!")
    speak("Hello I am Zara!.How May I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        query = " "

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('keshavagarwal2602@gmail.com', 'ikurdikurdcc')
    server.sendmail(' agarwalji2608@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # speak("Keshav is a hot and handsome man")
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'play music' in query:
            music_dir = 'D:\\musics'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))

        elif 'time now' in query:
            nowTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir!The time is {nowTime}")
        elif 'open vscode' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'mail to keshav' in query:
            try:
                speak("Tell me what should i do")
                content = takeCommand()
                to = "keshavagarwal2602@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                speak("Sorry! I am not able to send email")

        elif 'keep quiet' in query:
            speak('You keep quiet')

        elif 'exit' in query:
            exit()
