#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def game_over():
     print("\nDo you want to play again? (y or n)")
     answer = input(">").lower()
     if "y" in answer:
            start()
     
     else:
            exit()
def princess_Cell():
    print("You made to the princess")
    print("She is so happy to see you...")
    print("She pulled you into a tight hug")
    print("After sharing the moment you both make preparations to escape ")
    print("You have 3 ways to go back")
    print("Choose wisely")
    print("1: GO through the main exit")
    print("2: GO back via the House of ogres")
    print("3: GO back via the dragon Room")
    answer=input('>').lower()
    if  answer=='1':
        print("The army was all prepared to attack you ,you had no option but surrender ")
        print("The princess has been recaptured but she will live and you have been prisoned on the charges of being a spy and to be beheaded tommorow")
        game_over()
    elif answer=='2':
        print("are you out of your mind ! its a big ass dragon . You and the princess got turned to cinders in 2 seconds")
        game_over()
    elif answer=='3':
        print("The ogres have caught you both") , 
        print("the princess begs for your life. The Ogres let you go and keep the pricess and eat her ")
        print("You will live ")
        game_over()
    else:
        print("Game over! Press the right button you nitwit")
        game_over()
def Dragon_Room():
    print ("Welcome to the dragon room")
    print ("there is a door in front of you that leads you to the princesses cell")
    print("The Dragon is Currently sleeping")
    print("Be carefull not to wakeup the dragon")
    print("Choose wisely")
    print("What do you do (select 1 and 2 according to what you wish to do")
    print("1: Tip toe slowly to the princess cell and ignore the treasures")
    print("2: Fight the dragon for the treasure ")
    answer=input('>').lower()
    if  answer=='1':
        print("Good job you made your way to the princess cell")
        princess_Cell()
    elif answer=='2':
        print("are you out of your mind ! its a big ass dragon . You got turned to cinders in 2 seconds")
        game_over()
    else:
        print("Game over! Press the right button you nitwit")
        game_over()
def Ogre_Room():
    print("welcome to the House of ogres")
    print("there is a door in front of you that leads you to the princesses cell")
    print("The Room is dark with tainted windows as the ogres dont like sunlight")
    print("Be carefull not to piss them off they can smash you to pieces ")
    print("Tip toeing slowly........")
    print ("Oh no ! the ogres have seen you")
    print("What do you do (select 1 and 2 according to what you wish to do )")
    print("Choose wisely")
    print("1: Fight the Ogres ")
    print("2: Break the tainted glass windows ")
    answer=input('>').lower()
    if  answer=='1':
        print("You fought courageously but died as the ogres were too strong for you")
        game_over()
    elif answer=='2':
        print("Good job the ogres got distracted and you sprinted through escaping to the princess cell")
        princess_Cell()
    else:
        print("Game over! Press the right button you nitwit")
        game_over()
def start():
    print("Your are at the start point")
    print("Your Journey begins ")
    print("You have to find the exit... ")
    print("in front of you there are 2 rooms")
    print("press l to go to the left room and press r to go to the right room")
    answer=input('>').lower()
    if "l" in answer:
         Ogre_Room()
    elif "r" in answer:
         Dragon_Room()
    else:
        game_over()
        print("game over! press the right button you nitwit!")

start()


# In[ ]:




