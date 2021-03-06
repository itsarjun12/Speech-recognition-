import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("good Evening!")

    speak("I am your assitent sir . please tell me arjun gaud how may i help you ")   
    
    

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
        print("say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    wishme()
    takeCommand()

        
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
       
    server.close()
    
if __name__ == "__main__":
    wishMe()
    
    while True:
       
        query = takeCommand().lower()
    
           
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
          
            print(results)
            speak(results)
    
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
    
        elif 'open google' in query:
            webbrowser.open("google.com")
    
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
    
    
        elif 'play music' in query:
            music_dir = 'D:\\fav songs'
            
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
    
        elif 'the time' in query:
            
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            
            speak(f"Sir, the time is {strTime}")
    
        elif 'email to Arjun' in query:
    
            try:
    
                speak("What should I say?")
    
                content = takeCommand()
    
                to = "arjun20111996@gmail.com"    
    
                sendEmail(to, content)
    
                speak("Email has been sent!")
    
            except Exception as e:
    
                print(e)
    
                speak("Sorry my friend harry bhai. I am not able to send this email")     
        



