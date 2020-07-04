# Importing Needed Modules.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio
import re

# Voice Property.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Starting.
input("\n   <<<!!!---Press ENTER to Start---!!!>>>\n")
print("\n   <!!! ONLINE !!!> \n")
print("\n   I am SARA! Your Digital Assistant.\n")
engine.say('Hello. I am Sara, Your Digital Assistant! Please Enter Your Name.')
engine.runAndWait()
name = str(input('Name:- '))
engine.say('Now! Your Favourite Work!')
engine.runAndWait()
favwork = str(input("Favourite Work:- "))
engine.say('Next! Your Email Address.')
engine.runAndWait()
emailadd = str(input('Email:- '))
engine.say("Make Sure That You Have Enabled Less Secured App Access In Your Gmail Account or You Won't Be Able To Send Emails through Gmail. Finally enter your Password")
engine.runAndWait()
print("\n   <<<---[[[Enable Less Secure App Access In Your Gmail]]]--->>>\n")
pword = input('Password:- ')

# Speaks The Name.
engine.say(f'Okay, So You are {name}')
engine.runAndWait()

# Comments About the Name.
if len(name) < 3:
    engine.say("Don't Mind, But the Name Is Too Short.")
elif len(name) > 20:
    engine.say("Don't Mind, But the Name Is Too Long.")
else:
    engine.say("Nice Name.")

# Bades With The Time.
hour = int(datetime.datetime.now().hour)
if hour>=3 and hour<6:
    engine.say(f'Good Day,{name}')
    engine.runAndWait()
elif hour>=6 and hour<12:
    engine.say(f'Good Morning,{name}')
    engine.runAndWait()
elif hour>=12 and hour<18:
    engine.say(f'Good Afternoon,{name}')
    engine.runAndWait()
else:
    engine.say(f'Good Evening,{name}')
    engine.runAndWait()
engine.say("Now, We are Ready to Go.")
engine.runAndWait()

# Speaks The Audio.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Hears The Voice.
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n   Listening...\n")
        speak("Listening")
        r.pause_threshold = 0.75
        audio = r.listen(source)
    try:
        print("   Recognizing...\n") 
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"{name} said:-  {query}\n")
    except Exception as e: 
        print("   Did Not Get It...\n")  
        return "None"
    return query

# Also Hears The Voice but Prints and Speaks Differnt Massages.
def takeCommandSt():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n   Say Something...\n")
        speak("Hearing!")
        r.pause_threshold = 0.75
        audio = r.listen(source)
    try:
        print("   Getting...\n") 
        speak("understanding")
        query = r.recognize_google(audio, language='en-in')
        print(f"{name} said:-  {query}\n")

    except Exception as e: 
        print("   Say that again please...\n")  
        return "None"
    return query

# Function Of Sending E-mail using Gmail.
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(emailadd, pword)
    server.sendmail(emailadd, to, content)
    server.close()

if __name__ == "__main__":

    # The Querys Which The User Can Ask.
    while True:
        query = takeCommandSt().lower()

        # Searches Wikipedia.
        if 'wiki' in query:
            try:
                speak('Searching Wikipedia')
                query = query.replace("sara wikipedia", "")
                wikiResults = wikipedia.summary(query, sentences=5)
                speak("According to Wikipedia,")
                print(f"   {wikiResults}\n")
                speak(wikiResults)
            except Exception as e:
                print(e)
                speak("Cannot Get Results!")

        # Tells The Time.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The Time Is {strTime}")
            speak(f"The Time Is {strTime}")

        # Plays Music Online.
        elif 'play ' in query:
            try:
                query = query.replace("play music", "")
                webbrowser.open(f'https://music.youtube.com/search?q={query}')
                speak("Okay! Checkout!")
            except Exception as e:
                speak(f'Sorry! Cannot {query}.')

        # Searches With Google.
        elif "search for" in query:
            speak("Fine! Searching Results")
            query = query.replace("search for", "")
            webbrowser.open(f'https://www.google.com/search?q={query}')
            speak("Checkout Search Results!")

        # Opens Any Website.
        elif "go to" in query:
            query = query.replace("go to", "")
            speak(f"Okay! Going to {query}")
            webbrowser.open(query)
            speak("Done!")

        # Fetches Youtube Results.
        elif "youtube" in query:
            speak("Okay! Fetching Results")
            query = query.replace("youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            speak("Checkout Youtube Results!")

        # Launches Any app on Your PC.
        elif 'launch an app' in query:
            try:
                speak("Which Application Should I Open?")
                app = takeCommand()
                os.startfile(app)
                speak(f"opening {app}")
            except Exception as e:
                speak(f"couldnot open Application called {app}")

        # Opens Folders In "C Drive".
        elif 'start' in query:
                os.system('explorer C:\\{}'.format(query.replace('launch ','')))
                desired = ("{}".format(query.replace('launch ','')))
                speak(f"Launching {desired}")

        # Sends E-mail with Gmail if Username & Password is Correct and Less Secured App Access Is Enabled.
        elif 'send email' in query:
            try:
                speak("Okay! Whom to Send?")
                to = input("Email To:- ")
                speak("Now Tell Me What to Say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Done! Email has been sent!")
            except Exception as e:
                speak("Something Went Wrong! Email Was Not Sent!")

        # Copies User's Command.
        elif 'say' in query:
            copy = query.replace("say", "")
            speak(copy)

        # Answers Your Hello.
        elif 'hello' in query:
            speak(f'HI {name}! How Can I Help You?')

        # Says It's Condition.
        elif 'how are you' in query:
            speak("I am Fine, Thank You for asking!")

        # Tells User's Identity.
        elif 'who am i' in query:
            speak(f"You Are {name}. Who Likes {favwork}")
            print(f"   Your Name Is {name} you Like {favwork} Your Email Address is {emailadd}.")

        # Tells It's Identity.
        elif 'who are you' in query:
            speak("I am Sara Your Voice Assistant Made By Sanglap in Python.")
            speak("plaese go and Checkout Sanglap!")
            print("   Sanglap's")
            print("     Email:- putatundasanglap@gmail.com")
            print("     Youtube:- http://bit.ly/2RvBuco   Subscribe! ")
            print("     Instagram:- http://bit.ly/32S2CoJ   Follow! \n")

        # Exit or Quit.
        elif 'exit' in query:
            speak(f"Thank You {name} For Giving Me Your Valueable Time, BYE! Have a Good Day!")
            print("   <!!! OFFLINE !!!>")
            exit()

        # Reacts If User Says Hey.
        elif "hey" in query:
            speak("Ready To Help You")

        # If She Is Called.
        elif 'sara' in query:
            speak("Ready For Your Command!")

        # If "Query Is None Of The Above"
        else:
            speak("Sorry! Didn't Get It!")
            print("   Did Not Get It...\n")
