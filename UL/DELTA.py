import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import wolframalpha
import pyjokes
from pyautogui import screenshot
import webbrowser
import time
import subprocess
import os
import cv2
import random
from requests import get
import smtplib
from email.message import EmailMessage
import psutil
import instaloader
import pyautogui
import PyPDF2
# from Recordings import Record_Option
from PIL import ImageGrab
import pyaudio
import wave
import numpy as np    
import urllib.request
# from PhoneNumer import Phonenumber_location_tracker
from bs4 import BeautifulSoup
# from state import state
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import qrcode
import requests
import json
from pyautogui import click
from pyautogui import press
from pyautogui import write
from time import sleep
import datetime
import phonenumbers
from phonenumbers import geocoder
import folium
from phonenumbers import carrier
from keyboard import press_and_release
from opencage.geocoder import OpenCageGeocode

dict = {"suraj":"surajsc8928@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("          ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Your Command :  {query}\n")

    except:
        return "None"
    return query.lower()


def GreetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")

    Speak("initializing Delta...!")
    
#Weather forecast
def temperature():
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        Speak(f"current {search} is {temp}")
        
#weather
def weather():
    API_KEY = '9e39846f9abb1a4c6be08f618d02e9ed'
    Speak("Which city or country weather do you want to know?")
    LOCATION = takecommand().lower()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Print weather information
    print(f'Weather Description: {weather_description}')
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Wind Speed: {wind_speed} m/s')        
    Speak(f'Weather Description: {weather_description}')
    Speak(f'Temperature: {temperature}°C')
    Speak(f'Humidity: {humidity}%')
    Speak(f'Wind Speed: {wind_speed} m/s')        

#qrCodeGenerator
def qrCodeGenerator():
    Speak(f"Sir enter the text/link that you want to keep in the qr code")
    input_Text_link = takecommand()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
    )
    QRfile_name = (str(datetime.datetime.now())).replace(" ","-")
    QRfile_name = QRfile_name.replace(":","-")
    QRfile_name = QRfile_name.replace(".","-")
    QRfile_name = QRfile_name+"-QR.png"
    qr.add_data(input_Text_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"C:\\Users\\SURAJ\\OneDrive\\Pictures\\Saved Pictures\\{QRfile_name}")
    Speak(f"Sir the qr code has been generated")
    

#Web camera
#NOTE to exit from the web camera press "ESC" key 
def webCam(self):    
    Speak('Opening camera')
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imsquery('web camera',img)
        k = cv2.waitKey(50)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    

