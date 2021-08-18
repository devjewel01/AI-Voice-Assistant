from talk import custom_conversation
from talk import speak
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import os
import smtplib
import ctypes
import time
import shutil
import pyautogui
from urllib.request import urlopen

listener = sr.Recognizer()

numQuestion=len(custom_conversation['Question'])
numAnswer=len(custom_conversation['Answer'])

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            '''if 'open source' in command:
                command = command.replace('open source', '')
                print(command)'''

    except:
        pass
    return command

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    assname = "alexa"
    speak("I am your Assistant")
    speak(assname)

def usrname():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    clear()
    wishMe()
    usrname()
     
    while True:
         
        command = takeCommand().lower()
         

        check = False
        for i in range(1,numQuestion+1):
            try:
                if str(custom_conversation['Question'][i][0]).lower() in command:
                    speak(custom_conversation['Answer'][i])
                    check = True
                    break
            except Keyerror:
                speak('Please check if the number of questions matches the number of answers')

        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in command:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in command:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in command:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play music' in command or "play song" in command:
            speak("Here you go with music")
            music_dir = "C:\\Users\\GAURAV\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")
 
 
        elif 'send a mail' in command:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'exit' in command:
            speak("Thanks for giving me your time")
            exit()
      
        elif 'joke' in command:
            speak(pyjokes.get_joke())
 
        elif 'search' in command:    
            command = command.replace("search", "")
            webbrowser.open(command)
  
        elif 'lock window' in command:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in command:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif "don't listen" in command or "stop listening" in command:
            speak("for how much time you want to stop alexa from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
 
        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in command or "sleep" in command:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in command or "sign out" in command:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
            
        elif 'screenshot' in query:
            speak("And the file name would be...")
            name = takeCommand()
            pyautogui.screenshot(f"File_Location{name}.png")
            speak("The screenshot has been taken sir, check this out")
            os.startfile("File_Location")
             

 



