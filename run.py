""" Modules allow random selection, colour, time delay and scores record """
import random
import colorama
import gspread
import time
import sys
from colorama import Fore
from time import sleep
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('HJ_Scoresheet')

scores_data = SHEET.worksheet('scores_data')
data = scores_data.get_all_values()

##############################################################
# (pre-story set up of code, & support for some functions


class Heroine:
    """ Character for user to be through the game """
    def __init__(self, name, fighting_spirit, self_esteem, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit
        self.self_esteem = self_esteem
        self.calories_to_burn = calories_to_burn

    def printStats_and_start(self): 
        # STARTS THE GAME AFTER PLAYER CHOOSES 'Y' in PART 3, line 408)
        """ Calls stats on player's choice of Heroine,""" 
        """ & starts the story (with a bus fight!)"""
        global heroine
        slow_read(f"\nYou have selected {self.name}.\n") 
        print()
        sleep(1)
        print(F"{Fore.BLUE}These are your stats: \n")
        print()
        sleep(1)
        print(f"\nfighting spirit - {self.fighting_spirit}")
        print(f"\nself esteem - {self.self_esteem}")
        print(f"\ncalories to burn - {self.calories_to_burn}\n \n")
        print()
        time.sleep(2)  
        Bus_Fight()
        """Heroine is taken to first part of the story"""

# heroine stats:


Demeter = Heroine("Demeter", 80, 80, 2800)

Persephone = Heroine("Persephone", 90, 50, 1500)

Athena = Heroine("Athena", 100, 90, 2000)

Lilith = Heroine("Lilith", 75, 40, 3500)

Roe = Heroine("Roe", 100, 95, 3000)


# opponents who appear in battles:

class Enemy:
    """ Enemy who reduces player's power through the game """
    def __init__(self, name, fighting_spirit, calories_to_burn):
        self.name = name
        self.fighting_spirit = fighting_spirit 
        self.calories_to_burn = calories_to_burn

# enemy stats


Kavanaugh = Enemy("Kavanaugh", 40, 2500)

Schlafly = Enemy("Schlafly", 60, 3000)

Trump = Enemy("Trump", 100, 3500)

# # # 


def slow_read(string):
    """ allows text to appear letter by letter in console """
    for x in string:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.2)

###################################################################
# STORY: start at the bottom of the page for part 1, & move up.
###################################################################

# PART EIGHT of EIGHT: FIGHT KAVANAUGH AT WORK. THE OFFICE IS UNSAFE!. THE END.


def Office():
    global heroine
    time.sleep(2)
    print(F"{Fore.WHITE}You walk to work carefully...")
    time.sleep(2)
    print("go through the revolving doors and into the office.")
    time.sleep(2)
    print(F"{Fore.LIGHTRED_EX}Your colleagues look nervous as they look up.")
    time.sleep(2)
    print(f"Someone whispers, '{heroine.name}...'")
    time.sleep(2)
    print("'We've got a new boss!'")
    time.sleep(2)
    print("'But what happened to our old one?', you ask.")
    time.sleep(2)
    print("'She got voted out in some kind of horrible takeover!'")
    time.sleep(2)
    print("'It all happened last night....'")
    time.sleep(2)
    print(F"{Fore.YELLOW}Everyone looks down as a man approaches.")
    time.sleep(2)
    time.sleep(2)
    print("He looks polite, and smiles kindly.")
    time.sleep(2)
    print(f"'Hi, {heroine.name}, my name is Kavanaugh...'")
    time.sleep(2)
    print("'I'm sorry, but you don't work here anymore.'")
    time.sleep(2)
    print("'But why?!' You ask.")
    time.sleep(2)
    print("'I went through hell to get here!!!'")
    time.sleep(2)
    print("He smiles nicely. 'Because my people like to get what they want,'")
    time.sleep(2)
    print(F"{Fore.LIGHTCYAN_EX}Suddenly, your workmate Conor stands up...")
    print("and throws a stapler at Kavanaugh's head.")
    time.sleep(2)
    print("Others join in. Your desk-neighbour Quinn throws a book at him...")
    time.sleep(2)
    print("(it's a copy of Tom Paine's 'The Rights of Man', of course)")
    time.sleep(2)
    print(F"{Fore.LIGHTGREEN_EX}And that was how the revolution started.")
    time.sleep(2)
    print(F"{Fore.LIGHTBLUE_EX}In the words of Charles Bukowski:")
    time.sleep(2)
    print(F"{Fore.WHITE}'There is a light somewhere...")
    time.sleep(2)
    print("it may not be much light but")
    time.sleep(2)
    print("it beats the darkness.'")

    print("""
    ______ _                             
   (_) |  | |                         |  
       |  | |     _     _   _  _    __|  
     _ |  |/ \   |/    |/  / |/ |  /  |  
    (_/   |   |_/|__/  |__/  |  |_/\_/|_/                            
                                       
    """)
    
    exit()


