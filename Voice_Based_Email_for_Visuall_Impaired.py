import speech_recognition as sr
from playsound import playsound
import speech_recognition as sr
import smtplib
import pyaudio
import platform
import sys
from bs4 import BeautifulSoup
import email
import imaplib
from gtts import gTTS
import pyglet
import os, time
print("-" * 60)
print(" Project: Voice based Email for Visually impaired")
print(" <--Created by SYSTEM TRON-->")
print("-" * 60)
# project name
tts = gTTS(text="Project: Voice based Email for Visually impaired", lang='en')
ttsname = ("~tempfile01.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
# login from os
login = os.getlogin
print("You are logging from : " + login())
# choices
print("1. composed a mail.")
tts = gTTS(text="option 1. composed a mail.", lang='en')
ttsname = ("~tempfile01.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
print("2. Check your inbox")
tts = gTTS(text="option 2. Check your inbox", lang='en')
ttsname = ("~tempfile01.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
# this is for input choices
tts = gTTS(text="Your choice ", lang='en')
ttsname = ("~tempfile01.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
# voice recognition part
def Speech_to_text():
    """
    Speech to text
    Returns:
        str: Returns transcripted text
    """

r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Your choice:")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print("ok done!!")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service;{0}".format(e))
# choices details
if text == '1' or text == 'One' or text == 'one':
 r = sr.Recognizer() # recognize
try:
     with sr.Microphone() as source:
        print("Your message :")
        audio = r.listen(source)
        print("ok done!!")
        text1 = r.recognize_google(audio)
        print("You said : " + text1)
        msg = text1
        tts = gTTS(text="Your messag" + text1, lang='en')
        ttsname = ("~tempfile01.mp3")
        tts.save(ttsname)
        music = pyglet.media.load(ttsname, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(ttsname)
except sr.UnknownValueError:
 print("Google Speech Recognition could not understand audio.")
except sr.RequestError as e:
 print("Could not request results from Google Speech Recognition service;{0}".format(e))
mail = smtplib.SMTP('smtp.gmail.com', 587) # host and port area
mail.ehlo() # Hostname to send for this command defaults to the FQDN of the local host.
mail.starttls() # security connection
mail.login('kushalnayak82@gmail.com', 'saniha@123') # login part
mail.sendmail('kushalnayak82@gmail.com', 'reciver@gmail.com', msg) # send part
print("Congrates! Your mail has been sent. ")
tts = gTTS(text="Congrates! Your mail has been sent. ", lang='en')
ttsname = ("~tempfile01.mp3")
tts.save(ttsname)
music = pyglet.media.load(ttsname, streaming=False)
music.play()
time.sleep(music.duration)
os.remove(ttsname)
mail.close()

if text == '2' or text == 'tu' or text == 'two' or text == 'Tu' or text == 'to' or text == 'To' :
 mail = imaplib.IMAP4_SSL('imap.gmail.com', 993) # this is host and port area.... ssl security
 unm = ('your mail/ victim mail') # username
 psw = ('pswrd') # password
 mail.login(unm, psw) # login
 stat, total = mail.select('Inbox') # total number of mails in inbox
 print("Number of mails in your inbox :" + str(total))
 tts = gTTS(text="Total mails are :" + str(total), lang='en') # voice out
 ttsname = ("~tempfile01.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
 # unseen mails
 unseen = mail.search(None, 'UnSeen') # unseen count
 print("Number of UnSeen mails :" + str(unseen))
 tts = gTTS(text="Your Unseen mail :" + str(unseen), lang='en')
 ttsname = ("~tempfile01.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
 # search mails
 result, data = mail.uid('search', None, "ALL")
 inbox_item_list = data[0].split()
 new = inbox_item_list[-1]
 old = inbox_item_list[0]
 result2, email_data = mail.uid('fetch', new, '(RFC822)') # fetch
 raw_email = email_data[0][1].decode("utf-8") # decode
 email_message = email.message_from_string(raw_email)
 print("From: " + email_message['From'])
 print("Subject: " + str(email_message['Subject']))
 tts = gTTS(text="From: " + email_message['From'] + " And Your subject: " + str(email_message['Subject']), lang='en')
 ttsname = ("~tempfile01.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
 # Body part of mails
 stat, total1 = mail.select('Inbox')
 stat, data1 = mail.fetch(total1[0], "(UID BODY[TEXT])")
 msg = data1[0][1]
 soup = BeautifulSoup(msg, "html.parser")
 txt = soup.get_text()
 print("Body :" + txt)
 tts = gTTS(text="Body: " + txt, lang='en')
 ttsname = ("~tempfile01.mp3")
 tts.save(ttsname)
 music = pyglet.media.load(ttsname, streaming=False)
 music.play()
 time.sleep(music.duration)
 os.remove(ttsname)
 mail.close()
 mail.logout()
