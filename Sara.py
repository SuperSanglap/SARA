# Reommended & Used Python Version 3.6.0
# Before Running the Program Please Read the Readme.txt File

# Importing Needed Modules.
import pyttsx3, speech_recognition as sr, datetime, wikipedia, webbrowser
import subprocess, wolframalpha, cv2, smtplib, pyaudio, re, os, random, time
import sounddevice, matplotlib.pyplot as plt, socket
from PIL import ImageGrab
from colored import fg, attr
from googletrans import Translator
from getpass import getpass
from scipy.io.wavfile import write

# Color Properties.
reset = attr('reset') # Resets the Text Color to Default.
red = fg('red')       # Prints Text With Red Color.
blue = fg('blue')     # Prints Text With Blue Color.
green = fg('green')   # Prints Text With Green Color.
yellow = fg('yellow') # Prints Text With Yellow Color.

greeting_phrases = ["What's Up! ",'Hi! ','Hello! ','Hey! ']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
currentVoice = engine.setProperty('voice', voices[1].id)

# Speaks The Audio.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Hears to the User.
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(reset + '\n*\n' + blue + "\n  Listening...\n" + reset)
        speak('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        connectionCheck()
    try:
        print(green + "  Recognizing...\n" + reset)
        speak('Recognizing')
        query = r.recognize_google(audio)
        print(f"  {name.title()} {red}> {blue} {query}\n" + reset)
    except:
        return "©empty_^_^_queryª"
    return query

# Bades With The Time.
def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour>=22 and hour<5:
        print(yellow + f'\n\tGood Night, {name.title()}!' + reset)
        speak(f'Good Night,{name}')
    elif hour>=5 and hour<12:
        print(yellow + f'\n\tGood Morning, {name.title()}!' + reset)
        speak(f'Good Morning,{name}')
    elif hour>=12 and hour<18:
        print(yellow + f'\n\tGood Afternoon, {name.title()}!' + reset)
        speak(f'Good Afternoon,{name}')
    else:
        print(yellow + f'\n\tGood Evening, {name.title()}!' + reset)
        speak(f'Good Evening,{name}')

# Function of Sending E-mail Using Gmail.
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(emailadd, pword)
    server.sendmail(emailadd, to, content)
    server.close()

#Checks Internet Connection.
def connectionCheck():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.google.com', 80))
        s.close()
    except Exception:
        print(red + '\n\tUnable to Connect!' + reset)
        speak('Unable to Connect!')
        quitApp()

# Quits App.
def quitApp():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<18:
        print(yellow + f'\n\tBye {name.title()}, Have a Good Day!' + reset)
        speak(f'Bye {name}, Have a Good Day!')
    else:
        print(yellow + f'\n\tBye {name.title()}, Good Night!' + reset)
        speak(f'Bye {name}, Good Night!')
    print(red + "\n\t<!!! OFFLINE !!!>" + reset)
    exit(0)    

# ShutDown Function.
def shutdown():
    print(yellow + '\n\tAre You Sure?' + reset)
    speak('Are You Sure?')
    reply = command().lower()
    if "yes" in reply or 'ok' in reply or 'yup' in reply or 'do' in reply:
        print(yellow + '\n\tShutting Down!.' + reset)
        speak('Ok! Shutting Down in a Minute.')
        os.system('shutdown -s')
        quitApp()
    else:
        print(red + "\n\tOkay! Don't Worry." + reset)
        speak("Okay! Don't Worry")

# Plays Music Offline.
def playMusic():
    try:
        music_dir = 'E:\\Music\\Songs'
        songNum = random.randint(0,163)
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[songNum]))
        print(green + '\n\tPlaying Music! ' + reset)
        speak('Playing Music!')
        sleep()
    except Exception as e:
        speak('Unable to Play Music From Your Device!')
        print(red + '\n\tUnable to Play Music!' + reset)

# Changes User's Password.
def changePassword():
        pword = getpass(green + '\n\tEnter New Password : '+ reset)
        print(yellow + '\n\tPassword Updated Successfully!' + reset)
        speak('Password Updated Successfully.')
        print(yellow + "\n\tShould I Show It?" + reset)
        speak("Should I Show It?")
        reply = command().lower()
        if "yes" in reply or 'ok' in reply or 'show' in reply or 'do' in reply:
            print(yellow + '\n\tShowing Password!' + reset)
            speak('Okay! Showing!')
            print(yellow + f'\n\tPassword: {blue}"{pword}"' + reset)
        else:
            print(red + "\n\tOkay, Nevermind!" + reset)
            speak("Okay, Nevermind!")

