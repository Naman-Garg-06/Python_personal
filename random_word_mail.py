# https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts
# https://stackoverflow.com/questions/24518522/run-python-script-at-startup-in-ubuntu

import random,time,datetime,smtplib
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# word extractiom using Selenium
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#driver.set_page_load_timeout(10)
driver.get('https://randomword.com/')
# driver.find_element_by_name('q').send_keys("random word from dictionary"+"\n")
word = driver.find_element_by_id('random_word').text
word_meaning = driver.find_element_by_id('random_word_definition').text
driver.close()

# mailing the word to the recievers.
x = datetime.datetime.now()             # 2021-10-01 23:52:30.379660
x = str(x).split()[1]                   # date-time format
x = x.split('.')[0].split(':')          # only interested in hours, minutes and seconds

hour = int(x[0])
minutes = int(x[1])
seconds = int(x[2])
if (True):
    sender = 'garg.naman0607@gmail.com'
    reciever = ['17ucs097@lnmiit.ac.in','gargnitish678@gmail.com','17ucs178@lnmiit.ac.in']
    random_text = "This mail is just an execution of an idea. The idea is to get a random word online, using SELENIUM library. Then using SMTP library, e-mail this word and its meaning to a list of recipients. Sent from Linux terminal using python.\n\n"
    message = "NEW RANDOM WORD :: " + word + ": " + word_meaning

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('garg.naman0607@gmail.com', 'highlyconfidential')

    try:
        
        smtpObj.sendmail(sender,reciever,random_text+message)
        print("Mail sent.")
    except:
        print("Error")
