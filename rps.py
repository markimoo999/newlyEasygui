import random
import easygui
import time
easygui.msgbox( "hey! let's play rock paper scissors!")
options = ["rock", "paper", "scissors"]
i=0
while i<5:
    cominput = random.choice(options)
    myinput = easygui.enterbox("rock, paper, scissors,")
    if myinput=="scissors" and cominput=="rock":
        easygui.msgbox( "SHOOT! ...HA! I did rock! I win!!!")
        time.sleep(3)
        easygui.msgbox("let's play again!")
        time.sleep(3)
    elif myinput=="rock" and cominput=="paper":
        easygui.msgbox( "SHOOT! ...HA! I did paper! I win!!!")
        time.sleep(3)
        easygui.msgbox( "let's play again!")
        time.sleep(3)
    elif myinput=="paper" and cominput=="scissors":
        easygui.msgbox( "SHOOT! ...HA! I did scissors! I win!!!")
        time.sleep(3)
        easygui.msgbox( "let's play again!")
        time.sleep(3)
    elif myinput=="paper" and cominput=="rock":
        easygui.msgbox( "SHOOT!...DANG! I did rock. You win.")
        time.sleep(3)
        easygui.msgbox( "let's play again!")
        time.sleep(3)
    elif myinput=="scissors" and cominput=="paper":
        easygui.msgbox( "SHOOT!...DANG! I did paper. You win.")
        time.sleep(3)
        easygui.msgbox("let's play again!")
        time.sleep(3)
    elif myinput=="rock" and cominput=="scissors":
        easygui.msgbox("SHOOT!...DANG! I did scissors. You win.")
        time.sleep(3)
        easygui.msgbox("let's play again!")
        time.sleep(3)
    elif myinput=="rock" and cominput=="rock":
        easygui.msgbox( "SHOOT!...Welp, we did the same thing.")
        time.sleep(3)
        easygui.msgbox( "let's play again!")
        time.sleep(3)
    elif myinput=="scissors" and cominput=="scissors":
        easygui.msgbox( "SHOOT!...Welp, we did the same thing.")
        time.sleep(3)
        easygui.msgbox( "let's play again!")
        time.sleep(3)
    elif myinput=="paper" and cominput=="paper":
        easygui.msgbox( "SHOOT!...Welp, we did the same thing.")
        time.sleep(3)
        easygui.msgbox( "let's play again!")
        time.sleep(3)
    i = i + 1
easygui.msgbox( "Actually, you know what, that's it. i'm done.")