#covid 
def Covid(s):
    state = {"andaman and nicobar islands": "Andaman and Nicobar Islands","andhra pradesh":"Andhra Pradesh","arunachal pradesh":"Arunachal Pradesh","assam":"Assam","bihar":"Bihar","chandigarh":"Chandigarh","Chhattisgarh":"Chhattisgarh","dadra":"Dadra and Nagar Haveli and Daman and Diu","Nagar Haveli":"Dadra and Nagar Haveli and Daman and Diu","daman":"Dadra and Nagar Haveli and Daman and Diu","diu":"Dadra and Nagar Haveli and Daman and Diu","delhi":"Delhi","goa":"Goa","gujarat":"Gujarat","haryana":"Haryana","himachal pradesh":"Himachal Pradesh","jammu and kashmir":"Jammu and Kashmir","jharkhand":"Jharkhand","karnataka":"Karnataka","kerala":"Kerala","ladakh":"Ladakh","lakshadweep":"Lakshadweep","madhya pradesh":"Madhya Pradesh","maharashtra":"Maharashtra","manipur":"Manipur","meghalaya":"Meghalaya","mizoram":"Mizoram","nagaland":"Nagaland","odisha":"Odisha","puducherry":"Puducherry","punjab":"Punjab","skkim":"Skkim","tamil nadu":"Tamil Nadu","telangana":"Telangana","tripura":"Tripura","uttarakhand":"Uttarakhand","uttar pradesh":"Uttar Pradesh","west bengal":"West Bengal"}
    try:
        from covid_india import states
        details = states.getdata()
        if "check in" in s:
            s = s.replace("check in","").strip()
            print(s)
        elif "check" in s:
            s = s.replace("check","").strip()
            print(s)
        elif "tech" in s:
            s = s.replace("tech","").strip()
        s = state[s]
        ss = details[s]
        Total = ss["Total"]
        Active = ss["Active"]
        Cured = ss["Cured"]
        Death = ss["Death"]
        print(f"Sir the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
        Speak(f"Sir the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
        time.sleep(2)
        Speak("Sir do you want any information of other states")
        I = takecommand().lower()    
        print(I)
        if ("check" in I):
            Covid(I)
        elif("no" in I):
            Speak("Okay Sir stay home stay safe")
        else:
            Speak("Okay Sir stay home stay safe")
    except:
        Speak("Sir some error occured, please try again")
        Speak("Sir do you want any information of other states")
        I = takecommand().lower()      
        if("yes" in I):
            Speak("Sir, Which state covid status do u want to check")
            Sta = takecommand().lower()        
            Covid(Sta)
        elif("no" in I):
            Speak("Okay Sir stay home stay safe")
        else:
            Speak("Okay Sir stay home stay safe")
            
# Fetch latest news
def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=35705f5139a14db99ae0b77f829a702a",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=35705f5139a14db99ae0b77f829a702a",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=35705f5139a14db99ae0b77f829a702a",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=35705f5139a14db99ae0b77f829a702a",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=35705f5139a14db99ae0b77f829a702a",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=35705f5139a14db99ae0b77f829a702a"
}

    content = None
    url = None
    Speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = takecommand().lower()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = takecommand().lower()
        if str(a) == "one":
            pass
        elif str(a) == "two":
            break
        
    Speak("thats all")
    

# Rock paper scissors
def game_play():
    Speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Com_score = 0
    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takecommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                Speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                Speak("paper")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                Speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

            elif (com_choose == "paper"):
                Speak("paper")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak("Scissors")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                Speak("ROCK")
                Com_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            elif (com_choose == "paper"):
                Speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            else:
                Speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
        i += 1
    
    print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")
    

def whatsappMsg(name, message):
    
    click(x=1060, y=1050)
    sleep(2)
    click(x=310, y=155)
    sleep(2)
    write(name)
    sleep(2)
    click(x=304, y=251)
    sleep(2)
    click(x=741, y=988)
    sleep(2)
    write(message)
    press('enter')
    
def whatsappCall(name):
    click(x=1060, y=1050)
    sleep(2)
    press('windows + up arrow')
    sleep(2)
    click(x=310, y=155)
    sleep(2)
    write(name)
    sleep(2)
    click(x=304, y=251)
    sleep(2)
    click(x=1769, y=93)

def whatsappVDCall(name):
    click(x=1060, y=1050)
    sleep(2)
    press('windows + up arrow')
    sleep(2)
    click(x=310, y=155)
    sleep(2.5)
    write(name)
    sleep(2)
    click(x=304, y=251)
    sleep(2)
    click(x=1722, y=92)

def whatsappChat(name):
    click(x=1060, y=1050)
    sleep(2)
    press('windows + up arrow')
    sleep(2)
    click(x=310, y=155)
    sleep(2.5)
    write(name)
    sleep(2)
    click(x=304, y=251)
    
    
def No_result_found():
        Speak('Sir I couldn\'t understand, could you please say it again.')
    
    
def Fun(query):
    
    if 'your name' in query:
       Speak("My name is Delta")
       
    elif 'my name' in query:
       Speak("your name is Suraj")
       
    elif 'university name' in query:
       Speak("you are studing in Shivajirao S. Jondhale College Of Engineering, persuing batchelor in Computer Science.") 
    
    elif 'what can you do' in query:
       Speak("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
    
    elif 'your age' in query:
       Speak("I am very young that you.")
   
    elif 'joke' in query:
       Speak(pyjokes.get_joke())
   
    elif 'are you there' in query:
       Speak('Yes Sir I am here')
  
    elif 'tell me something' in query:
       Speak('Sir, I don\'t have much to say, you only tell me someting i will give you the company')

    elif 'thank you' in query:
       Speak('Sir, I am here to help you..., your welcome')

    elif 'in your free time' in query:
       Speak('Sir, I will be listening to all your words')
 
    elif 'can you hear me' in query:
       Speak('Yes Sir, I can hear you')
 
    elif 'do you ever get tired' in query:
       Speak('It would be impossible to be feel tired')
  
    else :
        No_result_found()
        
#clock commands
def Clock_time(query):
    print(query)
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    Speak("Current time is "+ time)
    
    
#calender day
def Cal_day():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
    
    return day_of_the_week

#schedule function for remembering todays plans
def schedule():
    day = Cal_day()
    Speak("Sir, today's schedule is")
    Week = {"Monday" : "Sir, you have holiday today, you have scheduled this day for you college assignments",
    "Tuesday" : "Sir, from 10:00 to 11:00 you have Cryptography and System security class, from 11:00 to 12:00 you have Mobile Computing class, from 12:00 to 1:00 you have System Programming and Compiler Construction class, from 1:00 to 1:30 you have 30 minutes brake, and today you have Cloud Computing lab from 1:30 to 5:30",
    "Wednesday" : "Sir, from 10:00 to 11:00 you have Artificial Inteligence class, from 11:00 to 12:00 you have Cryptography and System security class, from 12:00 to 1:00 you have Mobile Computing class, from 1:00 to 1:30 you have 30 minutes brake, and today you have System Programming and Compiler Construction lab from 1:30 to 3:30",
    "Thrusday" : "Sir, from 10:00 to 11:00 you have Internet of things class, from 11:00 to 12:00 you have Artificial Intelligence class, from 12:00 to 1:00 you have System Programming and Compiler Construction class, today you don't have any lab.",
    "Friday" : "Sir, today you have a full day of classes from 10:00 to 12:00 you have Artificial Intelligence lab, from 12:00 to 1:00 you have Internet of things, from 1:00 to 1:30 you have 30 minutes brake, after that from 1:30 to 2:30 you have Cryptography and System Security, from 2:30 to 3:30 you have System Programming and Compiler Construction class, then after that you have one more lab of Mobile Computing from 3:30 to 5:30",
    "Saturday" : "Sir, today you have a Cryptograhy and System Security lab from 10:00 to 12:00, from 12:00 to 1:00 you have Artificial Intelligence class, then you have a 30 minutes brake from 1:00 to 1:30, from 1:30 to 2:30 you have Internet Of Things class, from 2:30 to 3:30 you have Mobile compuying class.",
    "Sunday": "Sir, today is holiday but we can't say anything when they will bomb with any assisgnments"}
    if day in Week.keys():
        Speak(Week[day])

        
# college resources commands
def college_classroom(query):
    print(query)
    
    if ('internet of things' in query) or ('iot' in query):
        Speak('opening your iot Classroom')
        webbrowser.open('https://classroom.google.com/u/0/c/NTEyNDY2NDMyNTYx')
        
    elif ('system programming and compiler construction' in query) or ('spcc' in query):
        Speak('opening your SPCC classroom')
        webbrowser.open('https://classroom.google.com/u/0/c/NDc0MTc4NjgzNDQz')
 
    elif ('artificial intelligence' in query) or ('ai' in query):
        Speak('opening your AI classroom')
        webbrowser.open('https://classroom.google.com/u/0/c/NDU2Nzk3ODgxMTk1')
 
    elif ('mobile computing' in query) or ('mc' in query):
        Speak('opening your MC classroom')
        webbrowser.open('https://classroom.google.com/u/0/c/NTEyMDQ4NjczODMz')

    elif 'college' in query:
        Speak('opening your college website')
        webbrowser.open('http://www.jondhleengg.org/')

    else :
        No_result_found()
        
# communication command        # 
def comum():
    query = takecommand().lower()
    if ('hi'in query) or('hai'in query) or ('hey'in query) or ('hello' in query) :
        Speak("Hello boss what can I help for u")
    else :
        No_result_found()

#Silence
def silence(k):
    t = k
    s = "Ok boss I will be silent for "+str(t/60)+" minutes"
    Speak(s)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(2)
        t -= 1
    Speak("Boss "+str(k/60)+" minutes over")


def silenceTime(query):
    print(query)
    x=0
    #caliculating the given time to seconds from the speech commnd string
    if ('10' in query) or ('ten' in query):x=600
    elif '1' in query or ('one' in query):x=60
    elif '2' in query or ('two' in query):x=120
    elif '3' in query or ('three' in query):x=180
    elif '4' in query or ('four' in query):x=240
    elif '5' in query or ('five' in query):x=300
    elif '6' in query or ('six' in query):x=360
    elif '7' in query or ('seven' in query):x=420
    elif '8' in query or ('eight' in query):x=480
    elif '9' in query or ('nine' in query):x=540
    silence(x)
    
    
#OTT platform   
def OTT(query):
    if 'hotstar' in query:
        Speak('opening your disney plus hotstar')
        webbrowser.open('https://www.hotstar.com/in')
    elif 'prime' in query:
        Speak('opening your amazon prime videos')
        webbrowser.open('https://www.primevideo.com/')
    elif 'netflix' in query:
        Speak('opening Netflix videos')
        webbrowser.open('https://www.netflix.com/')
    else :
        No_result_found()
        
        
#Wikipedia
def wiki(query):
    print(query)
    try:
        # ('what is meant by' in self.query) or ('tell me about' in self.query) or ('who the heck is' in self.query)
        if ('wikipedia' in query):
            target1 = query.replace('search for','')
            target1 = target1.replace('in wikipedia','')
        elif('what is meant by' in query):
            target1 = query.replace("what is meant by"," ")
        elif('tell me about' in query):
            target1 = query.replace("tell me about"," ")
        elif('who the heck is' in query):
            target1 = query.replace("who the heck is"," ")
        print("searching....")
        info = wikipedia.summary(target1,2)
        print(info)
        Speak("according to wikipedia "+info)
    except :
        No_result_found()

# Google application
def Google_Apps(query):
    print(query)
    if 'mail' in query:
        Speak('opening your google gmail')
        webbrowser.open('https://mail.google.com/mail/')
    elif 'maps' in query:
        Speak('opening google maps')
        webbrowser.open('https://www.google.co.in/maps/')
    elif 'news' in query:
        Speak('opening google news')
        webbrowser.open('https://news.google.com/')
    elif 'calendar' in query:
        Speak('opening google calender')
        webbrowser.open('https://calendar.google.com/calendar/')
    elif 'photos' in query:
        Speak('opening your google photos')
        webbrowser.open('https://photos.google.com/')
    elif 'documents' in query:
        Speak('opening your google documents')
        webbrowser.open('https://docs.google.com/document/')
    elif 'spreadsheet' in query:
        Speak('opening your google spreadsheet')
        webbrowser.open('https://docs.google.com/spreadsheets/')
    else :
        No_result_found()
        
# open desktop apps
def OpenApp(query):
    print(query)
    
    if ('paint'in query):
        Speak('Opening msPaint')
        os.startfile('c:\\Windows\\System32\\mspaint.exe')
    elif ('notepad'in query) :
        Speak('Opening notepad')
        os.startfile('c:\\Windows\\System32\\notepad.exe')
    elif ('discord'in query) :
        Speak('Opening discord')
        os.startfile('..\\..\\Discord.exe')
    elif ('editor'in query) :
        Speak('Opening your Visual studio code')
        os.startfile('..\\..\\Code.exe')
    elif ('online classes'in query) :
        Speak('Opening your Microsoft teams')
        webbrowser.open('https://teams.microsoft.com/')
    elif ('spotify'in query) :
        Speak('Opening spotify')
        os.startfile('..\\..\\Spotify.exe')
    elif ('lt spice'in query) :
        Speak('Opening lt spice')
        os.startfile("..\\..\\XVIIx64.exe")
    elif ('steam'in query) :
        Speak('Opening steam')
        os.startfile("..\\..\\steam.exe")
    elif ('media player'in query) :
        Speak('Opening VLC media player')
        os.startfile("C:\Program Files\VideoLAN\VLC\vlc.exe")
    else :
       No_result_found()
       
# Send Email
dict = {"suraj":"surajsc8928@gmail.com"}

def send_email(receiver, subject, content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("surajsc983@gmail.com", "buyaqtzlpdeqcdzu")
    email = EmailMessage()
    email["From"] = "surajsc983@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(content)
    server.send_message(email)

# location
def location():
    Speak("Wait boss, let me check")
    try:
        IP_Address = get('https://api.ipify.org').text
        print(IP_Address)
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        print(url)
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        tZ = geo_data['timezone']
        longitude = geo_data['longitude']
        latidute = geo_data['latitude']
        org = geo_data['organization_name']
        print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
        Speak(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
        Speak(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
    except Exception as e:
        Speak("Sorry boss, due to network issue i am not able to find where we are.")
        pass

    #Instagram profile
def Instagram_Pro():
    Speak("Boss please enter the user name of Instagram: ")
    name = input("Enter username here: ")
    webbrowser.open(f"www.instagram.com/{name}")
    time.sleep(2)
    Speak("Boss would you like to download the profile picture of this account.")
    cond = takecommand().lower()
    if('download' in cond):
        mod = instaloader.Instaloader()
        mod.download_profile(name,profile_pic_only=True)
        Speak("I am done boss, profile picture is saved in your main folder. ")
    else:
        pass
    
# pdf reader
def pdf_reader():
    # Speak("Boss enter the name of the book which you want to read")
    # n = input("Enter the book name: ")
    # n = n.strip()+".pdf"
    # book_n = open('D:\\React Cheatsheet\\JSX_Cheatsheet.pdf','rb')
    # pdfReader = PyPDF2.PdfFileReader(book_n)
    # pages = pdfReader.numPages
    # Speak(f"Boss there are total of {pages} in this book")
    # Speak("plsase enter the page number Which I nedd to read")
    # num = int(input("Enter the page number: "))
    # page = pdfReader.getPage(num)
    # text = page.extractText()
    # print(text)
    # Speak(text)
    os.startfile('D:\\React Cheatsheet\\JSX_Cheatsheet.pdf')
    book = open('D:\\React Cheatsheet\\JSX_Cheatsheet.pdf','rb')
    pdfreader = PyPDF2.PdfReader(book)
    pages = len(pdfreader.pages)
    page = pdfreader.pages[0]
    text = page.extract_text()
    
    
# activate mod
def Activate():
    Speak("how to do mode is is activated")
    while True:
        Speak("Please tell me what you want to know")
        query = takecommand().lower()
        try:
            if ("exit" in query) or("close" in query):
                Speak("Ok sir query to mode is closed")
                break
            else:
                max_result=1
                how_to = search_wikihow(query ,max_result)
                assert len(how_to) == 1
                how_to[0].print()
                Speak(how_to[0].summary)
        except Exception as e:
            Speak("Sorry sir, I am not able to find this")
            
def Mobilecamra():
    try:
        Speak(f"Boss openinging mobile camera")
        URL = "http://192.168.0.208.8080/shot.jpg" #Discription for this is available in the README file
        while True:
            imag_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
            img = cv2.imdecode(imag_arr,-1)
            cv2.imshow('IPWebcam',img)
            q = cv2.waitKey(1)
            if q == ord("q"):
                Speak(f"Boss closing mobile camera")
                break
        cv2.destroyAllWindows()
    except Exception as e:
        print("Some error occured")
        
def Phonenumber_location_tracker():
    current_path = os.getcwd()
    num = input("Enter a number: ")
    time_ = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    #API key
    API_key = "58b54e2d5b114a129816515ad55e2b2b"
    sanNummber = phonenumbers.parse(num)
    #country Location finder
    location = geocoder.description_for_number(sanNummber,"en")
    #Service provider finder
    sea_pro = phonenumbers.parse(num)
    servise_prover=carrier.name_for_number(sea_pro,'en')
    #Finding the latitude and longitude
    geocoder = OpenCageGeocode(API_key)
    quesry = str(location)
    resltt = geocoder.geocode(quesry)
    lat = resltt[0]['geometry']['lat']
    lng = resltt[0]['geometry']['lng']
    #creating a map with the phone number location as pointer
    mymap = folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=location).add_to(mymap)
    mymap.save(rf"{current_path}/Maps/{num+str('-')+str(time_)}.html")

    return location,servise_prover,lat,lng

# Internet Speed
def InternetSpeed():
    Speak("Wait a few seconds boss, checking your internet speed")
    st = speedtest.Speedtest()
    dl = st.download()
    dl = dl/(1000000) #converting bytes to megabytes
    up = st.upload()
    up = up/(1000000)
    print(dl,up)
    Speak(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")


# System Condition
def condition():
    usage = str(psutil.cpu_percent())
    Speak("CPU is at " +usage+ " percentage")
    battray = psutil.sensors_battery()
    percentage = battray.percent
    Speak(f"Boss our system have {percentage} percentage Battery")
    if percentage >=75:
        Speak(f"Boss we could have enough charging to continue our work")
    elif percentage >=40 and percentage <=75:
        Speak(f"Boss we should connect out system to charging point to charge our battery")
    elif percentage >=15 and percentage <=30:
        Speak(f"Boss we don't have enough power to work, please connect to charging")
    else:
        Speak(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")
    
# Latest news
def news():
    MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=35705f5139a14db99ae0b77f829a702a"
    MAIN_PAGE_ = get(MAIN_URL_).json()
    articles = MAIN_PAGE_["articles"]
    headings=[]
    seq = ['first','second','third','fourth','fifth'] #If you need more than ten you can extend it in the list
    for ar in articles:
        headings.append(ar['title'])
    for i in range(len(seq)):
        print(f"todays {seq[i]} news is: {headings[i]}")
        Speak(f"todays {seq[i]} news is: {headings[i]}")
    Speak("Boss I am done, I have read most of the latest news")
    
def WolfRamAlpha(query):
    apikey = "7HPGGV-EUP9W5KLGV"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        Speak("The value is not answerable")
        
def Calc(query):
    Term = str(query)
    Term = Term.replace("delta","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        Speak(result)

    except:
        Speak("The value is not answerable")
    
    
# Main Execution
def taskExe():
        Speak("Today is " + Cal_day())
        GreetMe()
        Speak('Hello boss I am delta your assistant. please tell me how can i help you')
        while True:
            
            query = takecommand().lower()
            
            if ('your age' in query) or ('are you there' in query) or ('tell me something' in query) or ('thank you' in query) or ('in your free time' in query) or ('can you hear me' in query) or ('do you ever get tired' in query):
                Fun(query)
                
            elif 'window' in query:
                pyautogui.hotkey('winleft', 'm')
                
            elif 'time' in query : 
                Clock_time(query)
                
            elif (('hi' in query) and len(query)==2) or ((('hai' in query) or ('hey' in query)) and len(query)==3) or (('hello' in query) and len(query)==5):
                comum()
                
            elif ('what can you do' in query) or ('your name' in query) or ('my name' in query) or ('university name' in query):
                Fun(query)
                
            elif 'joke'in query:
                Fun(query)
                
            #schedule commands for remembering you what is the planns of the day
            elif ("college time table" in query) or ("schedule" in query):
                schedule()
                
            #It will tell the day Eg : Today is wednesday
            elif ("today" in query):
                day = Cal_day()
                Speak("Today is "+ day)
            
            #command if you don't want the delta to spack until for a certain time
            #Note: I can be silent for max of 10mins
            # Eg: delta keep quiet for 5 minutes 
            elif ('silence' in query) or ('silent' in query) or ('keep quiet' in query) or ('wait for' in query) :
                silenceTime(query)
                
            #command for opening your OTT platform accounts
            #Eg: open hotstart
            elif ('hotstar' in query) or ('prime' in query) or ('netflix' in query):
                OTT(query)
                
            elif 'weather' in query:
                weather()
                
            #command for opeing college websites
            elif ('internet of things' in query) or ('iot' in query) or ('system programming and compiler construction' in query) or ('spcc' in query) or ('artificial intelligence' in query) or ('ai' in query) or ('mobile computing' in query) or ('mc' in query) or ('college' in query):
                college_classroom(query)
            #command to search for something in wikipedia
            #Eg: what is meant by python in wikipedia (or) search for "_something_" in wikipedia
            elif ('wikipedia' in query) or ('what is meant by' in query) or ('tell me about' in query) or ('who the heck is' in query):
                wiki(query)
                
            elif 'google search' in query:
                import wikipedia as googleScrap
                query = query.replace("delta", "")
                query = query.replace("google search", "")
                query = query.replace("google", "")
                Speak("This Is What I Found On The Web!")
                pywhatkit.search(query)

                try:
                    result = googleScrap.summary(query, 1)
                    Speak(result)

                except:
                    Speak("No Speakable Data Available!")
                    
            #command to open your google applications
            elif ('open mail'in query) or('open maps'in query) or('open calendar'in query) or('open documents'in query )or('open spreadsheet'in query) or('open photos'in query) or('open drive'in query) or ('open news' in query):
                Google_Apps(query)
                
            # #Command to open desktop applications
            # #It can open : caliculator, notepad,paint, teams(aka online classes), discord, spotify, ltspice,vscode(aka editor), steam, VLC media player
            elif ('open calculator'in query) or ('open notepad'in query) or ('open paint' in query) or ('open online classes'in query) or ('open discord'in query)  or ('open spotify'in query) or ('open steam'in query):
                OpenApp(query)
                
            elif 'close' in query:
                pyautogui.hotkey('alt', 'f4')
                
            elif "launch" in query:
                query = query.replace("launch", "")
                # query = query.replace("delta", "")
                press("super")
                sleep(2)
                write(query)
                sleep(2)
                press("enter")
                
                if 'chrome' in query:
                    query = query.replace("launch", "")
                    query = query.replace("delta", "")
                    press("super")
                    sleep(2)
                    write(query)
                    sleep(2)
                    press("enter")
                    click(x=659, y=633)
                    sleep(1)
                    Speak("What do you want to search?")
                    a = takecommand().lower()
                    pyautogui.hotkey('ctrl', 'K')
                    write(a)
                    press('enter')
                
            
            elif 'new document' in query:
                pyautogui.hotkey('ctrl', 'n')
                press("enter")
                press("enter")
                write(query)
                
            if 'send email' in query:
                sleep(2)
                pyautogui.hotkey('alt', 'f4')
                Speak("To Whom do you want to send this email?")
                name = takecommand()
                receiver = dict[name]
                Speak("What is the subject of the email?")
                subject = takecommand()
                Speak("What is the message you want to send to the " + receiver)
                content = takecommand()
                send_email(receiver, subject, content)
                Speak("Email has been sent successfully!")
                
                # #Command to close desktop applications
            # #It can close : caliculator, notepad,paint, discord, spotify, ltspice,vscode(aka editor), steam, VLC media player
            # elif ('close calculator'in query) or ('close notepad'in query) or ('close paint'in query) or ('close discord'in query) or ('close ltspice'in query) or ('close editor'in query) or ('close spotify'in query) or ('close steam'in query) or ('close media player'in query):
            #     CloseApp(query)
            
            # #command for asking your current location
            # elif ('where i am' in query) or ('where we are' in query):
            #     location()
                
            # #command for opening command prompt 
            # #Eg: delta open command prompt
            elif ('command prompt'in query) :
                Speak('Opening command prompt')
                os.system('start cmd')
                
            # #Command for opening an instagram profile and downloading the profile pictures of the profile
            # #Eg: delta open a profile on instagram 
            elif ('instagram profile' in query) or("profile on instagram" in query):
                Instagram_Pro()
                
            # #Command for opening taking screenshot
            # #Eg: delta take a screenshot
            elif ('screenshot' in query):
                # im = screenshot()
                # im.save("ss.jpg")
                Speak("Ok Sir, What Should I Name That File ?")
                path = takecommand().lower()
                path1name = path + ".png"
                path1 = "C:\\Users\\SURAJ\\OneDrive\\Pictures\\Screenshots\\" + path1name
                kk = screenshot()
                kk.save(path1)
                os.startfile("C:\\Users\\SURAJ\\OneDrive\\Pictures\\Screenshots\\" + path1name)
                
            # #Command for reading PDF
            # #EG: delta read pdf
            elif ("read pdf" in query) or ("pdf" in query):
                pdf_reader()
                
            # #command for searching for a procedure query to do something
            # #Eg:delta activate mod
            #   delta query to make a cake (or) delta query to convert int to string in programming 
            elif "activate mode" in query:
                Activate()
                
            # #command for increaing the volume in the system
            # #Eg: delta increase volume
            elif ("volume up" in query) or ("increase volume" in query):
                pyautogui.press("volumeup")
                Speak('volume increased')
                
            # #command for decreaseing the volume in the system
            # #Eg: delta decrease volume
            elif ("volume down" in query) or ("decrease volume" in query):
                pyautogui.press("volumedown")
                Speak('volume decreased')
                
            # #Command to mute the system sound
            # #Eg: delta mute the sound
            elif ("volume mute" in query) or ("mute the sound" in query) or ("unmute" in query) or ("mute" in query) :
                pyautogui.press("volumemute")
                Speak('volume muted')
                
            # #command for opening your mobile camera the description for using this is in the README file
            # #Eg: delta open mobile camera
            elif ("open mobile camera" in query):
                Mobilecamra()
                
            # #Command for checking covid status in India
            # #Eg: delta check covid (or) corona status
            elif ("covid" in query) or  ("corona" in query):
                Speak("Boss which state covid 19 status do you want to check")
                s = takecommand().lower()
                Covid(s)


            # #Command for phone number tracker
            elif ("track" in query) or ("track a mobile number" in query):
                Speak("Boss please enter the mobile number with country code")
                try:
                    location,servise_prover,lat,lng=Phonenumber_location_tracker()
                    Speak(f"Boss the mobile number is from {location} and the service provider for the mobile number is {servise_prover}")
                    Speak(f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}")
                    print(location,servise_prover)
                    print(f"Latitude : {lat} and Longitude : {lng}")
                    Speak("Boss location of the mobile number is saved in Maps")
                except:
                    Speak("Boss an unexpected error occured couldn't track the mobile number")

            # #command for knowing your system IP address
            # #Eg: delta check my ip address
            elif 'ip address' in query:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                Speak(f"your IP address is {ip}")

            # #command for checking the temperature in surroundings
            # #delta check the surroundings temperature
            elif "temperature" in query:
               temperature()
                
            elif 'whatsapp' in query:

                if 'call' in query:
                    name = query.replace("whatsapp","")
                    name = name.replace("call","")
                    name = name.replace("to","")
                    Name = str(name)
                    whatsappCall(Name)
                
                elif 'video' in query:
                    name = query.replace("whatsapp","")
                    name = name.replace("video","")
                    name = name.replace("call","")
                    name = name.replace("to","")
                    Name = str(name)
                    whatsappVDCall(Name)
                    
                elif 'message' in query:
                    name = query.replace("send", "")
                    name = name.replace("whatsapp", "")
                    name = name.replace("message", "")
                    name = name.replace("to", "")
                    Name = str(name)
                    Speak(f"Whats the message for {Name}")
                    Msg = takecommand()
                    whatsappMsg(Name, Msg)

                elif 'chat' in query:
                    Speak("With Whom ?")
                    name = takecommand()
                    whatsappChat(name)
            
            elif 'terminate' in query:
                if 'call' in query:
                    click(x=1070, y=819)
                    sleep(2)
                    click(x=1894, y=9)

                elif 'video' in query:
                    click(x=1049, y=914)
                    sleep(2)
                    click(x=1894, y=9)

                else:
                    click(x=1894, y=9)
                    
            # #Command to generate the qr codes
            elif ("create a qr code" in query) or ("qr code" in query):
                qrCodeGenerator()
                
            # #command for checking internet speed
            # #Eg: delta check my internet speed
            elif "internet speed" in query:
                InternetSpeed()
                
            # #command to make the delta sleep
            # #Eg: delta you can sleep now
            elif ("you can sleep" in query) or ("sleep now" in query):
                Speak("Okay boss, I am going to sleep you can call me anytime.")
                break
            
            # #command for waking the delta from sleep
            # #delta wake up
            elif ("wake up" in query) or ("get up" in query):
                Speak("boss, I am not sleeping, I am in online, what can I do for you")
                
            # #command for exiting delta from the program
            # #Eg: delta goodbye
            elif ("goodbye" in query) or ("get lost" in query):
                Speak("Thanks for using me boss, have a good day")
                sys.exit()
                
                
            # #command for knowing about your system condition
            # #Eg: delta what is the system condition
            elif ('system condition' in query) or ('condition of the system' in query):
                Speak("checking the system condition")
                condition()
                
            # #command for knowing the latest news
            # #Eg: delta tell me the news
            
            elif ('tell me news' in query) or ("the news" in query) or ("todays news" in query):
                Speak("Please wait boss, featching the latest news")
                news()
            # #command for shutting down the system
            # #Eg: delta shutdown the system
            elif ('shutdown the system' in query) or ('down the system' in query):
                Speak("Boss shutting down the system in 10 seconds")
                time.sleep(20)
                os.system("shutdown /s /t 5")
            # #command for restarting the system
            # #Eg: delta restart the system
            elif 'restart the system' in query:
                Speak("Boss restarting the system in 10 seconds")
                time.sleep(20)
                os.system("shutdown /r /t 5")
                
            # #command for make the system sleep
            # #Eg: delta sleep the system
            elif 'sleep the system' in query:
                Speak("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
                
            elif "calculate" in query:
                query = query.replace("calculate","")
                query = query.replace("jarvis","")
                Calc(query)
                
            # elif "set an alarm" in query:
            #     print("input time example:- 10 and 10 and 10")
            #     Speak("Set the time")
            #     a = takecommand().lower()
            #     alarm(a)
            #     Speak("Done,sir")
            
            elif 'new tab' in query:
                press_and_release('ctrl + t')
            
            elif ('write' in query) or ('enter' in query):
                a = takecommand().lower()
                press('enter')
                
            elif 'tab' in query:
                press_and_release('ctrl + w')

            elif 'new window' in query:
                press_and_release('ctrl + n')

            elif 'history' in query:
                press_and_release('ctrl + h')

            elif 'download' in query:
                press_and_release('ctrl + j')

            elif 'bookmark' in query:
                press_and_release('ctrl + d')

            elif 'incognito' in query:
                press_and_release('Ctrl + Shift + n')

            elif 'switch tab' in query:
                tab = query.replace("switch tab ", "")  
                Tab = tab.replace("to","")
                num = Tab
                bb = f'ctrl + {num}'
                press_and_release(bb)

            elif 'down' in query:
                press('pagedown')

            elif 'up' in query:
                press('pageup')

            
            elif 'open' in query:
                name = query.replace("open ","")
                name = name.replace("website ","")
                NameA = str(name)

                if 'youtube' in NameA:
                    webbrowser.open("https://www.youtube.com/")

                else:
                    string = "https://www." + NameA + ".com"
                    string_2 = string.replace(" ","")
                    webbrowser.open(string_2)
                    
            elif 'time' in query:
                strtime = datetime.datetime.now().strftime("%H:%M")
                Speak(f"Sir, the time is {strtime}")
                
            elif 'go to location' in query:
                Speak('What is the location?')
                location = takecommand().lower()
                url = 'https://google.nl/maps/place/' + location + '/&amp;'
                webbrowser.open_new_tab(url)
                Speak('Here is the location ' + location)
            
            if 'pause' in query:
                 press_and_release('space bar')

            elif 'restart' in query:
                press_and_release('0')

            elif 'mute' in query:
                press_and_release('m')

            elif 'skip' in query:
                press_and_release('l')

            elif 'back' in query:
                press_and_release('j')

            elif 'full screen' in query:
                press_and_release('f')

            elif 'film mode' in query:
                press_and_release('t')
                
            # elif 'chrome' in query:
            #     query = query.replace("run", "")
            # # query = query.replace("delta", "")
            # press("super")
            # write(query)
            # sleep(2)
            # press("enter")
                
            elif "click my photo" in query:
                press("super")
                sleep(2)
                write("camera")
                sleep(2)
                press("enter")
                sleep(2)
                Speak("Say Cheeze..!")
                press("enter")
                sleep(2)
                click(x=1888, y=19)
            
            elif 'youtube search' in query:
                Speak("OK sIR , This Is What I found For Your Search!")
                query = query.replace("delta", "")
                query = query.replace("youtube search", "")
                web = 'https://www.youtube.com/results?search_query=' + query
                webbrowser.open(web)
                Speak("Done Sir!")
            
            elif 'find my phone' in query or 'locate my phone' in query or 'trace my phone' in query:
                webbrowser.open("https://www.google.com/android/find?hl=en&hl=en&did=_KcmB44NKpintD70F42bMDDu4qhYX6OEWQ7VgeVg8xk%3D&continue=https://myaccount.google.com/?hl%3Den%26utm_source%3DOGB%26utm_medium%3Dact&u=0")
                Speak("Wait a second sir, i am Searching.....")
                print("Wait a second sir, i am Searching.....")
                sleep(2)
                click(x=246, y=489)
                sleep(2)
                click(x=226, y=729)
                sleep(2)
                pyautogui.hotkey('alt', 'f4')
                
taskExe()