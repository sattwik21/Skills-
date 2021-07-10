import datetime
import wikipedia 
import webbrowser
import os
import pywhatkit

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning! ")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")   
    print("I am your Desktop Assistant. Please tell me how may I help you\n")    

if __name__ == "__main__":
    wishMe()
    while True:
          
        query = input("Type your requirement now \n").lower()

        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia")
            print(results)

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query))  and (('yt' in query) or ('youtube' in query)):
            webbrowser.open("youtube.com")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('google' in query)):
            webbrowser.open("google.com")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('stackoverflow' in query)):
            webbrowser.open("stackoverflow.com")   


        elif  (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('movies' in query)):
            music_dir = 'D:\\english novel'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('vscode' in query) or ('code' in query) or ('vs' in query) or ('ide' in query)):
            os.system("code")
        
        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('vlc' in query) or ('media player' in query)):
            os.system("start Vlc")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('virtual box' in query) or ('virtualbox' in query) or ('vm' in query) or ('virtual machine' in query)):
            os.system("VirtualBox")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('chrome' in query) or ('web browser' in query) or ('google chrome' in query) or ('browser' in query)):
            os.system("start chrome")
        
        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('discord' in query)):
            os.system("discord")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('illustrator' in query) or ('ai' in query)):
            os.system("illustrator")

        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('photoshop' in query) or ('ps' in query)):
            os.system("photoshop")
        
        elif (('open' in query) or ('start' in query) or ('run' in query) or ('execute' in query)) and (('figma' in query)):
            os.system("figma")

        elif 'What are you doing?' in query:
            print("waiting for your commands master")
        
        elif 'play' in query:
            print('Searching Youtube...')
            query = query.replace("play", "")
            results = pywhatkit.playonyt(query)
        
        elif 'search' in query:
            print('Searching google...')
            query = query.replace("search", "")
            results = pywhatkit.search(query)

        elif 'exit' in query:
            print("Bye master!")
            break
        
        else:
            print("Please type again, your previous command was beyond my comprehension")
