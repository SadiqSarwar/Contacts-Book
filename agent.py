#header file.
from time import sleep
import sys

#Create Agent class.
class Agent:

    #Create intro function.
    def intro(self):
        print("You have chosen 'Agent' as your character")
        sleep(1.0)    #Pause code 1 seconds.
        print("Loading...")
        sleep(2.0)    #Pause code 2 seconds.
        print("The game will now begin! \n")

    #Create setScence function.
    def setScene(self):
        sleep(2.0)    #Pause code 2 seconds.
        print("""┼┼┼┼┼┼┼┼┼┼┼┼████████████████
                ┼┼┼┼┼┼┼┼┼┼┼┼██▒██▒███▒██▒███
                ┼┼┼┼┼┼┼┼┼┼┼███████▒█▒████████
                ┼┼┼┼┼┼┼┼┼┼┼████████▒█████▒█▒█
                ┼┼┼┼┼┼┼┼┼┼████████▒█▒█████▒███
                ┼┼┼┼┼┼┼┼┼┼████▒██▒███▒███▒█▒██
                ┼┼┼┼┼┼┼┼┼████▒▒▒███████████████
                ┼┼┼┼┼┼┼┼┼████▒▒▒████████████▒██
                ┼┼┼┼┼┼┼┼████▒▒▒▒▒███▒█▒█████████
                ┼┼┼┼┼┼┼┼████▒▒▒▒▒████▒███▒██▒███
                ┼┼┼┼┼┼┼████▒▒▒▒▒▒▒██▒█▒███▒█▒████
                ┼┼┼┼┼┼┼████▒▒▒▒▒▒▒█████████▒█████
                ┼┼┼┼┼┼████▒▒▒▒▒▒▒▒▒███████▒█▒█████
                ┼┼┼┼┼┼████▒▒▒▒▒▒▒▒▒███▒██▒███▒████
                ┼┼┼┼┼████▒▒▒▒▒▒▒▒▒▒▒███████████████
                ┼┼┼┼┼████▒▒▒▒▒▒▒▒▒▒▒███████▒███▒███
                ┼┼┼┼████▒▒▒███████▒▒▒███████████████
                ┼┼┼┼████▒▒▒█░░█░░█▒▒▒████▒███▒██████
                ┼┼┼████▒▒▒▒█░░█░░█▒▒▒▒████▒█▒███▒█▒██
                ┼┼┼████▒▒▒▒███████▒▒▒▒█████▒█████▒███
                ┼┼████▒▒▒▒▒█░░█░░█▒▒▒▒▒███▒█▒███▒█▒███
                ┼┼████▒▒▒▒▒█░░█░░█▒▒▒▒▒██▒███▒████████
                ┼████▒▒▒▒▒▒███████▒▒▒▒▒▒████████████▒██
                ┼████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒███████████
                █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
                █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███████████████
                ┼┼┼┼█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒█▒█▒█▒█▒█▒█
                ┼┼┼┼█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
                ┼┼┼┼█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████
                ┼┼┼┼█▒▒▒█░█░█░█░█░█░█▒▒▒████▒▒▒▒▒▒▒███
                ┼┼┼┼█▒▒▒█████████████▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒███░░░█░░░███▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒█████████████▒▒▒████▒▒▒▒▒▒▒███
                ┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒███░░░█░░░███▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒█████████████▒▒▒████▒░░▒░░▒███
                ┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒████▒▒▒▒▒▒▒███
                ┼┼┼┼█▒▒▒███░░░█░░░███▒▒▒██████████████
                ┼┼┼┼█▒▒▒█░█░░░█░░░█░█▒▒▒██████████████
                ┼┼┼┼█▒▒▒█████████████▒▒▒██████████████
                ┼┼┼┼█▒▒▒█░█████████░█▒▒▒██████████████
                ┼┼┼┼█▒▒▒█████████████▒▒▒██████████████
                ┼┼┼┼█▒▒▒█░█████████░█▒▒▒██████████████
                ┼┼┼┼█▒▒▒█████████████▒▒▒██████████████
                ┼┼┼┼█▒▒▒█░█████████░█▒▒▒██████████████""")

        print("You are with artificial intellience swat members in a large building.")
        print("You received word that the chosen one and other humans are on the top floor")
        print("You search and search and have not yet found them")
        print("Make the correct choices needed in order capture the inferior humans. \n")
        sleep(2.0)

    #Create firstDecision function.
    def firstDecision(self):
        sleep(4.0)    #Pause code 4 seconds.
        print("----------------------------------Start------------------------------------")
        print("The swat members and you start to search rapidly in every hiding spot that they could be in.")
        print("In the process, an aritificial swat member searches the floors.\n")

        print("[Choices]")
        print("(1) Move on to the next floor")
        print("(2) Check the floor that you are on.")

    #Create firstFail function.
    def firstFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("The aritificial swat member decides to check the next floor.")
        print("The aritificial swat member has checked the next floor with nobody there!")
        print("""              ____________________________________ 
                          I___|___|___|___|___|__|____|___|__|_I 
                          I_|___|___|               |___|___|__I 
                    )\    I___|__ | ..,a@@@a,a@@@a,.. |___|____I      /( 
                   ( ))   I_|__  .,;*;;@@@@@a@@@@@;;;;,. ___|__I     (( ) 
                    :     I__|  ;;;;;;;;;a@@^@@a;;;*;;;;;  __|_I       : 
                   ,uU    I_|  ;;;;*;;;a@@@   @@@a;;;;*;;;  |__I      Uu. 
                   :Uu    I__|;;;;;;;a@@@@   .@@@@@;;;;;;;; __|I      uU: 
                   | |    I_| ;;*;;;a@@@@@   @@'`@@@;;;;;*; _|_I      | | 
                   |_|    I__ ;;;;;;@@;;@@   `@  `@;;;*;;;; ___I      |_| 
                _ (___) _ I_|_ ;;;*;;@;;;;@;;;;;*;;;;;;;;; _|__I___  (___) 
              ,-' )   (   ~~~~~ `;;;;;;*;;;;;;;;;;;*;;;;'  ~~~~~     )   (`-. 
            ,-____=====____________`;;;;;;;;;*;;;;;;;'_______________=====___`. 
            |~~|  _________________________________________________/o\___   |~~| 
            |_||  ||____|____|____|____|____|____|____|____|____|_/ /,\__|  ||_| 
            |__|  |___|____|____|____|____|____|____|____|____|__/ /,,,\||  ||_| 
            |_||__||____|____|____|____|____|____|____|____|____|\/,,,,,\|__|__| 
            |____|____|____|____|____|____|____|____|____|____|___\,,,,,,\___|_| 
            |_|____|__I####I..........  /%%%%%%%%%%%\ ..........I##\,,,,( )|___| 
            |____|____I####I.......... .%%%%%( )%%%%%. .........I###\,,,,\/__|_| 
            |_|____|__I####I.......... @@%%%%0%0%%%%@@  ........I## /,,,,/_|___| 
            |____|____I####I.......... `@@@@@@@@@@@@@@' ........I# /,,,,/____|_| 
            |_|____|__I####I............ \\\\\\\\\\\\\) ........I ( \,,/___|___| 
            |____|____I####I.............  `\\\\\\\\\\) ........I  \_)/_|____|_| 
            | |   _|__I####I............  A   `\\\\\\\' ..   .. I#  :_|____|___| 
            vvnnmm. __I####I.........    AAA  .. `\\\' ..  A.  .I###I___|____|_| 
            vvnnmmm, _I####I......   .A  `AAA ....  *  ..  AAA. I ##I_|____|___| 
            vvnnnmmm _I####I....    AAA  AA;AA  ...   ...  `AAA.I ##I___|____|_| 
            vvnnnnmm _I####/~~~,-.A;;A'-A;;;;;A-----A-----,A;;;A  ##I_|____|___| 
            vvnnnnmm _I###/    I.;;;;;  ;;;;;;;   AAA     I;;;A'\###I___|____|_| 
            vvnnnnm' _I##/     I;;;;;; ;;;;;;;   A;;;A    I;;;;  \##I_|____|___| 
            vvnnnmm  _I#/     !~;;;;;;~~~~~~~~~~~;;;;;;~~~~~!;'   \#I___|____|_| 
            vvnnnm'  _I/______!  ::::;;           ;;;;;;    !______\I_|____|___| 
            vvnnm'   ~~/       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       \~~~~~~~~~~ 
            vvnmm     /_______________________________________________\ 
            vvmmmvvnnnnnnnnnnmmv,             
            vvmmvvnnnnnnnnnnmmvvv            
            vvnnnnnnnnnnnnnnmmvv'       
            vvnnnnnnnnnnnnnnnnnv,    
            vvnnnnnnnnnnnnnnnnnnv,  
            vvnnnnnnnnnnnnnnnnnnvv  
            %%%%%%%%%%%%%%%%%%%%%;  
            mmvvvmvvvmvvvmvvvmvvvm,   
            mmv'vmv'vmv'vmv'vmv'vmv,            """)
        print("The inferior humans have escaped!")
        print("[Game Over]")

    #Create secondDecision function.
    def secondDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("The aritificial swat member slowly checks every corner with a flashlight")
        print("He hears a noise in the wall that sounds like a rat, turning 90 degrees, he slowly creeps up against it.")
        print("The aritificial swat member hear someone sneeze in the wall and he start firing at it.")
        print("""                                     |
                  ----.                               |
                 "   _}                               |   
                 "@   >                               |
                 |\   7                               |
                 / `-- _         ,-------,****        |
              ~    >o<  \---------o{___}-             |
             /  |  \  /  ________/8'                  |
             |  |       /         "                   |
             |  /      |                              |   \n                                """)
        
        print("He take cover from the enemies barrage of fire, calling for backup.")
        print("You take over the aritificial swat member's body as the agent.")
        print("""─────────────────────────────▄██▄
                ─────────────────────────────▀███
                ────────────────────────────────█
                ───────────────▄▄▄▄▄────────────█
                ──────────────▀▄────▀▄──────────█
                ──────────▄▀▀▀▄─█▄▄▄▄█▄▄─▄▀▀▀▄──█
                ─────────█──▄──█────────█───▄─█─█
                ─────────▀▄───▄▀────────▀▄───▄▀─█
                ──────────█▀▀▀────────────▀▀▀─█─█
                ──────────█───────────────────█─█
                ▄▀▄▄▀▄────█──▄█▀█▀█▀█▀█▀█▄────█─█
                █▒▒▒▒█────█──█████████████▄───█─█
                █▒▒▒▒█────█──██████████████▄──█─█
                █▒▒▒▒█────█───██████████████▄─█─█
                █▒▒▒▒█────█────██████████████─█─█
                █▒▒▒▒█────█───██████████████▀─█─█
                █▒▒▒▒█───██───██████████████──█─█
                ▀████▀──██▀█──█████████████▀──█▄█
                ──██───██──▀█──█▄█▄█▄█▄█▄█▀──▄█▀
                ──██──██────▀█─────────────▄▀▓█
                ──██─██──────▀█▀▄▄▄▄▄▄▄▄▄▀▀▓▓▓█
                ──████────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ──███─────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ──██─────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ──██────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█
                ──██───────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
                ──██──────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
                ──██─────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌
                ──██────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌\n""")
        sleep(3.0)

        print("[Choices]")
        print("(1) Shoot back")
        print("(2) Try to fistfight them as they shoot you.")

    #Create secondFail function.
    def secondFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You try to rush at them hoping to dodge the bullets.")
        print("Instead, you get shot multiple times and die, not before you leave the swat body, barely living.")
    
        print("Until next time........")
        print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░▓████████████████████████▒░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░▓█████▓▒░░░░░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░████▒░░░░░░░░░░░░░░░░░░░░░░░░░▓███▒░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░
                ░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░
                ░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░
                ░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░██░░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██▒░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓░▒██░░░░░░░░░░░
                ░░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
                ░░░░░░░░░░░░██▒░██░░░░░▒▒▓███▒░░░░░░░▒███▓▒▒░░░░░██░▓██░░░░░░░░░░░░
                ░░░░░░░░░░░░░██░██░░██████████▒░░░░░▓██████████░░██▒██░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░████░████████████░░░░░████████████░████░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░███░▒██████████░░░░░░░██████████▒░██▒░░░░░░░░░▒░░░░░
                ░░░▒████░░░░░░░▓█▒░░█████████░░░░░░░░░█████████░░▒█▓░░░░░░▓████░░░░
                ░░░██░▒██▒░░░░░██░░░░██████▓░░░░█░█░░░░███████░░░░██░░░░░███░░██░░░
                ░░░██░░░██▓░░░░██░░░░░░▒▓▓░░░░▒██░██░░░░░▓▓▒░░░░░▒██░░░░███░░░██░░░
                ░▓██▒░░░░████▓░░██░░░░░░░░░░░░███░███░░░░░░░░░░░░██░░█████░░░░▓██▒░
                ██▓░░░░░░░░▒████████▓░░░░░░░░████░███▓░░░░░░░▒▓████████░░░░░░░░░███
                ██▓▒▓███▓░░░░░░▓████████▓░░░░████░███▓░░░░▓████████▓░░░░░░████▓▓███
                ░███████████▒░░░░░░███████░░░░██░░░██░░░░██████▓░░░░░░▓███████████░
                ░░░░░░░░░░▓█████░░░░██▓▓░██░░░░░░░░░░░░░██░█▒██░░░▒█████▓░░░░░░░░░░
                ░░░░░░░░░░░░░▒█████▒▒█▓█░███▓▓▒▒▒▓▒▒▓▓▓███▒███░▓█████░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░▒████▒▓█▒▒█░█▒█░█░█▓█▒█▓░█░█████▒░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░██░░██▓█▓█▓█▒█▒█▓█▓████░▓█▓░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░▓████▓░▓█▓█░█▒█░█░█▒█▒███▒░██████░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▓█████░░██░░░▒█████▓█▓█████▒░░░██░▒█████▓░░░░░░░░░░░░░
                ░░░░▒██████████▓░░░░░███░░░░░░░░░░░░░░░░░░░██▒░░░░░▓██████████▒░░░░
                ░░░░██░░░▓▓▓░░░░░░▒██████▓░░░░░░░░░░░░░░░███████▒░░░░░░▓▓▒░░▒██░░░░
                ░░░░▓██░░░░░░░░▓████▓░░░█████▒░░░░░░▒▓█████░░░▓████▓░░░░░░░▒██▓░░░░
                ░░░░░░███░░░░████▒░░░░░░░░▓█████████████▒░░░░░░░░▒████░░░░███░░░░░░
                ░░░░░░░██░░░██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓██░░░██░░░░░░░
                ░░░░░░░██▒▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▒▓██░░░░░░░
                ░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
        print("The inferior humans have escaped!")
        print("[Game Over]")

    #Create thirdDecision function.
    def thirdDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You start shooting back until everyone is out of ammo.\n")
        
        print("[Choices]")
        print("(1) Try and get one through the wall")
        print("(2) Run away like a scaredy cat.")

    #Create thirdFail function.
    def thirdFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You run away like a scaredy, waiting for another day to strike.")
        print("Until next time........")
        print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░▓████████████████████████▒░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░▓█████▓▒░░░░░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░████▒░░░░░░░░░░░░░░░░░░░░░░░░░▓███▒░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░
                ░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░
                ░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░
                ░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░██░░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██▒░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓░▒██░░░░░░░░░░░
                ░░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
                ░░░░░░░░░░░░██▒░██░░░░░▒▒▓███▒░░░░░░░▒███▓▒▒░░░░░██░▓██░░░░░░░░░░░░
                ░░░░░░░░░░░░░██░██░░██████████▒░░░░░▓██████████░░██▒██░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░████░████████████░░░░░████████████░████░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░███░▒██████████░░░░░░░██████████▒░██▒░░░░░░░░░▒░░░░░
                ░░░▒████░░░░░░░▓█▒░░█████████░░░░░░░░░█████████░░▒█▓░░░░░░▓████░░░░
                ░░░██░▒██▒░░░░░██░░░░██████▓░░░░█░█░░░░███████░░░░██░░░░░███░░██░░░
                ░░░██░░░██▓░░░░██░░░░░░▒▓▓░░░░▒██░██░░░░░▓▓▒░░░░░▒██░░░░███░░░██░░░
                ░▓██▒░░░░████▓░░██░░░░░░░░░░░░███░███░░░░░░░░░░░░██░░█████░░░░▓██▒░
                ██▓░░░░░░░░▒████████▓░░░░░░░░████░███▓░░░░░░░▒▓████████░░░░░░░░░███
                ██▓▒▓███▓░░░░░░▓████████▓░░░░████░███▓░░░░▓████████▓░░░░░░████▓▓███
                ░███████████▒░░░░░░███████░░░░██░░░██░░░░██████▓░░░░░░▓███████████░
                ░░░░░░░░░░▓█████░░░░██▓▓░██░░░░░░░░░░░░░██░█▒██░░░▒█████▓░░░░░░░░░░
                ░░░░░░░░░░░░░▒█████▒▒█▓█░███▓▓▒▒▒▓▒▒▓▓▓███▒███░▓█████░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░▒████▒▓█▒▒█░█▒█░█░█▓█▒█▓░█░█████▒░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░██░░██▓█▓█▓█▒█▒█▓█▓████░▓█▓░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░▓████▓░▓█▓█░█▒█░█░█▒█▒███▒░██████░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▓█████░░██░░░▒█████▓█▓█████▒░░░██░▒█████▓░░░░░░░░░░░░░
                ░░░░▒██████████▓░░░░░███░░░░░░░░░░░░░░░░░░░██▒░░░░░▓██████████▒░░░░
                ░░░░██░░░▓▓▓░░░░░░▒██████▓░░░░░░░░░░░░░░░███████▒░░░░░░▓▓▒░░▒██░░░░
                ░░░░▓██░░░░░░░░▓████▓░░░█████▒░░░░░░▒▓█████░░░▓████▓░░░░░░░▒██▓░░░░
                ░░░░░░███░░░░████▒░░░░░░░░▓█████████████▒░░░░░░░░▒████░░░░███░░░░░░
                ░░░░░░░██░░░██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓██░░░██░░░░░░░
                ░░░░░░░██▒▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▒▓██░░░░░░░
                ░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
        print("The inferior humans have escaped!")
        print("[Game Over]")

    #Create fourthDecision function.
    def fourthDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You decide to charge at them like a viking rushing into war")
        print("You have luckily found the chosen one through the wall")
        print("As you grabbed him almost pulling him out of the wall, Morpheus screams,")
        print("pinning you down to the ground long enough for Neo to escape\n")
        
        print("[Choices]")
        print("(1) Chase after Neo")
        print("(2) Fight Morpheus.")

    #Create fourthFail function.
    def fourthFail(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You get up and try to chase Neo, but Morpheus comes from behind with a reloaded gun and shoots you, only after you barely escape the useless body.")
        print("Until next time........")
        print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░▓████████████████████████▒░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░▓█████▓▒░░░░░░░░░░░░░░░▒██████▒░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░████▒░░░░░░░░░░░░░░░░░░░░░░░░░▓███▒░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██░░░░░░░░░░░░░░
                ░░░░░░░░░░░░▒██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░░
                ░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░░░░░░░
                ░░░░░░░░░░░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░██░░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░
                ░░░░░░░░░░░██▒░██▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓░▒██░░░░░░░░░░░
                ░░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░
                ░░░░░░░░░░░░██▒░██░░░░░▒▒▓███▒░░░░░░░▒███▓▒▒░░░░░██░▓██░░░░░░░░░░░░
                ░░░░░░░░░░░░░██░██░░██████████▒░░░░░▓██████████░░██▒██░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░████░████████████░░░░░████████████░████░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░███░▒██████████░░░░░░░██████████▒░██▒░░░░░░░░░▒░░░░░
                ░░░▒████░░░░░░░▓█▒░░█████████░░░░░░░░░█████████░░▒█▓░░░░░░▓████░░░░
                ░░░██░▒██▒░░░░░██░░░░██████▓░░░░█░█░░░░███████░░░░██░░░░░███░░██░░░
                ░░░██░░░██▓░░░░██░░░░░░▒▓▓░░░░▒██░██░░░░░▓▓▒░░░░░▒██░░░░███░░░██░░░
                ░▓██▒░░░░████▓░░██░░░░░░░░░░░░███░███░░░░░░░░░░░░██░░█████░░░░▓██▒░
                ██▓░░░░░░░░▒████████▓░░░░░░░░████░███▓░░░░░░░▒▓████████░░░░░░░░░███
                ██▓▒▓███▓░░░░░░▓████████▓░░░░████░███▓░░░░▓████████▓░░░░░░████▓▓███
                ░███████████▒░░░░░░███████░░░░██░░░██░░░░██████▓░░░░░░▓███████████░
                ░░░░░░░░░░▓█████░░░░██▓▓░██░░░░░░░░░░░░░██░█▒██░░░▒█████▓░░░░░░░░░░
                ░░░░░░░░░░░░░▒█████▒▒█▓█░███▓▓▒▒▒▓▒▒▓▓▓███▒███░▓█████░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░▒████▒▓█▒▒█░█▒█░█░█▓█▒█▓░█░█████▒░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░██░░██▓█▓█▓█▒█▒█▓█▓████░▓█▓░░░░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░░░░░▓████▓░▓█▓█░█▒█░█░█▒█▒███▒░██████░░░░░░░░░░░░░░░░░
                ░░░░░░░░░░░░░▓█████░░██░░░▒█████▓█▓█████▒░░░██░▒█████▓░░░░░░░░░░░░░
                ░░░░▒██████████▓░░░░░███░░░░░░░░░░░░░░░░░░░██▒░░░░░▓██████████▒░░░░
                ░░░░██░░░▓▓▓░░░░░░▒██████▓░░░░░░░░░░░░░░░███████▒░░░░░░▓▓▒░░▒██░░░░
                ░░░░▓██░░░░░░░░▓████▓░░░█████▒░░░░░░▒▓█████░░░▓████▓░░░░░░░▒██▓░░░░
                ░░░░░░███░░░░████▒░░░░░░░░▓█████████████▒░░░░░░░░▒████░░░░███░░░░░░
                ░░░░░░░██░░░██▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓██░░░██░░░░░░░
                ░░░░░░░██▒▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒██▒▓██░░░░░░░
                ░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
        print("The inferior humans have escaped!")
        print("[Game Over]")

    #Create firstDecision function.
    def fifthDecision(self):
        sleep(1.0)    #Pause code 1 seconds.
        print("---------------------------------------------------------------------------")
        print("You decide to fight Morpheus and capture him, using him as bait for the chosen one,")
        print(""".::::::::::.                           .::::::::::.
                .::::''''''::::.                      .::::''''''::::.
              .:::'          `::::....          ....::::'          `:::.
             .::'             `:::::::|        |:::::::'             `::.
            .::|               |::::::|_ ___ __|::::::|               |::.
            `--'               |::::::|_()__()_|::::::|               `--'
             :::               |::-o::|        |::o-::|               :::
             `::.             .|::::::|        |::::::|.             .::'
              `:::.          .::\-----'        `-----/::.          .:::'
                `::::......::::'                      `::::......::::'
                  `::::::::::'                          `::::::::::'""")
        print("You have captured one of the inferior humans and plan to catch the rest later.")
        print("Congradulations! You have won the game!")
        print("[Victory!]")
    
        

                           
        

    

    
        

    
    
   
        
        
        
    