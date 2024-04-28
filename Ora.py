import time
import os

DIGITS = [
	[" ┏━┓ ", "  ╻  ", " ┏━┓ ", " ┏━┓ ", " ╻ ╻ ", " ┏━┓ ", " ┏   ", " ┏━┓ ", " ┏━┓ ", " ┏━┓ ", "   "],
	[" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", " ╻ "],
	[" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┏━┛ ", " ┣━┫ ", " ┗━┫ ", " ┗━┓ ", " ┣━┓ ", "   ┃ ", " ┣━┫ ", " ┗━┫ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ╹ "],
	[" ┗━┛ ", "  ╹  ", " ┗━━ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   "],
] # [7][11] mátrix

### IGAZÍTÁS ###
X = 1
Y = 1

def clear():
    os.system("cls")
    
def separate(numbers):
    tizes = numbers // 10
    numbers = numbers % 10
    egyes = numbers // 1
    return [tizes,egyes]
     
def get_digit(h1,h2,m1,m2,s1,s2):
    i=0
    spaces = os.get_terminal_size()
    if Y==1:
        h = 0                           #Y tengelyen középre igazítás
        while h < (spaces[1]-7)//2: 
            print("\n",end="")
            h+=1
        
    while i < 7: 
        if X == 1:
            w = 0                       #X tengelyen középre igazítás
            while w < (spaces[0]-33)//2: 
                print(" ",end="")
                w+=1
        print(DIGITS[i][h1] + DIGITS[i][h2] + DIGITS[i][10] + DIGITS[i][m1] + DIGITS[i][m2] + DIGITS[i][10] + DIGITS[i][s1] + DIGITS[i][s2] + "\n",end = "")
        i+=1
    
def main():
    while True:
        t = time.localtime()
        hour = separate(t.tm_hour)
        minute = separate(t.tm_min)
        second = separate(t.tm_sec)
        get_digit(hour[0],hour[1],minute[0],minute[1],second[0],second[1])
        print('\033[?25l', end="") #eltünteti a cursor-t [vissza ===> print('\033[?25h', end="")]
        time.sleep(1)
        clear()       #innen lefelé már csak a main meghívása és komment van számomra
        '''
        localtime():

        tm_year=2022
        tm_mon=10
        tm_mday=18
            tm_hour=8
            tm_min=52
            tm_sec=35
        tm_wday=1
        tm_yday=291
        tm_isdst=1
        '''

if __name__ == '__main__':
    main()