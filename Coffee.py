import pyttsx3
from time import sleep

Erik = str(100)
Ciaran = str(200)
Daniel = str(9999)

engine = pyttsx3.init()

def Timer():
    engine.say("you have;; 30;; seconds to to make a coffee before your credits are seized")
    sleep(10)
    engine.say("you have;; 20;; seconds to to make a coffee before your credits are seized")
    sleep(10)
    engine.say("you have;; 10;; seconds to to make a coffee before your credits are seized")
    sleep(5)
    engine.say("you have;; 5;; seconds to to make a coffee before your credits are seized")
    sleep(1)
    engine.say("you have;; 4;; seconds to to make a coffee before your credits are seized")
    sleep(1)
    engine.say("you have;; 3;; seconds to to make a coffee before your credits are seized")
    sleep(1)
    engine.say("you have;; 2;; seconds to to make a coffee before your credits are seized")
    sleep(1)
    engine.say("you have;; 1;; seconds to to make a coffee before your credits are seized")
    

while True:
    name = input("Name: ")
    name = name.capitalize()

    if name=="Erik":
        engine.say("you have;;" + Erik + ";credits")
    
    elif name=="Ciaran":
        engine.say("you have;;" + Ciaran + ";credits")
    
    elif name=="Daniel":
        engine.say("you have;;" + Daniel + ";credits")
    
    elif name=="Eliminate":
        engine.say("understood;; you have;; 5;; seconds to surrender")
        sleep(1)
        engine.say("you have;; 4;; seconds to surrender")
        sleep(1)
        engine.say("you have;; 3;; seconds to surrender")
        sleep(1)
        engine.say("you have;; 2;; seconds to surrender")
        sleep(1)
        engine.say("you have;; 1;; seconds to surrender")
        sleep(1)
        engine.say(";;; oh;;;; you called my bluff")
    
    else:
        engine.say("I do not recognise;;" + name + ";;in my data; please report this if you think that is a mistake")

    engine.runAndWait()
