#!/data/data/com.termux/files/usr/bin/python

from argparse import ArgumentParser as AP
from time import sleep

ap = AP(description="A simple program to simulate animated typing effect like Typer.JS")

ap.add_argument('-delay',type=int,default=100,help='Time delay between typed characters (in ms)')
ap.add_argument('-delete_delay',type=int,default=50,help='Time delay between deleted characters (in ms)')
ap.add_argument('-words_delay',type=int,default=800,help='Time delay between typed words (in ms)')
ap.add_argument('-start',type=str,default='',help='The starting word or sentence')

ap.add_argument('words',type=str,nargs='+',help='The words to be typed')

args = ap.parse_args()

print(args.start,end='')

words = args.words

for i in range(len(words)):
    word = words[i]
    for x in word:
        print(x,end='',flush=True)
        sleep(args.delay / 1000)
    sleep(args.words_delay / 1000)
    if not i == len(words) - 1:
        for y in word:
            print('\b \b',end='',flush=True)
            sleep(args.delete_delay / 1000)
print()
