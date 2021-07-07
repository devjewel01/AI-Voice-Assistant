from talk import custom_conversation
from talk import talk
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()

numQuestion=len(custom_conversation['Question'])
numAnswer=len(custom_conversation['Answer'])

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'open source' in command:
                command = command.replace('open source', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    
    check = False
    for i in range(1,numQuestion+1):
        try:
            if str(custom_conversation['Question'][i][0]).lower() in command:
                talk(custom_conversation['Answer'][i])
                check = True
                break
        except Keyerror:
            say('Please check if the number of questions matches the number of answers')
    if check:
        return

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who  is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('I dont understand.  Please say the command again.')


while True:
    run_alexa()