""" CREDS for script/ lettering in 'The End': 
Script by Glenn Chappell 4/93
Includes ISO Latin-1
figlet release 2.1 -- 12 Aug 1994
Permission is hereby given to modify this font, as long as the
modifier's name is placed on a comment line.

Modified by Paul Burton <solution@earthlink.net> 
12/96 to include new parameter
supported by FIGlet and FIGWin.  May also be slightly modified for better use
of new full-width/kern/smush alternatives, but default output is NOT changed.
from http://patorjk.com/ """

    
# PART SEVEN: IF PLAYER BEAT TRUMP, TREATS!! AND TIME TO GO TO WORK.


def treats():
    treats_list = [
        F"{Fore.MAGENTA}coffee", 
        F"{Fore.MAGENTA}smoothie", F"{Fore.MAGENTA}valium"]
    treat_rand = random.randint(0, 2)
    treat = treats_list[treat_rand]
    print(treat)
    print(F"{Fore.MAGENTA}Nice! :)")
    Office()
    """ Time to go to work!"""


# PART SIX - FIGHT TRUMP, OR NO FREE MEDICAL TREATMENT!


def Fight_Trump():
    global heroine
    """a fight for medical care"""
    time.sleep(2)
    print(F"{Fore.WHITE}You're feeling pretty damn good about yourself...")
    time.sleep(2)
    print("and you cross the road to a tall, glass building.")
    time.sleep(2)
    print("These are the offices where you work.")
    time.sleep(2)
    print("You push at the revolving door...")
    time.sleep(2)
    print("And bang your face. Someone pushed it in the opposite direction...")
    time.sleep(2)
    print(F"{Fore.LIGHTRED_EX}Blood streams from your nose. It feels broken.")
    time.sleep(2)
    print("Holding your nose, you run to the hospital.")
    time.sleep(2) 
    print("It's only a block away... and work would make you go anyway.")
    time.sleep(2)
    print("But at the main entrance to the emergency department...")
    time.sleep(2)
    print("stands a squarish, tanned man shaking his head.")
    time.sleep(2)
    print(f"'No free medical care for you, {heroine.name}.")
    time.sleep(2)
    print("'I've called the cops on you. Your insurance ran out years ago.'")
    time.sleep(2)
    print("Three black vans pull up by the hospital gate.")
    time.sleep(2)
    print("The men who get out...")
    time.sleep(2)
    print("They don't look like police officers, more like private security.")
    time.sleep(2)
    print(F"{Fore.GREEN}You have three options... ")
    time.sleep(2)
    choice = input(
        F"{Fore.BLUE}1. Use injustice_zapper \n2. Run! \n3. Call cops.")
    if choice == "1":
        time.sleep(2)
        slow_read(F"{Fore.WHITE}You point the zapper at Trump.")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 3:
            time.sleep(2)
            print("But his men get to you before you zapp... ")
            time.sleep(2)
            print("They bundle you into the back of a van.")
            time.sleep(2)
            print("Oh dear...")
            time.sleep(2)
            slow_read(F"{Fore.RED}Game over.")
            exit()
        elif defeat_chance < 4:
            Trump.fighting_spirit -= 90
            time.sleep(2) 
            print(F"{Fore.WHITE}You stun him, then turn and zapp the others.")
            time.sleep(2)
            print("Trump's fighting spirit has been knocked by 90 points...")
            time.sleep(2)
            print(f"and is now down to just {Trump.fighting_spirit}.")
            time.sleep(2)
            print("It'll be a while before he poses a problem again...")
            print("Well done :)")
            time.sleep(3)
            print("You get the medical treatment you need...")
            time.sleep(1)
            print("and are able to return to work.")
            time.sleep(2)
            print(F"{Fore.GREEN}You decide to flip a coin...")
            time.sleep(2)
            print("If it's heads, you grab a coffee.")
            time.sleep(2)
            print("If it's tails, you get a smoothie.")
            time.sleep(2)
            print("And if the coin falls out of your hand...")
            time.sleep(2)
            print("you can have some valium. (You probably need it).")
            time.sleep(2)
            print(F"{Fore.BLUE}You flip the coin and you get... ")
            treats()
            """ treats for if you beat Trump """
 
    elif choice == 2:
        print("You run, and slip on your own blood.")
        time.sleep(2)
        print("A black van drives straight into you.")
        time.sleep(2)
        print("Sorry. You died.")
        time.sleep(2)
        slow_read(F"{Fore.RED}Game over.")
        exit()
    else:
        police = """The police don't arrive in time.
        But some medical staff run out of the building.
        A nurse gets Trump in the neck with a needle...
        The security men scatter.
        You get the care you need, and everyone is smiling.
        You decide to flip a coin...
        If it's heads, you grab a coffee.
        If it's tails, you get a smoothie."
        And if the coin falls out of your hand...
        you can have some valium from the nurse. (You probably need it).
        You flip the coin and you get..."""
        for line in police.splitlines():
            print(line)
            sleep(1) 
        treats()
        """Treats for if you beat Trump"""


