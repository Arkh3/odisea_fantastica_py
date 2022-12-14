import keyboard
import yaml
import os

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios    #for linux/unix
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def captureKeys(keys):
    exit = False
    ret = None

    while not exit:
        event = keyboard.read_event()
        
        if event.event_type == keyboard.KEY_DOWN and event.name in keys:
            exit = True
            ret = event.name

    return ret

def loadYaml(file_path):
    with open(file_path, "r", encoding="utf8") as stream:
        try:
            parameters = yaml.safe_load(stream)
        except yaml.YAMLError:
            parameters = None

    return parameters

def storeYaml(dictionary, file_path):
    with open(file_path, 'w') as outfile:
        yaml.dump(dictionary, outfile, default_flow_style=False)

def menu(menuHeader, options, markedOption=None, confirmOptions=None):
    MIN_OPTION = 0
    MAX_OPTION = len(options) -1

    if (markedOption is None) or (markedOption not in options):
        option = 0
    else:
        option = options.index(markedOption)

    exit = False

    while not exit:
        os.system('cls')
        print(menuHeader)

        for i in range(len(options)):
            if i == option:
                print("  - " + options[i] + " <")
            else:
                print("  - " + options[i])

        capturedKey = captureKeys(['up', 'down', 'enter'])

        if capturedKey == 'up':
            option -= 1
            if option < MIN_OPTION:
                option = MAX_OPTION

        elif capturedKey == 'down':
            option += 1
            if option > MAX_OPTION:
                option = MIN_OPTION

        elif capturedKey == 'enter':
            if confirmOptions is not None and options[option] in confirmOptions:
                confirm = menu("¿Seguro que quieres '" + options[option] + "'?\n", ['Si', 'No'])

                if confirm == 'Si':
                    exit = True
            else: 
                exit = True

    return options[option]