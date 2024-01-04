"""
p3Shell v0.1.0
A universal shell with plugins
"""
# Start Imports
import sys
import os
import subprocess
import json
# End imports
config = {
    "chdircmds": ["cd", "chdir"],
    "CTRL_C_EXIT": False,
    "STARTING_DIRECTORY": os.path.expanduser('~'),
    "PROMPT": "os.getcwd()+\" p3> \"",
    "COMMANDS": {
    }
}

loadedCommands = {
    "p3CommandTest": "echo Hello!"
}

class PromptError:
    pass

def loadConfig():
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

def addInstalledCommands(binDir):
    for command in config["COMMANDS"].keys():
        loadedCommands[command] = config["COMMANDS"][command]

def processCommandAlt(commandRaw):
    cmdSplit = commandRaw.split(" ")
    try:
        if cmdSplit[0] in config["chdircmds"]:
            os.chdir(" ".join(cmdSplit[1:]))
        else:
            print(subprocess.run(cmdSplit, shell=True, capture_output=True).stdout.decode("utf-8"))

    except Exception as error:
        print(error)

def processCommand(commandRaw):
    cmdSplit = commandRaw.split(" ")
    try:
        if cmdSplit[0] in config["chdircmds"]:
            os.chdir(" ".join(cmdSplit[1:]))
        elif cmdSplit[0] == "exit":
            print("exit")
            sys.exit()
        elif cmdSplit[0] in loadedCommands.keys():
            os.system(loadedCommands[cmdSplit[0]])
        else:
            os.system(commandRaw)

    except Exception as error:
        print(error)

def main():
    loadConfig()
    print("p3Shell")

    online = True
    os.chdir(config["STARTING_DIRECTORY"])
    
    while online:
        try:
            prompt = eval(config["PROMPT"])
        except:
            raise PromptError
        try:
            sys.path.append(os.getcwd())
            commandRaw = input(prompt)
            processCommand(commandRaw)
            # processCommandAlt(commandRaw) # Uses subprocess.run, not recommended for most platforms
        except KeyboardInterrupt:
            if config["CTRL_C_EXIT"]: sys.exit()
            print()

if __name__ == "__main__":
    main()
    
