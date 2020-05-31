# Importing Needed Modules.
import pyttsx3, speech_recognition as sr, datetime, wikipedia, webbrowser
import subprocess, wolframalpha, cv2, smtplib, pyaudio, re, os, random
import matplotlib.pyplot as plt
from PIL import ImageGrab
from colored import fg, attr

# Color Properties.
reset = attr('reset')
green = fg('green')
red = fg('red')
blue = fg('blue')
yellow = fg('yellow')

greeting_phrases = ["What's Up! ",'Hi! ','Hello! ','Hey! ']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speaks The Audio.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Hears to the User.
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('\n*\n' + blue + "\n  Listening...\n" + reset)
        speak('Listening')
        r.adjust_for_ambient_noise = 0.75
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(green + "  Recognizing...\n" + reset)
        speak('Recognizing')
        query = r.recognize_google(audio, language='en-us')
        print(f"  {name} Said : {red} {query}\n" + reset)
    except:
        return "empty___query"
    return query

# Bades With The Time.
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<6:
        print(yellow + f'\n\tGood Day, {name}!' + reset)
        speak(f'Good Day,{name}')
    elif hour>=6 and hour<12:
        print(yellow + f'\n\tGood Morning, {name}!' + reset)
        speak(f'Good Morning,{name}')
    elif hour>=12 and hour<18:
        print(yellow + f'\n\tGood Afternoon, {name}!' + reset)
        speak(f'Good Afternoon,{name}')
    else:
        print(yellow + f'\n\tGood Evening, {name}!' + reset)
        speak(f'Good Evening,{name}')

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
        songNum = random.randint(0,159)
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[songNum]))
        print(green + '\n\tPlaying Music! ' + reset)
        speak('Playing Music!')
    except Exception as e:
        speak('Unable to Play Music From Your Device!')
        print(red + '\n\tUnable to Play Music!' + reset)

# Organises Files In a Valid Directory.
def organiseFiles():
    try:
        speak("Enter a Valid Directory to Organise.")
        print('\n')
        org_dir = input(green + r"        Directory:  " + reset)
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
        print(green + f"\n\tOrganised Files in {org_dir}" + reset)
        speak(f"Organised Files!")
    except Exception as e:
        print(red + '\n\tUnable to Organise Fles!' + reset)
        speak(f"Unable to Organise Files!")

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
        print(green + '\n\tDone!' + reset)
        plt.imshow(img1)
        plt.title('Image Camera-1')
        plt.xticks([])
        plt.yticks([])
        plt.show()
        cap.release()
    except Exception as e:
        print(red + '\n\tUnable to Grab Image!' + reset)
        speak('Unable to Grab Image!')

# User Details.
name = 'Sanglap'
bot = 'sara'
emailadd = 'ahardlyunknown@gmail.com'
pword = 'Hardly_1234'

os.system('cls')
print(green + "\n\t<!!! ONLINE !!!>" + reset)
speak(random.choice(greeting_phrases))
greet_user()
speak("How Can I Help You?")

