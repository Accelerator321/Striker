import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import requests
import json
import datetime
import pickle
import pyautogui as pg
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')

class Striker:

    def __call__(self):

        try:
            file = open('voicefile1.pkl', 'rb')
            vno1 = pickle.load(file)
            Striker.myvoice =engine.setProperty('voice', voices[int(vno1)].id)
            file.close()

        except Exception:
            myvoice = engine.setProperty('voice', voices[0].id)

        global name, number
        name = "Striker"
        number = "First"

class Diva:
    
    def __call__(self):

        try:
            file = open('voicefile2.pkl', 'rb')
            vno2 = pickle.load(file)
            Diva.myvoice =engine.setProperty('voice', voices[int(vno2)].id)
            file.close()

        except Exception:
            myvoice = engine.setProperty('voice', voices[-1].id)

        global name, number
        name = "Diva"
        number = "Second"




# ----------------Speak Function----------------------


def speak(speech):
    '''This fuction speaks the argument given to it.
    But you have to set the voice using
    engine.setProperty('voice', voices[0 or 1].id) first'''

    pyttsx3.speak(speech)
    engine.runAndWait()


#     ----------------Take Command Function------------------

def takecom(comtype):

    '''This function takes command from the user.
    '''
    if comtype == "type":
        a = input("\n-Please Type your command here-\n")
        print(f"<{20*'='}>")
        return a
    while True:
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1
                r.energy_threshold = 4000
                print("Listening........")
                audio = r.listen(source)
                query = r.recognize_google(audio, language="en-in")
                return query

        except Exception:
            e = "Could not recognize the words, Please Speak Again........."
            print(e)
            speak(e)
            continue


# ------A simple Function to reduce the work in code---------------------

def wreak(text):
    '''This function writes and speaks the given arguments.
    It uses speak function'''
    print(text)
    speak(text)


# -------------------------------Wish Function----------------------

def wish(vda):
    '''This function wishesh you.
    It uses wreak function'''
    hour = int(datetime.datetime.now().hour)
    if hour in range(4, 12):
        print(vda, end=": ")
        wreak(f"Good Morning Sir")

    if hour in range(12, 17):
        print(vda, end=": ")
        wreak("Good Afternoon Sir")
    if hour in range(17, 24):
        print(vda, end=": ")
        wreak("Good Evening Sir")


# -------------------Open websites Function----------------------
def openweb(url):
    
    '''This function opens the Url given to it as argument'''

    firefox_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open_new_tab(url)


# ____________________Voice Changer Function______________________________
def voicechanger():
    while True:
        inp = input("Do you want Demo of Voices\nType Yes or no\n").lower()

        if inp == "yes":
            
            
            for m in range(len(voices)):
                engine.setProperty('voice', voices[m].id)
                wreak(f"Hello Sir this is Voice sample {m}\n")

            
            if name == "Striker":
                striker()

            else:
                diva()

        elif inp == "no":
            break
        else:
            print("Please type yes or no")
            continue

    while True:
        inp = input("\nWhich voice you want to change\nType 1 for STRIKER, 2 for DIVA\n")

        if inp not in ["1", "2"]:
            wreak("Please type 1 or 2")
        else:
            break

    wreak(f"There are {len(voices)} voices available\nPlease type a number 0 to {len(voices)-1} to set Voice")

    while True:
        a = input()

        if int(a) not in range(len(voices)):
            print(f"\nPlease type between 0 to {len(voices)-1}")
        
        else:
            if inp == "1":

                with open("voicefile1.pkl", "wb") as f:
                    pickle.dump(a, f)
                
                file = open('voicefile1.pkl', 'rb')
                vno = pickle.load(file)
                Striker.myvoice =engine.setProperty('voice', voices[int(vno)].id)
                file.close()
                wreak("Voice Changed Succesfully")
                striker()
                break

            else:
                with open("voicefile2.pkl", "wb") as f:
                    pickle.dump(a, f)
                
                file = open('voicefile2.pkl', 'rb')
                vno = pickle.load(file)
                Diva.myvoice =engine.setProperty('voice', voices[int(vno)].id)
                file.close()
                wreak("Voice Changed Succesfully")
                diva()
                break

