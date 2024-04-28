import sys
import time
import os
import pygame

h_param = ''' 
Parameters:

    -h                  this help
    -p, -p2, -p3        play the sound effect (for adjusting the volume)
    <time>              where time can be given in different formats, e.g.
                        60    -> 60 seconds
                        60s   -> 60 seconds
                        1m    -> 1 minute
                        1m10s -> 1 minute and 10 seconds
                        1h5m  -> 1 hour and 5 minutes'''
    
def clear():
    os.system("cls")
    
def r(szam):
    if len(str(szam))==1: return "0" + str(szam)
    return str(szam)

def get_time(seconds):
    hours = seconds//3600
    seconds = seconds%3600
    minutes = seconds//60
    seconds = seconds%60
    return [hours,minutes,seconds]

def countdown(seconds):
    clear()
    while seconds>=0:
        szamok = get_time(seconds)
        h,m,s = r(szamok[0]),r(szamok[1]),r(szamok[2])
        print(f"Time: {h}:{m}:{s}")
        print("\x1b[?25l") #cursor eltüntetése
        time.sleep(1)
        clear()
        seconds-=1  
    
def play_for(szam,filenev):
    pygame.mixer.init()
    pygame.mixer.music.load(filenev)
    file_hossz = 1
    #file_hossz = 9
    for i in range(szam):
        pygame.mixer.music.play()
        time.sleep(file_hossz)
        pygame.mixer.music.stop()
 
def get_total(s):
    total = 0
    if "h" in s: total += 3600* int(s[0:s.find("h")])        
    if "m" in s and "h" in s: total += 60* int(s[s.find("h")+1:s.find("m")]) 
    elif "m" in s: total += 60* int(s[0:s.find("m")])
    if "s" in s and "m" in s: total += int(s[s.find("m")+1:-1])
    elif "s" in s and "h" in s: total += int(s[s.find("h")+1:-1])
    elif "s" in s: total += int(s[0:-1])
    return total

def main():
    filenev = "error.mp3"  # 1 sec
    #filenev = "what.mp3"  # 9 sec
    
    if len(sys.argv)==1: print("\nSegítségért használd a -h paramétert!\n")
    elif len(sys.argv)==2:
        if (sys.argv[1][0:1]).isdigit() and ("h" in sys.argv[1] or "m" in sys.argv[1] or "s" in sys.argv[1]):
            countdown(get_total(sys.argv[1]))
            play_for(2,filenev)
            
        elif (sys.argv[1][0:1]).isdigit():    
            seconds = int(sys.argv[1])
            countdown(seconds)
            play_for(2,filenev)
        
        elif sys.argv[1] == "-h":
            print(h_param)
            sys.exit(0)
            
        elif sys.argv[1] == "-p" or "-p2" or "-p3":
            repeat = 0
            if sys.argv[1] == "-p": repeat = 1
            if sys.argv[1] == "-p2": repeat = 2
            if sys.argv[1] == "-p3": repeat = 3
            play_for(repeat,filenev)
            sys.exit(0)
    else: print("Hibás paraméterezés!")
        
if __name__ == "__main__":
    main()