if __name__ == "__main__":
    while True:

        #query = input(blue + '\n  Type Something : ' + reset).lower()
        query = command().lower()

        # Searches Wikipedia.
        if 'wiki' in query or 'wikipedia' in query:
            try:
                speak('Searching Wikipedia')
                query = query.replace("sara wikipedia ", "")
                wikiResults = wikipedia.summary(query, sentences=2)
                print(green + f"\n\tAccording to Wikipedia:{yellow}\t {wikiResults}" + reset)
                speak('According to Wikipedia: '+ wikiResults)
            except Exception as e:
                print(red + '\n\tUnable to Get Results!' + reset)
                speak("Sorry, Cannot Get Results!")

        # Tells The Time.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(yellow + f"\n\tThe Time Is {strTime}" + reset)
            speak(f"The Time Is {strTime}")

        # Tells The Date.
        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%m/%d/%y")
            print(yellow + f"\n\tToday's Date: {strDate}" + reset)
            speak(f"The Date Is {strDate}")

        # Greets the User.
        elif 'greet me' in query or 'wish me' in query:
            greet_user()

        # Grabs Photo Using WebCam.
        elif 'grab image' in query or ' grab photo' in query:
            grabPhoto()
        
        # Plays Music.
        elif 'play music' in query or 'play song' in query:
            playMusic()

        # Grabs ScreenShot.
        elif 'screenshot' in query or 'screen shot' in query:
            speak("Grabbing Screenshot!")
            print(yellow + '\n\tDone!' + reset)
            img = ImageGrab.grab()
            speak("Done!")
            img.show()

        # Sends E-mail With G-Mail.
        elif 'send email' in query or 'an email' in query:
            try:
                speak("Ok! Whom to Send? Enter the E-mail ID")
                to = input(green + "\n\tEmail To : " + reset)
                speak("Now Tell Me What to Say?")
                content = command().title()
                #content = input(green + '\n\tContent: ' + reset)
                sendEmail(to, content)
                print(green + '\n\tE-mail Has Been Sent!' + reset)
                speak("Done! Email has been sent!")
            except Exception as e:
                print(red + '\n\tThe E-mail Was Not Sent!' + reset)
                speak("Something Went Wrong! the Email Was Not Sent!")

        # Opens Any Website.
        elif '.com' in query or '.org' in query or '.net' in query or '.io' in query:
            query = query.replace('open ', '')
            query = query.replace('start ', '')
            query = query.replace('launch ', '')
            print(green + '\n\tOpening ' + query + reset)
            speak(f"Opening {query}!")
            webbrowser.open('http://'+ query)

        # Searches With Google.
        elif "search" in query or 'google' in query:
            query = query.replace("search", "")
            query = query.replace('google', '')
            webbrowser.open(f'https://www.google.com/search?q={query}')
            print(yellow + f'\n\tSearching for, {query}' + reset)
            speak("Checkout Search Results!")

        # Fetches Youtube Results.
        elif "youtube" in query:
            speak("Ok! Fetching Results")
            query = query.replace("youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            print(yellow + '\n\tCheckout YouTube Results!' + reset)
            speak("Checkout Youtube Results!")

        # Organises Files in a Specific Directory.
        elif "organise file" in query or  "manage file" in query:
            organiseFiles()
                
        # Opens Notepad.
        elif 'open notepad' in query:
            print(yellow + '\n\tOpening NOTEPAD!' + reset)
            speak('Opening Notepad')
            os.startfile('C:\\Windows\\system32\\notepad.exe')

        # Opens CMD.
        elif 'open cmd' in query or 'command prompt' in query:
            print(yellow + '\n\tOpening COMMAND PROMPT!' + reset)
            speak('Opening Command Promt')
            os.startfile('C:\Windows\System32\cmd.exe')

        # Starts Calculator.
        elif 'open calculator' in query:
            print(yellow + '\n\tOpening CALCULATOR' + reset)
            speak('Opening Calculator!')
            os.startfile('C:\Windows\System32\calc.exe')

        # Launches Any app on Your PC.
        elif 'launch' in query:
            query = query.replace('launch ', "")
            app = query.title()
            try:
                os.startfile(app)
                print(green + '\n\tLaunching ' + app.upper() + reset)
                speak(f'Launching {app}!')
            except:
                speak(f"Couldn't Launch {app}")
                print(red + f"\n\tCouldn't Launch {app}!" + reset)

        # Shows Connected Wifi Details.
        elif "wi-fi details" in query or 'wifi details' in query:
            try:
                speak("Trying to Show Details")
                print(yellow + "\n\tTrying Show Details..." + reset)
                subprocess.call('netsh wlan show profiles')
            except Exception as e:
                print(red + "\n\tUnable to Show Details!" + reset)
                speak("Unable to ShoW Details! Sorry")

        # Shows IP Details
        elif 'ip details'in query or 'my ip' in query:
            print(yellow + '\n\nShowing!' + reset)
            speak("Showing Ip Details")
            subprocess.call("ipconfig")

        # Shows System Information in CMD.
        elif 'systeminfo' in query or 'system info' in query:
            speak("Ok! Showng Your System Information. Please Wait")
            print(yellow + '\n\tShowing System Information!' + reset)
            subprocess.call('systeminfo')
            speak('Done!')

        # Clears the Console.
        elif 'clear console' in query or 'clear terminal' in query:
            os.system('cls')
            speak('Current Console Cleared')

        # Shuts Down the PC.
        elif 'shutdown' in query or 'power off' in query:
            speak('Ok! Shutting Down. Bye')
            print(yellow + '\n\tShutting Down! Bye.' + reset)
            os.system('shutdown -s')
            print(red + "\n\t<!!! OFFLINE !!!>" + reset)
            exit()

        # Answers Your Hello.
        elif f'hello' in query or f'hi {bot}' in query:
            hello_ans = [
                f'Hi {name}',
                f'Hey {name}',
                f'Hello {name}',
                f'Hi There {name}',
                f'Hey There {name}',
                f'Hello There {name}'
            ]
            hello_ans = random.choice(hello_ans)
            print(yellow + f'\n\t{hello_ans}! How Can I Help You?' + reset)
            speak(f'{hello_ans}! How Can I Help You?')

        # Reacts If User Says Hey.
        elif f"hey {bot}" in query:
            hey_ans = [
                'Ready to Help You!',
                'How Can I Help You?',
                'I am Here to Help You!'
            ]
            hey_ans = random.choice(hey_ans)
            print(yellow + f'\n\t{hey_ans}' + reset)
            speak(hey_ans)

        # Says It's Condition.
        elif 'how are you' in query:
            as_i_am = [
                'I am Fine,',
                'I am Doing Well,',
                'I am Great,'
            ]
            as_i_am = random.choice(as_i_am)
            print(yellow + f'\n\t{as_i_am} Thanks For Asking!' + reset)
            speak(as_i_am + ' Thanks For Asking!')

        # Tells User's Identity.
        elif 'who am i' in query:
            print(yellow + f'\n\tYou are {name}.' + reset)
            speak(f"You Are {name}.")

        # Tells Her Name
        elif 'what is your name' in query:
            print(yellow + f'\n\t My Name is {bot.title()}.' + reset)
            speak(f'I am {bot}')

        # Tells It's Identity.
        elif 'who are you' in query:
            print(yellow + f'\n\tI am {bot.title()}, Your Virtual Assistant!' + reset)
            speak(f"I am {bot}, Your Virtual Assistant.")

        # Copies User's Command.
        elif 'say' in query:
            copy = query.replace("say", "")
            speak(copy)

        # Exit or Quit.
        elif 'exit' in query or f'bye' in query:
            hour = int(datetime.datetime.now().hour)
            if hour>=3 and hour<18:
                print(yellow + f'\n\tBye {name}, Have a Good Day!' + reset)
                speak(f'Bye {name}, Have a Good Day!')
            else:
                print(yellow + f'\n\tBye {name}, Have a Good Night!' + reset)
                speak(f'Bye {name}, Have a Good Night!')
            print(red + "\n\t<!!! OFFLINE !!!>" + reset)
            exit()

        # Invaild Query.
        elif 'empty___query' in query:
            print(red + "  Did Not Get It...\n" + reset)
            speak('Did not Get it!')

        # If "Query Is None Of The Above"
        else:
            try:
                try:
                    client  = wolframalpha.Client('9LXRT5-WHYX7PK8HX')
                    res = client.query(query)
                    output = next(res.results).text 
                    print(green + f'\n\tAnswer: {yellow} {output}' + reset)
                    speak(output)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    print(green + f'\n\tWikipedia Says: {yellow} {results}' + reset)
                    speak(f"Wikipedia Says {results}")
            except:
                print(red + "\n\tI Don't Know How to Reply This!" + reset)
                speak("I Don't Know, How to Reply This!")