# ---------------------------------------------------------------------------------------
# ------------------------------Program Code Starts Here---------------------------------
# ---------------------------------------------------------------------------------------

if __name__ == '__main__':

    # ____________Checking required data files_____________________


    cdir = os.getcwd()
    required = os.listdir(cdir)
    if "direc.pkl" not in required:
        file = open("direc.pkl", 'wb')
        a = {}
        pickle.dump(a, file)
        file.close()
    
    if "voicefile1.pkl" not in required:

        with open("voicefile1.pkl", "wb") as f:
                    pickle.dump(0, f)
                
        file = open('voicefile1.pkl', 'rb')
        vno1 = pickle.load(file)
        Striker.myvoice =engine.setProperty('voice', voices[int(vno1)].id)
        file.close()

    if "voicefile2.pkl" not in required:

        with open("voicefile2.pkl", "wb") as f:
                    pickle.dump(-1, f)
                
        file = open('voicefile1.pkl', 'rb')
        vno2 = pickle.load(file)
        Diva.myvoice =engine.setProperty('voice', voices[int(vno2)].id)
        file.close()


    # __________________Itroduction______________________________
    striker = Striker()
    diva = Diva()
    striker()
    wish("Striker")
    print("Striker", end=": ")
    wreak("I am Striker")

    diva()
    print("Diva", end=": ")
    wreak("I am Diva")




    # -------------------------Main Program code--------------------

    comtype = "type" # Two comtypes type/speak
    striker()

    while True:

        speak(f"Please {comtype} your command")
        query = takecom(comtype).lower()
        print(f"\nYou: {query.capitalize()}")
        print(name, end=": ")

        if "stop" in query or "exit" in query or "shutdown" in query or "shut down" in query:
            print("Now Shutting Down...........\n"
                "..............Thank you................")
            speak("Now Shutting Down, Thank you")
            exit()

        elif "close" in query and ("program" in query or "app" in query or "window" in query):
            pg.hotkey("alt", "f4")
        
        elif "go" in query and ("sleep mode" in query or "sleepmode" in query):
            wreak("Going to sleep mode")
            input("\n-Please enter any key(A-Z) and hit Enter button to get me out of sleep-\n")
            print(name, end=": ")
            wreak("Sleep mode over")

        # ___________________Websites_______________________

        elif "youtube" in query and "open" in query:
            wreak("Opening Youtube......")
            openweb("youtube.com")
        elif "google" in query and "open" in query:
            wreak("Opening Google......")
            openweb("google.com")

        # _________________________Programs______________________________________

        elif "open" in query:
            file = open("direc.pkl", 'rb')
            direc = pickle.load(file)
            query1 = query.split(" ")

            for item in query1:
                if item in list(direc.keys()):
                    os.startfile(direc[item])
                    wreak(f"Opening {item.capitalize()}")
                    break
            else:
                wreak("No such app was found")

        # __________________Wikipedia______________________

        elif "wikipedia" in query:
            print("Searching wikipedia")
            speak("Searching Wikideia")

            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2, auto_suggest=False)
                print(f"According to Wikipedia {result}")
                speak(f"According to Wikipedia {result}")

            except Exception as e:
                print("Could not find in Wikipedia")
                speak("Could not find in Wikipedia")

        # _____________________News Function__________________

        elif ("show" in query or "tell" in query) and "news" in query:
            print("Showing 5 latest news")
            speak("Showing 5 latest news")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=Your_newsapi_key"
            read = requests.get(url)
            k = json.loads(read.text)

            news_index = 1
            for news in k["articles"]:
                if news_index <= 5:
                    final = news['description']
                    print("=>", final)
                    speak(final)

                    if news_index < 5:
                        speak("Next News")

                    else:
                        speak("News Finished Thank you")
                news_index += 1

        # _____________________MY Name_______________________

        elif "your name" in query:
            wreak(f"Sir my name is {name} ")

        # ______________________Time and Date________________________

        elif "the time" in query:
            ctime = datetime.datetime.now().strftime("%H:%M:%S")
            wreak(f"The Time is {ctime}")

        elif "the date" in query:
            cdate = datetime.date.today()
            wreak(f"The Date is {cdate}")

        # __________________Switching between Striker and Diva__________________

        elif "switch" in query and "striker" in query:
            striker()
            print("==========>Striker")
            print("Striker", end=": ")
            wreak("Thank You for choosing me, Sir")

        elif "switch" in query and "diva" in query:
            diva()
            print("==========>Diva")
            print("Diva", end=": ")
            wreak("Thank You for choosing me, Sir")

        # ________________Saving a directory for an app_______________________

        elif "save" in query and "directory" in query:

            while True:
                app = input("Please type the name of app-\n").lower()
                path = input(f"{name}: Please enter the file path-\n")
                ask = ""
                asklist  = ["p", "d"]
                while ask not in asklist:
                    ask = input(f"{name}: Is this a program or directory\n{name}: type 'p' if program, type 'd' if directory-\n").lower()
                file = open("direc.pkl", 'rb')
                direc = pickle.load(file)
                if ask == "p":

                    if not path.endswith(".exe"):

                        if path.endswith('.exe"'):
                            pass

                        else:
                            print(f"\n{name}", end=": ")
                            wreak("Please enter a path with name of exe file attached to it")
                            print(name, end=": ")
                            continue

                if app not in list(direc.keys()):
                    file = open("direc.pkl", 'wb')
                    direc[app] = path
                    pickle.dump(direc, file)
                    file.close()
                    wreak("Directory saved")
                    another = ""
                    while another not in ["y", "n"]:
                        another = input("Wanna save another directory-type'y' for yes 'n' for No-\n").lower()

                    if another == "y":
                        continue
                    if another == "n":
                        break

                else:
                    wreak("App already exist")
                    break

        # ________________Deleting a program directory_________________________

        elif "delete" in query and ("directory" in query or "app" in query):

            app = input("Please type the name of app-\n").lower()
            file = open("direc.pkl", 'rb')
            direc = pickle.load(file)

            if app in list(direc.keys()):
                file = open("direc.pkl", 'wb')
                del direc[app]
                pickle.dump(direc, file)
                file.close()
                print(name, end=": ")
                wreak("Directory Deleted")
            else:
                print(name, end=": ")
                wreak("No such app or directory exists")

        # ___________________Short Intro____________________________

        elif "short intro" in query:
            wish("")
            wreak(f"\t I am {name}"
                f"\n\t {number} Extension of this Virtual Desktop Assistant\n")


        # ______________________Voice Setter_________________________________
        elif ("change" in query and "voice" in query) or ("open voicechanger" in query) or ("open voice changer") in query:

            voicechanger()

        # _____________________Switching Command Mode_______________________

        elif "switch" in query and "text" in query and "mode" in query:
            comtype = "type"
            wreak("Switching to Text Mode")

        elif "switch" in query and "speech" in query and "mode" in query:
            comtype = "speak"
            wreak("Switching to Speech Mode")

        # ___________________________Question Mode Setup________________ ___________

        elif "question mode" in query or "questionmode" in query:

            wreak("Question mode Initialized")

            while True:

                try:
                    query = takecom(comtype)
                    print("You: " + query,"\n"+ name + ": ", end="")

                    if "exit" in query and ("questionmode" in query or "question mode" in query):
                        wreak("Question mode closed")
                        break

                    elif "switch" in query and "text" in query and "mode" in query:
                        comtype = "type"
                        wreak("Switching to Text Mode")

                    elif "switch" in query and "speech" in query and "mode" in query:
                        comtype = "speak"
                        wreak("Switching to Speech Mode")



                    apikey = "Your_api_key"

                    client = wolframalpha.Client(apikey)

                    res = client.query(query)

                    answer = next(res.results).text

                    wreak(answer)

                except Exception:
                    wreak("Sorry, There was some error")

        # ___________________________Last else Statement__________________________

        else:
            wreak("No actions were found")

        print(f"<{20*'='}>")