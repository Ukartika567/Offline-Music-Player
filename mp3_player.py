
import os 
from playsound import playsound

file_dir = '/home/amantya/Downloads/'
song = ['Ye Ladki Pagal Hai Badsah Dj Remix Song(KoshalWorld.Com).mp3',  'She Move It Like (Remix) _ DJ Scopio Dubai X DJ Kimi Dubai(KoshalWorld.Com).mp3']

def print_message():
    print('-------------------Welcome to the **Rock On** Music--------------')
    print('\n')

    print('--> Hey!Dude, press s to start a  Rock On music')
    flag = input()
    return flag



def startMusic():
    while True:
        try:
            inp = int(input('Hey! Dude : \n  Whose song will you want to hear?? \n    1 for Badshaah & \n       2 for Honey Singh\n'))
            
            if inp not in [1,2]:
                print('Sorry! Dude , Now We have only 2 songs , so plz enter a valid key which is given in playlist \n')
                continue

            if inp == 1:
                playsound(file_dir + song[0])


            if inp == 2:
                playsound(file_dir + song[1])


        except Exception as e:
            print('Oops! Please enter a valid key to play the song\n ')    



flag = print_message()         
if flag == 's' or flag == 'S':
    startMusic()
else:    
    while not (flag == 'q' or flag == 'Q' or flag == 's' or flag == 'S'):
        flag=input("Hey! It's wrong , plz press s & come on *Rock On* Music because we are waitting for you . \n 1. 'q' for quit & \n 2. 's' for start. \n ")
            
        if flag == 's' or flag == 'S':
            startMusic()    
        if  flag == 'q' or flag == ' Q':
            exit()


    