# PART FIVE - IF PLAYER BEAT SCHLAFLY, GO TO CAFE & GET READY TO FIGHT TRUMP!


def perks_select():
    """ heroine gets a perk that raises score after defeating Schlafly """
    global heroine
    perk_chance = random.randint(0, 10)
    if perk_chance > 5:
        slow_read(F"{Fore.BLUE}Tails!")
        time.sleep(2)
        print("You get a large coffee AND a big slice of chocolate cake.")
        heroine.fighting_spirit += 100
        heroine.calories_to_burn += 300
        heroine.self_esteem += 200
        time.sleep(1)
        slow_read("Your fighting spirit increases by 100pts...")
        time.sleep(1.5)
        slow_read(
            f"to {heroine.fighting_spirit}.")
        slow_read("Your calories to use for fighting increase by 200,") 
        slow_read(f"to {heroine.calories_to_burn}.")
        slow_read("& your self-esteem has gone up by 200pts")
        slow_read(f"to: {heroine.self_esteem}.")

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
    elif perk_chance < 6:
        time.sleep(1)
        print(F"{Fore.LIGHTYELLOW_EX}Heads!")
        heroine.fighting_spirit += 50
        time.sleep(1)
        print("You grab a coffee. Caffiene boosts your fighting spirit...")
        time.sleep(1)
        print(f"by 50 points, to {heroine.fighting_spirit} :)")

        Fight_Trump()
        """ Onto the next scene to fight Trump! """
                

# PART FOUR: A BUS FIGHT WITH SCHLAFLY! 1st PART OF REAL STORY.

def Bus_Fight():
    global heroine
    """ First battle of heroine Vs opponent """
    slow_read(F"{Fore.MAGENTA}CHAPTER ONE:\n \n")
    slow_read(F"{Fore.WHITE}You get on a bus. It is 8am.\n")
    time.sleep(2)
    slow_read("You have 20mins to read before work.\n")
    time.sleep(2)
    slow_read("Just as you get your book out of your bag...\n")
    time.sleep(2)
    slow_read("a dangerous enemy sits next to you...\n")
    time.sleep(2)
    bus_description = """blocking your way out into the aisle.
'Hello', she says. 'My name's Schlafly...'
'I don't think you should be going to work,' she continues...  
\n"""

    for line in bus_description.splitlines():
        print(line)
        time.sleep(2)
    
    slow_read("she draws a tiny gun from the pocket of her cardigan.\n")

    print(F"\n{Fore.GREEN}You have two choices: \n")
    time.sleep(2)
    choice = input(
        F"{Fore.BLUE}1. Use injustice_zapper \n \n2. Push her and run! \n")
    if choice == "1":
        slow_read(
            F"{Fore.WHITE}You point the anti-injustice zapper at Schlafly.")
        defeat_chance = random.randint(0, 10)
        if defeat_chance > 7:
            time.sleep(2)
            print(
                F"\n{Fore.WHITE}Schlafly knocks the zapper out of your hands")
            time.sleep(1)
            print("\nand shoots you. You die.\n")
            time.sleep(0.5)
            print("You'll never get to work, now.\n")
            time.sleep(0.5)
            slow_read(F"{Fore.RED}Game over. Sorry :(")

            exit()
        elif defeat_chance < 8:
            Schlafly.fighting_spirit -= 40 
            print(F"\n{Fore. WHITE}You manage to stun her. She falls.")
            time.sleep(1)
            slow_read("\nHer fighting spirit has been knocked by 40 points...")
            print(f"\nand is now down to just {Schlafly.fighting_spirit}.")
            prize = """She'll have less energy to pester other people, now :)
Well done!
The bus stops near the office and you get off.
You decide to flip a coin...
If it's heads, you'll grab a coffee from the cafe opposite.
If it's tails, you get coffee AND cake.
And if the coin falls out of your hand...
you can have a coffee and a pain au chocolate.
You flip the coin and you get... """

            for line in prize.splitlines():
                print(line)
                sleep(1.5) 
            
            perks_select()
    else:
        print(F"\n{Fore. WHITE}Schlafly gets right back up...")
        time.sleep(1)
        print("\n... and shoots you in the back as you try to run.")
        time.sleep(1.5)
        print("\nSorry. She won. You died.\n \n")
        time.sleep(1.5)
        slow_read(F"{Fore.RED}Game over.")
        exit()


