import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!") 

    speak("I am you assisstant sir. Please tell me how may I help you")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password') #you can enter your gmail details here
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    greetings()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("I have opened youtube sir.")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("I have opened google sir.")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("I have opened stackoverflow sir.") 


        elif 'play music' in query:
            music_dir = 'Downloads\Official Music Video  VALORANT Champions 2021.mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "D:\pycharm\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'email to maheshwar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "maheshwar.sathyabama@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")   
        elif 'open game' in query:
            codePath = "D:\Valorant\Riot Games\Riot Client\RiotClientServices.exe" #enter your favorite game file location
            os.startfile(codePath)
            speak("As you wish sir, I have opened riot client!") 
        
        elif 'gold rate' in query:
            webbrowser.open("https://www.goodreturns.in/gold-rates/chennai.html")
            speak("Here is the current gold rate sir")
        else:
            speak("I apologize sir, but I couldn't understand your message ")