# modules
import pyttsx3
from time import sleep

# variables for how much starting points people have
Erik = str(100)
Ciaran = str(100)
Daniel = str(100)

# gets the TTS engine ready
engine = pyttsx3.init()

# loop for the actual username and pass
while True:
    # asks for the username
    name = input("Name: ")
    # ignores capitalization
    name = name.capitalize()

    # if the input was Erik runs code
    if name == "Erik":
        # asks for password
        password = input("password: ")
        # if the input password is "ABC123" it runs TTS
        if password == "ABC123":
            engine.say("you have;;" + Erik + ";credits")
        # else it will say that the password does not match the username
        else:
            engine.say("Your password does not match the username of;;" +
                       name + ";; please contact admin if you think this is a mistake")

    # if the input was Ciaran runs code
    elif name == "Ciaran":
        # asks for password
        password = input("password: ")
        # if the input password is "ABC123" it runs TTS
        if password == "ABC123":
            engine.say("you have;;" + Ciaran + ";credits")
        # else it will say that the password does not match the username
        else:
            engine.say("Your password does not match the username of;;" +
                       name + ";; please contact admin if you think this is a mistake")

    # if the input was Ciaran runs code
    elif name == "Daniel":
        # asks for password
        password = input("password: ")
        # if the input password is "ABC123" it runs TTS
        if password == "ABC123":
            engine.say("you have;;" + Daniel + ";credits")
        # else it will say that the password does not match the username
        else:
            engine.say("Your password does not match the username of;;" +
                       name + ";; please contact admin if you think this is a mistake")

    # if the username is not recognised it lets the user know
    else:
        engine.say("I do not recognise;;" + name +
                   ";;in my database; please report this if you think that is a mistake")

    # tells the TTS engine to run and wait for its que
    engine.runAndWait()
