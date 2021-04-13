#dot is 0.25 sec
#dash is 0.75 sec
#space between letters is 0.75 sec
#space between words is 1.75 sec
#do not use capital letters

from gpiozero import Buzzer
from time import sleep
bz = Buzzer(17)
def dot():
    bz.on()
    sleep(0.25)
    bz.off()
    sleep(0.25)
def dash():
    bz.on()
    sleep(0.75)
    bz.off()
    sleep(0.25)
def end():
    sleep(0.5)
def morse(str):
    for i in range(0, len(str), 1):
        x = str[i:i+1]
        if x == 'a':
            dot()
            dash()
            end()
        elif x == 'b':
            dash()
            dot()
            dot()
            dot()
            end()
        elif x == 'c':
            dash()
            dot()
            dash()
            dot()
            end()
        elif x == 'd':
            dash()
            dot()
            dot()
            end()
        elif x == 'e':
            dot()
            end()
        elif x == 'f':
            dot()
            dot()
            dash()
            dot()
            end()
        elif x == 'g':
            dash()
            dash()
            dot()
            end()
        elif x == 'h':
            dot()
            dot()
            dot()
            dot()
            end()
        elif x == 'i':
            dot()
            dot()
            end()
        elif x == 'j':
            dot()
            dash()
            dash()
            dash()
            end()
        elif x == 'k':
            dash()
            dot()
            dash()
            end()
        elif x == 'l':
            dot()
            dash()
            dot()
            dot()
            end()
        elif x == 'm':
            dash()
            dash()
            end()
        elif x == 'n':
            dash()
            dot()
            end()
        elif x == 'o':
            dash()
            dash()
            dash()
            end()
        elif x == 'p':
            dot()
            dash()
            dash()
            dot()
            end()
        elif x == 'q':
            dash()
            dash()
            dot()
            dash()
            end()
        elif x == 'r':
            dot()
            dash()
            dot()
            end()
        elif x == 's':
            dot()
            dot()
            dot()
            end()
        elif x == 't':
            dash()
            end()
        elif x == 'u':
            dot()
            dot()
            dash()
            end()
        elif x == 'v':
            dot()
            dot()
            dot()
            dash()
            end()
        elif x == 'w':
            dot()
            dash()
            dash()
            end()
        elif x == 'x':
            dash()
            dot()
            dot()
            dash()
            end()
        elif x == 'y':
            dash()
            dot()
            dash()
            dash()
            end()
        elif x == 'z':
            dash()
            dash()
            dot()
            dot()
            end()
        else:
            sleep(1.75)

while True:
  morse(input("enter:"))
  print('')