# PART THREE: If 'Y', CHOOSE A HEROINE & move to a bus fight!!


def heroine_select():
    global heroine
    """ Allows player to choose which heroine they play as.
    Go to line 32 if need to read the printStats function """
    selection = input(
        "\n1. Demeter \n2. Persephone  \n3. Athena \n4. Lilith \n5. Roe \n")
   
    if selection == "1":
        heroine = Demeter
        heroine.printStats_and_start()
        """Heroine is taken to first part of the story"""
    elif selection == "2":
        heroine = Persephone
        heroine.printStats_and_start()
    elif selection == "3":
        heroine = Athena
        heroine.printStats_and_start()
        """Heroine is taken to first part of the story"""
    elif selection == "4":
        heroine = Lilith
        heroine.printStats_and_start()
        """Heroine is taken to first part of the story"""
    elif selection == "5":
        heroine = Roe
        heroine.printStats_and_start()
    else:
        slow_read(F"{Fore.RED}Error!")
        slow_read("Only press 1, 2, 3, 4 or 5 and press enter")
        heroine_select()  # This function is defined on line 37.


# PART TWO - WANNA PLAY OR NOT?


def play_or_not():
    """ player chooses to continue to game or quit """
    answer = input(F"\n\n{Fore.BLUE}Answer 'y' or 'n': ")
    if answer.lower().strip() == "y":
        slow_read(F"\n{Fore.WHITE}Great! ") 
        slow_read("Choose which heroine you want to play as...")
        print()
        heroine_select()
    elif answer.lower().strip() == "n":
        print(F"{Fore.WHITE}I don't blame you. Bye!")
        exit()
    else:
        slow_read(F"\n{Fore.RED}Incorrect input!")
        slow_read("\n\nTry again. Just one letter and press enter.")
        play_or_not()


# PART ONE: LOGO. INTRO to game. Takes goes to decision function: play or not

print("""
╔╦╗╦ ╦╔═╗╦═╗╔═╗  ╦╔═╗  ╦  ╦╔═╗╦ ╦╔╦╗
 ║ ╠═╣║╣ ╠╦╝║╣   ║╚═╗  ║  ║║ ╦╠═╣ ║ 
 ╩ ╩ ╩╚═╝╩╚═╚═╝  ╩╚═╝  ╩═╝╩╚═╝╩ ╩ ╩                                                       
""")

""" CREDS for lettering in title: 
Mini by Glenn Chappell 4/93
Includes ISO Latin-1
figlet release 2.1 -- 12 Aug 1994
Permission is hereby given to modify this font, as long as the
modifier's name is placed on a comment line.

Modified by Paul Burton <solution@earthlink.net> 12/96 to include 
new parameter
supported by FIGlet and FIGWin.  May also be slightly modified for better use
of new full-width/kern/smush alternatives, but default output is NOT changed.

from https://patorjk.com/"""

time.sleep(2)
intro = """This is a game where winning is hard.
The situation is as follows... 
You wake up trapped in a patriarchial nightmare.
The odds are staked against you.
There will be enemies! And enemies are a drag!
But you will always have options: either y/n...
...or a number you need to select to choose a pathway.
(Remember to press 'enter' after your selection.)
Also, you can pick up points, which increases your score...
... by eating cake and winning fights :) """

for line in intro.splitlines():
    print(line)
    sleep(2)

slow_read(F"\n{Fore.GREEN}Would you like to play?")

play_or_not()       