# User Details.
name = 'Sanglap'.lower() # User's Name
bot = 'Sara'.lower() # Voice Assistant's Name
wakeWord = 'Ok'.lower() # Wake Word For the Virtual Assistant
emailadd = 'putatundasanglap@gmail.com' # User's E-Mail ID
pword = '©empty_^_^_pwordª' # Constant Password(Must Not Be Changed)

os.system('cls')
print(green + "\n\t<!!! ONLINE !!!>" + reset)
connectionCheck()
speak(random.choice(greeting_phrases))
greet_user()
speak("How Can I Help You?")

if __name__ == "__main__":
    while True:
        query = command().lower()

        # Searches Wikipedia.
        if 'wiki' in query or 'wikipedia' in query:
            try:
                speak('Searching Wikipedia')
                query = query.replace("wikipedia", "")
                query = query.replace("wiki", "")
                wikiResults = wikipedia.summary(query, sentences=5)
                print(green + f"\n\tAccording to Wikipedia:{yellow}\t {wikiResults}" + reset)
                speak('According to Wikipedia: '+ wikiResults)
            except Exception as e:
                print(red + '\n\tUnable to Get Results!' + reset)
                speak("Couldn't Get Results!")

        # Opens Any Website.
        elif '.' in query:
            query = query.replace('open ', '')
            print(yellow + '\n\tOpening ' + query + reset)
            speak(f"Opening {query}!")
            webbrowser.open('http://'+ query)
            sleep()

        # Searches With Google.
        elif "search" in query or 'google' in query:
            query = query.replace("search", "")
            query = query.replace(" for ", "")
            query = query.replace(' google', '')
            query = query.replace('google ', '')
            webbrowser.open(f'https://www.google.com/search?q={query}')
            print(yellow + f'\n\tSearching For "{query.title()}"' + reset)
            speak(f"Searching for {query}")
            sleep()

        # Fetches Youtube Results.
        elif "youtube" in query:
            speak("Ok! Fetching Results")
            query = query.replace("youtube ", "")
            query = query.replace(" youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            print(yellow + '\n\tCheckout YouTube Results!' + reset)
            speak("Checkout Youtube Results!")
            sleep()

        # Copies User's Command.
        elif 'say ' in query or 'speak' in query:
            copy = query.replace("say ", "")
            print(yellow + f'\n\t{copy.title()}' + reset)
            speak(copy)
            time.sleep(1)

        # Tells The Time.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(yellow + f"\n\tIt is {strTime}" + reset)
            speak(f"It's {strTime}")
            time.sleep(1)

        # Tells The Date.
        elif 'the date' in query or "today's date" in query:
            strDate = datetime.datetime.now().strftime("%m/%d/%y")
            print(yellow + f"\n\tToday is {strDate}" + reset)
            speak(f"Today is, {strDate}")
            time.sleep(1)

        # Greets the User.
        elif 'greet me' in query or 'wish me' in query:
            greet_user()

        # Greets User When User Greets.
        elif 'good morning'in query or 'good afternoon' in query or'good evening'in query:
            greet_user()

        # Plays Music.
        elif 'play music' in query or 'play song' in query or 'change music' in query:
            playMusic()

        # Plays Any Music Online.
        elif 'play ' in query:
            query = query.replace('play ', '')
            musicSearch = f'https://music.youtube.com/search?q={query}'
            print(yellow + f"\n\tPlaying {query} Online." + reset)
            speak(f'Playing {query} Online!')
            webbrowser.open(musicSearch)
            sleep()

        # Sends E-mail With G-Mail.
        elif 'send email' in query or 'send an email' in query:
            try:
                if pword == '©empty_^_^_pwordª':
                    speak('Atfirst Enter Your Password!')
                    pword = getpass(green + '\n\tEnter Your Password : '+ reset)
                    speak("Ok! Whom to Send? Enter the E-mail ID")
                else:
                    speak("Ok! Whom to Send? Enter the E-mail ID")
                to = input(green + "\n\tEmail To : " + reset)
                speak("What Should I Say?")
                print(yellow +'\n\tWhat Should I Say?' + reset)
                content = command().title()
                sendEmail(to, content)
                print(green + '\n\tE-mail Has Been Sent!' + reset)
                speak("Done! Email has been sent!")
            except Exception as e:
                print(red + '\n\tThe E-mail Was Not Sent!' + reset)
                speak("Something Went Wrong! the Email Was Not Sent!")

        # Changes Listed Password.
        elif 'change password' in query or 'change my password' in query:
            speak('Enter New Password!')
            changePassword()

        # Shows User's Password
        elif 'my password' in query or 'show password' in query:
            if pword == '©empty_^_^_pwordª':
                print(yellow + "\n\tYou Don't Have a Password! Enter One." + reset)
                speak("You Don't Have a Password! Enter One.")
                changePassword()
            else:
                print(yellow + 'Showing Password!' + reset)
                speak('Okay! Showing!')
                print(yellow + f'Password: \n\t"{blue}{pword}"' + reset)

        # Launches Any app on Your PC.
        elif 'launch' in query:
            query = query.replace('launch ', "")
            app = query.title()
            try:
                os.startfile(app)
                print(yellow + '\n\tLaunching ' + app.title() + reset)
                speak(f'Launching {app}!')
                sleep()
            except:
                print(red + f"\n\tCouldn't Launch {app.title()}!Should I Search Online ?" + reset)
                speak(f"Couldn't Launch {app}, Should I Search Online?")
                reply = command().lower()
                if "yes" in reply or 'ok' in reply or 'yup' in reply or 'do' in reply:
                    print(yellow + f'\n\tSearching Online for {app}')
                    speak('Fine, Searching Online!')
                else:
                    print(yellow + "\n\tOkay! Don't Worry" + reset)
                    speak("Okay, Don't Worry")
   
        # Opens Notepad.
        elif 'open notepad' in query:
            print(yellow + '\n\tOpening NOTEPAD!' + reset)
            speak('Opening Notepad')
            os.startfile('C:\\Windows\\system32\\notepad.exe')
            sleep()

        # Opens Task Manager.
        elif 'task manager' in query or 'task-manager' in query:
            print(yellow + '\n\tOpening Task Manager!' + reset)
            speak('Opening Task Manager')
            os.startfile('C:\\Windows\\system32\\Taskmgr.exe')
            sleep()

        # Opens CMD.
        elif 'cmd' in query or 'command prompt' in query:
            print(yellow + '\n\tOpening COMMAND PROMPT!' + reset)
            speak('Opening Command Promt')
            os.startfile('C:\Windows\System32\cmd.exe')
            sleep()

        # Starts Calculator.
        elif 'open calculator' in query:
            print(yellow + '\n\tOpening CALCULATOR' + reset)
            speak('Opening Calculator!')
            os.startfile('C:\Windows\System32\calc.exe')
            sleep()

        # Shows Connected Wifi Details.
        elif "wi-fi details" in query or 'wifi details' in query:
            try:
                speak("Trying to Show Details")
                print(green + "\n\tTrying Show Details..." + yellow)
                subprocess.call('netsh wlan show profiles')
                time.sleep(3)
            except Exception as e:
                print(red + "\n\tUnable to Show Details!" + reset)
                speak("Unable to ShoW Details! Sorry")

        # Shows IP Details
        elif 'ip details'in query or 'my ip' in query:
            print(green + '\n\tShowing!' + yellow)
            speak("Showing Ip Details")
            subprocess.call("ipconfig")
            time.sleep(2)

        # Shows System Information in CMD.
        elif 'systeminfo' in query or 'system info' in query:
            print(green + '\n\tShowing System Information!\n' + yellow)
            speak("Ok, Showng Your System Information. Please Wait")
            subprocess.call('systeminfo')
            speak('Done!')
            time.sleep(5)

        # Shows All Running Tasks.
        elif 'task list' in query or 'tasklist' in query:
            print(green + '\n\tShowing All Running Tasks!' + yellow)
            speak('Showing All Running Tasks!')
            subprocess.call('tasklist')
            time.sleep(10)

        # Clears the Console.
        elif 'clear' == query or 'clean' == query or 'clear console' in query:
            os.system('cls')
            speak('Current Console Cleared')
            sleep()

        # Shuts Down the PC.
        elif 'shutdown' in query or 'power off' in query:
            shutdown()

        # Answers Your Hello.
        elif f'hello' in query or f'hi {bot}' in query:
            hello_ans = [
                f'Hi {name.title()}!',
                f'Hey {name.title()}!',
                f'Hello {name.title()}!',
                f'Hi There {name.title()}!',
                f'Hey There {name.title()}!',
                f'Hello There {name.title()}!'
            ]
            hello_ans = random.choice(hello_ans)
            print(yellow + f'\n\t{hello_ans}! How Can I Help You?' + reset)
            speak(f'{hello_ans}! How Can I Help You?')

        # If Only It's Name in Query.
        elif bot == query:
            toReply = [
                'Ready to Help You!',
                'How Can I Help You?',
                'I am Here'
            ]
            toReply = random.choice(toReply)
            print(yellow + f"\n\t{toReply}" + reset)
            speak(toReply)

        # Reacts If User Says Hey.
        elif "hey" in query or "hi" == query:
            hey_ans = [
                'Ready to Help You!',
                'How Can I Help You?',
                'I am Here to Help You!'
            ]
            hey_ans = random.choice(hey_ans)
            print(yellow + f'\n\t{hey_ans}' + reset)
            speak(hey_ans)

        # Says It's Condition.
        elif 'how are you' in query or 'how do you do' in query:
            as_i_am = [
                'I am Fine,',
                'I am Doing Well,',
                'I am Great,'
            ]
            as_i_am = random.choice(as_i_am)
            print(yellow + f'\n\t{as_i_am} Thanks For Asking!' + reset)
            speak(as_i_am + ' Thanks For Asking!')

        # Replies Thank You!
        elif 'thanks' in query or 'thank you' in query:
            thanksGiving = [
                'Nevermind!',
                'You are Always Welcome!',
                'Mention Not!',
                "That's My Duty!"
            ]
            thanksGiving = random.choice(thanksGiving)
            print(yellow + f'\n\t{thanksGiving}' + reset)
            speak(thanksGiving)

        # Replies Welcome.
        elif 'welcome' in query:
            print(yellow + '\n\tI Feel Honored!' + reset)
            speak('I Feel Honored!')

        # Replies Sorry.
        elif 'sorry' in query or 'my fault' in query or 'my mistake' in query:
            print(yellow + '\n\tHey! Never Repeat This.' + reset)
            speak('Hey! Please Never Repeat This.')

        # User's Name in Query.
        elif name in query or f' {name}' in query or f' {name} ' in query:
            print(yellow + f"\n\tIt's Your Name! {name.title()}." + reset)
            speak(f"It's Your Name! {name}.")                            

        # Changes User's Name
        elif 'change my name' in query:
            print(yellow + f"\n\tWhat Should I Call You From Now?" + reset)
            speak('What Should I Call You From Now?')
            nameChange = command().title()
            if nameChange != "©empty_^_^_queryª":
                name = nameChange.replace('Call Me ', "")
                print(yellow + f"\n\tHello {name.title()}" + reset)
                speak(f'Hello {name}')
            else:
                print(red + '\n\tSorry! Your Name Was Not Changed!')
                speak('Sorry! Your Name Was Not Changed!')

        # Changes Bot's Name.
        elif 'change your name' in query:
            print(yellow + f"\n\tWhat Do You Want My Name To Be?" + reset)
            speak('What Do You Want My Name To Be?')
            botChange = command().title()
            if botChange != "©empty_^_^_queryª":
                bot = botChange.replace('Change Your Name to ', "")
                print(yellow + f"\n\tI am {bot.title()} From Now!" + reset)
                speak(f'I am {bot} From Now!')
            else:
                print(red + '\n\tSorry! My Name Was Not Changed!')
                speak('Sorry! My Name Was Not Changed!')

        # Tells User's Identity.
        elif 'who am i' in query or 'my name' in query:
            print(yellow + f'\n\tYou are {name.title()}.' + reset)
            speak(f"You Are {name}.")

        # It's Creator.
        elif 'who made you' in query or 'who created you' in query:
            print(yellow + '\n\tI Was Made by Sanglap.' + reset)
            speak("I Was Made By Sanglap.")

        # Tells It's Identity.
        elif 'who are you' in query or 'your name' in query:
            print(yellow + f'\n\tI am {bot.title()}, Your Virtual Assistant!' + reset)
            speak(f"I am {bot}, Your Virtual Assistant.")

        # Exit or Quit.
        elif 'exit' in query or 'quit' in query:
            quitApp()

        # Replies Okay
        elif 'ok' in query or 'okay' in query:
            print(yellow + "\n\tThat's It" + reset)
            speak("That's It.")

        # Invaild Query.
        elif '©empty_^_^_queryª' in query:
            print(red + f"  Did Not Get It...\n\n{reset}~\n")
            speak('Did Not Get it!')

        # If Query Is None Of The Above.
        else:
            try:
                try:
                    client  = wolframalpha.Client('Your API') # Generated From wolframalpha.com
                    res = client.query(query)
                    output = next(res.results).text 
                    print(yellow + f'\n\t{output.title()}' + reset)
                    speak(output)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    print(f'\n\t{yellow} {results.title()}' + reset)
                    speak(results)
            except:
                print(yellow + "\n\tShould I Google It?" + reset)
                speak("Should I Google It?")
                reply = command().lower()
                if "yes" in reply or 'ok' in reply or 'yup' in reply or 'do' in reply:
                    print(yellow + f'\n\tGoogling For "{query.title()}"' + reset)
                    speak(f"Googling for {query}")
                    webbrowser.open(f'https://www.google.com/search?q={query}')
                else:
                    print(red + "\n\tTry Something Else!" + reset)
                    speak("Try Something Else!")
