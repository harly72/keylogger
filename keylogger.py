from pynput import keyboard 
import datetime #add
import os
 

def keyPressed(key): 
    file_path = 'study/keylife.txt'#if error run in study environment
    if os.path.exists(file_path):
        os.remove(file_path)
        print("oh no.. the file was deleted! Yay!")
    
    print(str(key))
    time_now_1 = datetime.datetime.now()
    timestamp_now = datetime.datetime.timestamp(time_now_1)
    #time_now = datetime.datetime.timestamp().now # useless
    with open("study/keyfile.txt", 'a') as logkey:# appending key to the first line in keyfile
        try:
            char = key.char
            logkey.write(f"{char}, {timestamp_now}\n")# we need to add while loop for analyser.py
        except AttributeError:
            print(AttributeError)

if __name__ == "__main__": 
    listener = keyboard.Listener(on_press=keyPressed)#Creating the listener 
    listener.start()
    input() # takes key presses endlessly