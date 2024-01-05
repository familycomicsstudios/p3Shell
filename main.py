### AT THE END I WILL MAKE THE FINAL VERDICT OF HOW GOOD THIS CODE IS ###

"""
p3Shell v0.1.0
A universal shell with plugins
"""
###### IMPORTS ######
import sys
import os
import subprocess # wait what i am curious why do you need this? ill see later in the code
import json


config = {
    "chdircmds": ["cd", "chdir"], # I don't see a reason to make an alias system, in the Custom CMD api you can create your own aliases by just making the command execute other commands with the API.
    "CTRL_C_EXIT": False,
    "STARTING_DIRECTORY": os.path.expanduser('~'),
    "PROMPT": "os.getcwd()+\" p3> \"", # Nice idea for customizing the prompt, I will add that to my own
    "COMMANDS": {
    } # No Point of that if you already have the loadedCommands thing, right?  Either way this one confuses me
}

loadedCommands = {
    "p3CommandTest": "echo Hello!" # I'd recommmend making a Command class, and having the custom commands list be static.
}

# If you want to make a loadedCommands list, here's the changes I'd make
def sayHi():
    print("Hello!")
myLoadedCommands = {
    "p3CommandTest": lambda:print("Hello!"), # The difference is that you can do a LOT more with python functions than batch
    "p3CommandTestOther": sayHi # If you want to make a more complex command you can also do this
}

__version__ = "0.1.0" # NOOOO DON"T DO THAT CONST VARIABLES SHOULD NEVER BE LIKE THIS
VERSION = "0.1.0" # Here's the correct naming case

class PromptError: # What?  Either way if you wanted to make a custom exception I guess you could do this by doing class PromptError(Exception)
    pass

def loadConfig(): # ok fine just steal my code, and don't even give credit i see how it goes
    print("Loading .p3shellconfig file from home directory...")
    homepath = os.path.expanduser('~') + "\\"
    path = homepath + ".p3shellconfig"
    try:
        with open(path, encoding='utf-8') as c:
            c = json.load(c)
            for v in config:
                if v in c: config[v] = c[v]
    except FileNotFoundError:
        with open(path, "w+", encoding='utf-8') as f:
            json.dump(config, f)
    except Exception as error:
        print(error)
        os.system('pause')

def addInstalledCommands(): # There's no point of having it in the command list if you need to edit the code to give it an action, lol
    for command in config["COMMANDS"].keys():
        loadedCommands[command] = config["COMMANDS"][command]

def processCommandAlt(commandRaw): # Did you just steal a lot of my code??
    cmdSplit = commandRaw.split(" ")
    try:
        if cmdSplit[0] in config["chdircmds"]:
            os.chdir(" ".join(cmdSplit[1:]))
        else:
            print(subprocess.run(cmdSplit, shell=True, capture_output=True).stdout.decode("utf-8")) # Why make that?  Just do a ternary operator

    except Exception as error: 
        print(error) # I'm honestly disappointed.  For non tech savvy users they might not understand what is happening, but if you use an fstring with some extra details like "Error" then it is WAY easier to understand what is happening

def processCommand(commandRaw): # Honestly, I like the change to rename it to commandRaw, but i'd personally name it raw_command because python uses snake case, the case you used is more for other languages
    cmdSplit = commandRaw.split(" ")
    try:
        if cmdSplit[0] in config["chdircmds"]:
            os.chdir(" ".join(cmdSplit[1:]))
        elif cmdSplit[0] == "exit":
            print("exit")
            sys.exit()
        elif cmdSplit[0] in loadedCommands.keys(): # the way you did this makes it useless. jsut make a command class
            os.system(loadedCommands[cmdSplit[0]])
        else:
            os.system(commandRaw)
    
    #is this just my code? meh it's ok i guess

    except Exception as error:
        print(error)

def main():
    print("p3shell v"+__version__+" by Themadpunter") # I like the idea of printing info about it
    loadConfig()
    addInstalledCommands()

    online = True
    os.chdir(config["STARTING_DIRECTORY"])
    
    while online:
        try:
            prompt = eval(config["PROMPT"])
        except:
            raise PromptError # Nothing to raise, this doesn't work I don't think because it isn't derived from the Exception class
        try:
            sys.path.append(os.getcwd())
            commandRaw = input(prompt)
            processCommand(commandRaw)
            # processCommandAlt(commandRaw) # Uses subprocess.run, not recommended for most platforms
            # Glad you know it isn't recommended LOL
        except KeyboardInterrupt:
            if config["CTRL_C_EXIT"]: sys.exit()
            print()

if __name__ == "__main__": # I see why you would do this to make the program more simple, personally I need some things to be ran outside of this for purposes like the API
    main()
    
### FINAL VERDICT
    
# I believe your code is extremely flawed, but has great potential. 
    
# The configuration system is purely copied from mine, and the command system is a 10x worse system than mine.  It has an awful naming convention, and bad systems that aren't necessary or useful
    
# On the other side, the things you did well are the idea of the PromptError, except I don't believe it works as you didn't derive it from the Exception class but if you do you have great potential for a custom error handling system, and it would end up great.
    
# Naming Convention: 2.6/10
# Unnecessary Code: 6/10
# The Amount of Original, Not Copied Code: 6.3/10
# Working Code: 8.8/10
# User Friendly (Non Technical): 7.3/10
# User Friendly (More Technical like Config System): 5.5/10
