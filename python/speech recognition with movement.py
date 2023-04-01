import speech_recognition as sr
import wikipedia
import pyttsx3
import pywhatkit
import os
import subprocess
from datetime import datetime
import webbrowser
import urllib.request
import random

import serial
import time

now = datetime.now()

jokes = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why do seagulls fly over the sea? Because if they flew over the bay, they'd be bagels!",
    "Why did the photo go to jail..It was framed",
    "Where do polar bears keep their money? In a snowbank.",
]

quotes = [
    "sure......The man who does not read books has no advantage over the one who cannot read them.",
    "sure......Education is the passport to the future, for tomorrow belongs to those who prepare for it today.",
    "sure......Teachers can open the door, but you must enter it yourself.",
    "sure......The beautiful thing about learning is that no one can take it away from you.",
    "sure......Don’t let what you cannot do interfere with what you can do.",
    "sure......A person who never made a mistake never tried anything new.",
    "sure......The expert in anything was once a beginner.",
    "sure......There are no shortcuts to any place worth going.",
    "sure......Motivation is what gets you started. Habit is what keeps you going.",
    "sure......Success is the sum of small efforts, repeated.",
    "sure......The best way to predict your future is to create it.",
    "sure......The future belongs to those who believe in the beauty of their dreams.",
    "sure......Learn from yesterday. Live for today. Hope for tomorrow.",
    "sure......Today a reader. Tomorrow a leader.",
    "sure......You have to be odd to be No.1.",
    "sure......You have to dream before your dreams can come true.",
    "sure......You cannot change your future, but, you can change your habits, and surely your habits will change your future.",
    ]


flag=2
beast_mode=0

def send_command(cmd):
    ser.write(cmd.encode())  # send the command to the Arduino
    time.sleep(0.1)  # wait for the command to be processed

