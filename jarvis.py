import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Mam, I am jarvis. Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')    
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tiwarishreya022002@gmail.com', 'shreya#1234')
    server.sendmail('tiwarishreya022002@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
     query = takeCommand().lower()


     if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("Wikipedia", "")
         results = wikipedia.summary(query, sentences=2)
         speak("According to Wikipedia")
         speak(results)


     elif 'open youtube'in query:  
         webbrowser.open("youtube.com")   

     elif 'open google'in query:  
         webbrowser.open("google.com")  

     elif 'open stackoverflow'in query:  
         webbrowser.open("stackoverflow.com")     

     elif 'play music' in query:
         music_dir = 'C:\\Users\\tiwar\\Desktop\\Favourites'
         songs = os.listdir(music_dir)
         os.startfile(os.path.join(music_dir, random.choice(songs)))

     elif 'play videos' in query:
         video_dir = 'C:\\Users\\tiwar\\videos' 
         videos = os.listdir(video_dir)
         os.startfile(os.path.join(video_dir, videos[0]))  
   

     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Mam, the time is {strTime}")  

     elif 'open code' in query:
         codePath = "C:\\Users\\tiwar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)  


     elif 'send email to vaishnavi' in query:
         try:
             speak("What should I say?")
             content = takeCommand()
             to = "vaishnaviu1224@gmail.com"
             sendEmail(to, content)
             speak("Email has been sent!")
         except Exception as e:
             print(e)
             speak("Sorry mam. I am not able to send this email.")    

     elif 'shut the program' in query:
         os._exit(os.EX_OK)              






