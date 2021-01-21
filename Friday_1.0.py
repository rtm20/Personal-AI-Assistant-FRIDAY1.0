import pyttsx3                      #for audio output
import datetime
import speech_recognition as sr
import wikipedia                    #wikipedia query searching 
import smtplib                      #for email purpose
import webbrowser as wb             #for searching query in chrome.
import psutil                       #for CPU & Battery status of your laptop
import pyjokes                      #for getting jokes
import os                           #for opening computer applications
import pyautogui                    #pip install pyautogui (For Screenshot)
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha                 # for calculation purpose
import time
import winshell

engine = pyttsx3.init()

# Background


# MAIN CODE START!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 165)     # setting up new voice rate

engine.setProperty('volume',1.0)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Introduction():
    speak("I am FRIDAY 1.0 , The Personal AI assistant , "
    "I am created by Mr Ritesh Meena , "
    "I can help you in various regards , "
    "I can search for you on the Internet , "
    "I can also grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you , ")

def Creator():
    speak(".......Mr Ritesh Meena is an extra-ordinary person."
    "...........He has a passion for Artificial Intelligence and Machine Learning."
    "......He is very co-operative.")

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S") #for 12 hrs format and (use %H for 24 hrs format)
    speak('the current time is')
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back BOSS")
    time_()
    date_()

    #greetings

    '''hours=datetime.datetime.now().hour

    if hours>=6 and hours<12:
        speak('Good morning Sir!')
    elif hours>=12 and hours<18:
        speak('Good afternoon sir!')
    elif hours>=18 and hours<24:
        speak('good evening sir!')
    else:
        speak('Good night sir!')'''

    speak('FRIDAY at your help sir. Ask me anything!!')    

#wishme()

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak('Im listening....')
        print("Listening........")
        r.pause_threshold = 0.6
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Say that again please.....")
        speak('Sir Say that again please.....')
        return "None"

    return query

#TakeCommand()
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)               #587 is the port for gmail services
    server.ehlo()  #help to identify ourself to ESMTP server
    server.starttls()  #to start server in ESMTP mode

    #for this function to work, enable low security in your gmail which you use as sender!!

    server.login('riteshbrainer99@gmail.com','Ritesh@2099')
    server.sendmail('riteshbrainer99@gmail.com',to,content)
    server.close()


def cpu():
    usage= str(psutil.cpu_percent())
    speak('CPU usage is'+ usage+'percent')

    batt=psutil.sensors_battery()
    speak('Your laptops battery is.....')
    speak(batt.percent) 
    speak('percent')
    

def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/Asus/Desktop/JARVIS/Screenshots/pic.jpg')



if __name__ == "__main__":

    clear = lambda: os.system('cls') 
	
	# This Function will clean any 
	# command before execution of this python file
    clear()

    wishme()
    while True:
        query =  TakeCommand().lower()

        #all the commands are stored in lowercase in the variable query
        #for easy recognition 

        if 'time' in query: #tell us time
            time_()
            speak('anything else boss???')
        elif 'date' in query: #tell us date
            date_()
            speak('anything else boss???')
            
        elif 'wikipedia' in query:

            speak('searching....')
            query=query.replace('wikipedia', ' ')
            speak('According to wikipedia')
            #query=query.replace('what is', ' ')
            result=wikipedia.summary(query,sentences=4)
            
            print(result)
            speak('According to wikipedia')
            speak(result)
            speak('anything else boss???')

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content=TakeCommand()

                #provide recierver email address
                speak('Who is the reciever?')
                reciever=input("Enter Recievers Email address. ")
                to=reciever
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent.')
                speak('anything else boss???')
            
            except Exception as e:
                print(e)
                speak('Unable to send the mail')
                speak('anything else boss???')

        elif 'open in chrome' in query:
            speak('what should i search Sir')
            chromepath='C:\Program Files (x86)\Google\Chrome\Application\chrome.exe  %s'

            search=TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

            speak('anything else boss???')

        elif 'search on youtube' in query or 'open youtube' in query:
            speak('what should i search Sir')
            search_term=TakeCommand().lower()

            speak('Here we go to YOUTUBE!')
            wb.open('https://www.youtube.com/results?search_query='+search_term)

            speak('anything else boss???')
        
        elif 'search online' in query or'seach in google' in query or 'google search' in query:
            speak('what should i search Sir')
            search_term=TakeCommand().lower()

            speak('Here we go to Google!')
            wb.open('https://www.google.com/search?q='+search_term)

            speak('anything else boss???')

        elif 'cpu' in query:
            cpu()
            speak('anything else boss???')

        elif 'joke' and 'jokes' in query:
            jokes()
            

            speak('anything else boss???')


        elif 'word' in query:
            speak('Opening MS WORD Sir')
            ms_word=r'C:\Program Files\Microsoft Office\Office16\WINWORD.exe'
            os.startfile(ms_word)

            speak('anything else boss???')

        elif "write a note" in query:
            speak("What should i write, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
                speak('anything else boss???')
            else:
                file.write(note)
                speak('anything else boss???')
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read())

            speak('anything else boss???')

        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")

            speak('anything else boss???')

        elif 'play songs' in query:
            video ='songs path'
            audio = 'Songs path'
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                       #used while loop to keep the jarvis on the speak command untill req. command is given.
                speak("I could not understand you. Please Try again.")          #first used 'rand' before while then again after, so that rand is already defind, and Input is taken and then checked if it is according to reuirement or not. And if it is not which means while loop is true, then commands under 'while loop' will execute untill desired approach.As it will again ask the user for input in the same block. 
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                    #'continue' is used, so that after executing the commands in 'if' or 'elif' block, it will move to the next part of execution (or code). but in this case as this is the last execution of related function then it will move to the next function (i.e. in this code, it will be TakeCommand() )
            elif 'random' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
         
         
        elif 'remember that' in query:
             
             speak("What should I remember ?")
             memory = TakeCommand()
             speak("You asked me to remember that"+memory)
             remember = open('memory.txt','w')
             remember.write(memory)
             remember.close()

             speak('anything else boss???')

        elif 'do you remember anything' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())   

            speak('anything else boss???')   

        elif 'news' in query:
            try:

                jsonObj = urlopen('http://newsapi.org/v2/top-headlines?country=in&apiKey=06397090fb38471e82e0efbb3f874cac')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are the top 3 news from the Times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    if i<3:
                        i += 1
                    else:
                        quit()

                speak('anything else boss???')

                    
                    
            except Exception as e:
                print(str(e)) 

         #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

            speak('anything else boss???')

        #calculation
        elif "calculate" in query:
            
            app_id = "UWRRWQ-KUHQRAXQKL"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

            speak('anything else boss???')
        
            #General Questions
   
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much seconds you want me to stop listening commands (just say the number..)")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        #General irrelevent questions for JARVIS!!! (just for FUN)
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")
            speak('anything else boss???')

        elif 'who is your creator' in query or 'who created you' in query:
            Creator()
            speak('anything else boss???')

        elif 'why you came to this world' in query:
            speak("Thanks to Ritesh Sir. further it is a secret")
            speak('anything else boss???')

        elif 'introduce yourself' in query or 'introduction' in query:
            Introduction()
            speak('anything else boss???')

        elif 'what is love' in query or 'tell me about love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is waste of time but at the same point it is a neccesary part of human life.")

            speak('anything else boss???')

        #clear recycle bin 

        elif 'empty recycle bin' in query or 'empty my recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled") 

            speak('anything else boss???')

        elif 'no thanks' in query or 'go offline' in query:
            speak('going offline!! happy to help sir.')
            quit()

        


        