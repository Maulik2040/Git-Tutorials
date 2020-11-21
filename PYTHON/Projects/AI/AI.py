import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speech(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speech("Good Morning!")

    elif hour>=12 and hour <18:
        speech("Good Afternoon!")

    else:
        speech("Good Evening!")

    speech("I am Jarvis sir. Tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query




if __name__ == "__main__":
    wishme()  
    while 1:
    
        # quit = False
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speech("Searching Wikipedia")
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speech("According to Wikipedia")
            print(results)
            speech(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("chrome/google.com")
         
        elif 'open stackoverflow' in query:

            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speech(f"Sir, The time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\Omprakash\\AppData\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        

        elif 'open word' in query:
            a = "C:\\Program Files (x86)\\Microsoft Office\\root\Office16\\WINWORD.EXE"
            os.startfile(a)

        elif 'open skype' in query:
            b = "C:\\Program Files (x86)\Microsoft Office\\root\\Office16\\lync.exe" 
            os.startfile(b)
        
        elif 'open excel' in query:
            c = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(c)

        

        elif 'what is your name' in query:
            speech("My name is Jarvis")

        elif 'what is my name' in query:
            speech("your name is Maulik")

        pyautogui.keyDown(query)