# Importing Needed Modules.
import pyttsx3, speech_recognition as sr, datetime, wikipedia, webbrowser
import subprocess, wolframalpha, cv2, smtplib, pyaudio, re, os, random
import matplotlib.pyplot as plt
from PIL import ImageGrab

greeting_phrases = ["what's up ",'hi ','hello ','hey ',"What's going on "]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speaks The Audio.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Hears to the User.
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        speak('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...\n")
        speak('Recognizing')
        query = r.recognize_google(audio, language='en-us')
        print(f"{name} said: {query}\n")
    except:   
        print("Did Not Get It...\n")
        return "None"
    return query

# Bades With The Time.
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<6:
        speak(f'Good Day,{name}')
        print(f'\n\tGood Day, {name}\n')
    elif hour>=6 and hour<12:
        speak(f'Good Morning,{name}')
        print(f'\n\tGood Morning, {name}\n')
    elif hour>=12 and hour<18:
        speak(f'Good Afternoon,{name}')
        print(f'\n\tGood Afternoon, {name}\n')
    else:
        speak(f'Good Evening,{name}')
        print(f'\n\tGood Evening, {name}\n')

# Function Of Sending E-mail using Gmail.
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(emailadd, pword)
    server.sendmail(emailadd, to, content)
    server.close()

# Plays Music Offline.
def playMusic():
    try:
        music_dir = 'E:\\Music\\Songs'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
        speak('Playing Music!')
    except Exception as e:
        speak('Unable to Play Music From Your Device!')
        print('Error : ' + e)

# Organises Files In a Valid Directory.
def organiseFiles():
    try:
        speak("Enter a Valid Directory to Organise.")
        org_dir = input(r"\tDirectory:  ")
        all_files = os.listdir(org_dir)
        all_fext = []
        for f in all_files:
            _, fext = os.path.splitext(f)
            if fext not in all_fext:
                all_fext.append(fext)
        for ext in all_fext:
            if ext:
                os.mkdir(os.path.join(org_dir, ext))
        for f in all_files:
            _, ext = os.path.splitext(f)
            old_path = os.path.join(org_dir, f)
            new_path = os.path.join(org_dir, ext, f)
            os.rename(old_path, new_path)
        print(f"\n\tOrganised Files in {org_dir}")
        speak(f"Organised Files in {org_dir}")
    except Exception as e:
        speak(f"Something Went Wrong! Unable to Organise Files!")
        print('Error : ' + e)

# Grabs Photo Using Webcam.
def grabPhoto():
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
        else:
            ret = False
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        speak('Image Captured!')
        plt.imshow(img1)
        plt.title('Image Camera-1')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        cap.release()
    except Exception as e:
        print('Something Went Wrong!')
        print('Error : ' + e)
        speak('Unable to Grab Image!')

# User Details.
name = 'Sanglap'
emailadd = 'ahardlyunknown@gmail.com'
pword = 'Hardly_1234'

print("\n\t<!!! ONLINE !!!> \n")
speak(random.choice(greeting_phrases))
greet_user()
speak("How Can I Help You?")

if __name__ == "__main__":
    while True:
        query = input('\nType Something : ').lower() #takeCommand().lower()

        # Searches Wikipedia.
        if 'wiki' in query or 'wikipedia' in query:
            try:
                speak('Searching Wikipedia')
                query = query.replace("sara wikipedia ", "")
                wikiResults = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia,")
                print(f"\n\tAccording to Wikipedia:\t {wikiResults}\n")
                speak(wikiResults)
            except Exception as e:
                print(e)
                speak("Sorry! Cannot Get Results!")

        # Tells The Time.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"\tThe Time Is {strTime}")
            speak(f"The Time Is {strTime}")

        # Tells The Date.
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%m/%d/%y")
            print(f"\tToday's Date {strDate}")
            speak(f"The Date Is {strDate}")

        # Greets the User.
        elif 'greet' in query or 'wish me' in query:
            greet_user()

        # Grabs ScreenShot.
        elif 'screenshot' in query or 'screen shot' in query:
            speak("Grabbing Screenshot!")
            img = ImageGrab.grab()
            speak("Done! Showing Screenshot")
            img.show()

        # Grabs Photo Using WebCam.
        elif 'grab image' in query or ' grab photo' in query:
            grabPhoto()
                
        # Searches With Google.
        elif "search for" in query:
            query = query.replace("search for ", "")
            webbrowser.open(f'https://www.google.com/search?q={query}')
            speak("Checkout Search Results!")

        # Organises Files in a Specific Directory.
        elif "organise file" in query or  "manage file" in query:
            organiseFiles()
                
        # Opens Notepad.
        elif 'notepad' in query:
            speak('Opening Notepad')
            os.startfile('C:\\Windows\\system32\\notepad.exe')

        # Opens CMD.
        elif 'cmd' in query or 'command prompt' in query:
            speak('Opening Command Promt')
            os.startfile('C:\Windows\System32\cmd.exe')

        # Starts Calculator.
        elif 'calculator' in query:
            speak('Opening Calculator!')
            os.startfile('C:\Windows\System32\calc.exe')

        # Shows Connected Wifi Details.
        elif "wi-fi details" in query or 'wifi details' in query:
            try:
                speak("Trying to Show Details")
                print("\n\tTrying to Show Details...")
                subprocess.call('netsh wlan show profiles')
            except Exception as e:
                print("\n\tUnable to Show Details!")
                speak("Unable to ShoW Details! Sorry")

        # Shows IP Details
        elif 'ip details'in query or 'my ip' in query:
            speak("Showing Ip Details")
            subprocess.call("ipconfig")

        # Shows System Information in CMD.
        elif 'systeminfo' in query or 'system info' in query:
            speak("Ok! Showng Your System Information. Please Wait")
            print('\n')
            subprocess.call('systeminfo')
            speak('Done!')

        # Opens Any Website.
        elif "go to" in query:
            query = query.replace("go to ", "")
            speak(f"Going to {query}")
            webbrowser.open('http://'+ query)
            speak("Done!")

        # Copies User's Command.
        elif 'say' in query:
            copy = query.replace("say", "")
            speak(copy)

        # Plays Music.
        elif 'music' in query or 'song' in query:
            playMusic()

        # Fetches Youtube Results.
        elif "youtube" in query:
            speak("Ok! Fetching Results")
            query = query.replace("youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            speak("Checkout Youtube Results!")

        # Launches Any app on Your PC.
        elif 'launch' in query:
            query = query.replace('launch ', "")
            app = query.title()
            try:
                os.startfile(app)
                speak(f'Launching {app}!')
            except:
                speak(f"Couldn't Launch {app}")

        # Sends E-mail With Gmail if Username & Password is Correct and Less Secured App Access is Enabled.
        elif 'send email' in query or 'send an email' in query:
            try:
                speak("Ok! Whom to Send? Enter the Eamil-ID")
                to = input("Email To:- ")
                speak("Now Tell Me What to Say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Done! Email has been sent!")
            except Exception as e:
                speak("Something Went Wrong! the Email Was Not Sent!")
                print("Error : " + e)

        # Shuts Down the PC.
        elif 'shutdown' in query or 'power off' in query:
            speak('Ok! Shutting Down.')
            print("\n\tShutting Down")
            os.system('shutdown -s')

        # Answers Your Hello.
        elif 'hello' in query:
            speak(f'HI {name}! How Can I Help You?')

        # Says It's Condition.
        elif 'how are you' in query:
            speak("I am Fine, Thanks for Asking!")

        # Tells User's Identity.
        elif 'who am i' in query:
            speak(f"You Are {name}.")

        # Tells It's Identity.
        elif 'who are you' in query:
            speak("I am Sara, Your Voice Assistant.")

        # Exit or Quit.
        elif 'exit' in query or 'bye' in query:
            speak(f"Bye {name}! Have a Good Day!")
            print("\n\t<!!! OFFLINE !!!>")
            exit()

        # Reacts If User Says Hey.
        elif "hey" in query:
            speak("Ready To Help You")

        # Clears the Console.
        elif 'clear console' in query or 'clear terminal' in query:
            os.system('clear')
            speak('Current Console Cleared')

        # If "Query Is None Of The Above"
        else:
            try:
                try:
                    client  = wolframalpha.Client('9LXRT5-WHYX7PK8HX')
                    res = client.query(query)
                    output = next(res.results).text 
                    print(f'\n\tAnswer: {output}\n')
                    speak(output)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    print(f'\n\tWikipedia Says: {results}')
                    speak(f"Wikipedia Says {results}")
            except:
                google_url = 'https://www.google.com/search?q='
                webbrowser.open(google_url + query)