def check(text):
    text = text.lower()
    if "name" in text:
        engine.say("hello i am clara")
        engine.runAndWait()
    elif "age" in text:
        engine.say("i am eighteen years old")
        engine.runAndWait()
    elif "your developer" in text or "you are developer" in text or "developer" in text:
        engine.say("developed and inspired by aaira")
        engine.runAndWait()
    elif "How can you impress me" in text or "Can you impress me" in text or "impress me" in text:
        engine.say("Actually impressing you is a very difficult task for me, If I can sing, I will sing for you. and, If I can dance, I will surely dance for you, But I cant do any of this.  -I am So... sorry")
        engine.runAndWait()
    elif "How can you motivate me" in text or "Can you motivate me" in text or "motivate me" in text:
        joke = random.choice(quotes)
        print(joke)
        engine.say(joke)
        engine.runAndWait()
    elif "hello" in text:
        engine.say("hello,  How can I help you? ")
        engine.runAndWait()
    elif "who are you" in text:
        engine.say("i am clara")
        engine.runAndWait()
    elif "how are you" in text:
        engine.say("i am fine")
        engine.runAndWait()
    elif "tell a joke" in text:
        joke = random.choice(jokes)
        print(joke)
        engine.say(joke)
        engine.runAndWait()
    elif "when is your birthday" in text:
        engine.say("its in christmas eve")
        engine.runAndWait()
    elif "Can you hear me" in text or "can you hear me" in text:
        engine.say("Yes... I can...")
        engine.runAndWait()
    elif "Are you fine" in text or "are you fine" in text :
        engine.say("Yes... Iam fine.. and you..")
        engine.runAndWait()
    elif "I am fine" in text or "i am fine" in text:
        engine.say("Good.. happy to hear...")
        engine.runAndWait()
    elif "Can you help me" in text or "can you help me" in text:
        engine.say("Oh..sure, How can I help you?")
        engine.runAndWait()
        
    elif " move forward" in text:
        send_command("F")
        engine.say("moving forward")
        engine.runAndWait()
    elif " move backward" in text:
        send_command("B")
        engine.say("moving backward")
        engine.runAndWait()
    elif " move left" in text or 'move loft' in text or 'turn left' in text:
        send_command("L")
        engine.say("moving left")
        engine.runAndWait()
    elif " move right" in text or 'turn right' in text:
        send_command("R")
        engine.say("moving right")
        engine.runAndWait()
    elif " stop" in text:
        send_command("S")
        engine.say("stopped")
        engine.runAndWait()
        
   
    elif "play" in text:
       
           
        print(text)
        pywhatkit.playonyt(text)
    elif "stop music" in text or "stop youtube" in text :
        os.system("taskkill /f /im chrome.exe")
    elif "self destruct" in text or "self-destruct" in text:
        engine.say("self deatructing")
        os.system("taskkill /f /im code.exe")

    elif "time" in text :

        t= now.strftime("%r")
        time=''
        for i in range(5):
            time=time+t[i]
        time =time+t[9]+t[10]
        time =time.replace("0","")

        engine.say("the time is......."+time)
        engine.runAndWait()  
        print(time)
       

    elif "bye" in text or "goodbye" in text or "good bye" in text or "good night" in text or "goodnight" in text :
        exit()
   
    elif "who is" in text:
        text = text.replace("who is","")
        wikisearch=wikipedia.summary(text,1)
        engine.say(wikisearch)
        engine.runAndWait()
   
    elif "turn on tube" in text:
        urllib.request.urlopen("http://blr1.blynk.cloud/external/api/update?token=Sag6sE0_v6_tjZF2lMqM3DZ3LDWPpLvd&V0=1")  
    elif "turn off tube" in text:
        urllib.request.urlopen("http://blr1.blynk.cloud/external/api/update?token=Sag6sE0_v6_tjZF2lMqM3DZ3LDWPpLvd&V0=0")
    elif "turn on the bulb" in text:
        urllib.request.urlopen("http://blr1.blynk.cloud/external/api/update?token=Sag6sE0_v6_tjZF2lMqM3DZ3LDWPpLvd&V1=1")
    elif "turn off the bulb" in text:
        urllib.request.urlopen("http://blr1.blynk.cloud/external/api/update?token=Sag6sE0_v6_tjZF2lMqM3DZ3LDWPpLvd&V1=0")

    elif "-" in text :
        engine.say("sorry, I don't understand what you're asking for.")  
        engine.runAndWait()

def beast_check(text):                                              #beast mode questions
    if "" in text:
        engine.say("i dont know... you go mannn")
        engine.runAndWait()
       
       
engine=pyttsx3.init()
engine.setProperty('rate',-1)                    #SPEECH SPEED
voices= engine.getProperty('voices')                
engine.setProperty('voice',voices[2].id)
recognizer=sr.Recognizer()
engine.say("hello...... i am clara...... 3 point o 7")
engine.say("may i help u.......... you have selected microsoft catherine as the default voice")
engine.runAndWait()

ser = serial.Serial('COM7', 9600)  # configure the serial connection

while flag==2:
    if flag%2==0:
        with sr.Microphone() as source:
            #print('Clearing background noise...Please wait')
            recognizer.adjust_for_ambient_noise(source,duration=1)
            print("waiting for your message...")
            recordedaudio=recognizer.listen(source)
            print('Done recording')

            try:
                print('Printing your message...Please wait')
                text=recognizer.recognize_google(recordedaudio,language='en-gb')
                x=-1
                text=text.lower()
                x = text.find("alexa")
                if x>=0:
                    text = text.replace("alexa","-")
                    print(text)
                    if "activate beast mode" in text:       # beast mode
                        beast_mode=1
                        print("activated beast mode")
                    elif "deactivate beast mode" in text:    # beast mode
                        beast_mode=0
                        print("beast mode deactivated")
                    # check
                    if beast_mode==0:
                        check(text)
                    elif beast_mode==1:                  # beast mode
                        beast_check(text)
                    x=-1
                #print(text)
                text=""

            except Exception as ex:
                print(ex)
