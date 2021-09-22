'''=========================================================================================================================================================
|                                                                                                                                                          |
|                                                                                                                                          ,---,    ,---,  |
| ,-.----.                                                                                                                               ,`--.' | ,`--.' | |
| \    /  \                  ,-.                    ____                                 ,----..                                         |   :  : |   :  : |
| |   :    \             ,--/ /|                  ,'  , `.                              /   /   \                    ,--,                '   '  ; '   '  ; |
| |   |  .\ :   ,---.  ,--. :/ |               ,-+-,.' _ |   ,---.        ,---,        /   .     :            ,--, ,--.'|          ,----,|   |  | |   |  | |
| .   :  |: |  '   ,'\ :  : ' /             ,-+-. ;   , ||  '   ,'\   ,-+-. /  |      .   /   ;.  \         ,'_ /| |  |,         .'   .`|'   :  ; '   :  ; |
| |   |   \ : /   /   ||  '  /      ,---.  ,--.'|'   |  || /   /   | ,--.'|'   |     .   ;   /  ` ;    .--. |  | : `--'_      .'   .'  .'|   |  ' |   |  ' |
| |   : .   /.   ; ,. :'  |  :     /     \|   |  ,', |  |,.   ; ,. :|   |  ,"' |     ;   |  ; \ ; |  ,'_ /| :  . | ,' ,'|   ,---, '   ./ '   :  | '   :  | |
| ;   | |`-' '   | |: :|  |   \   /    /  |   | /  | |--' '   | |: :|   | /  | |     |   :  | ; | '  |  ' | |  . . '  | |   ;   | .'  /  ;   |  ; ;   |  ; |
| |   | ;    '   | .; :'  : |. \ .    ' / |   : |  | ,    '   | .; :|   | |  | |     .   |  ' ' ' :  |  | ' |  | | |  | :   `---' /  ;--,`---'. | `---'. | |
| :   ' |    |   :    ||  | ' \ \'   ;   /|   : |  |/     |   :    ||   | |  |/      '   ;  \; /  |  :  | : ;  ; | '  : |__   /  /  / .`| `--..`;  `--..`; |
| :   : :     \   \  / '  : |--' '   |  / |   | |`-'       \   \  / |   | |--'        \   \  ',  . \ '  :  `--'   \|  | '.'|./__;     .' .--,_    .--,_    |
| |   | :      `----'  ;  |,'    |   :    |   ;/            `----'  |   |/             ;   :      ; |:  ,      .-./;  :    ;;   |  .'    |    |`. |    |`. |
| `---'.|              '--'       \   \  /'---'                     '---'               \   \ .'`--"  `--`----'    |  ,   / `---'        `-- -`, ;`-- -`, ;|
|   `---`                          `----'                                                `---`                      ---`-'                 '---`"   '---`" |
|                                                                                                                                                          |
|                                                    Name:     Pokémon: Let's GO, Eevee! Quiz                                                              |
|                                                    Author:   JohnnySD                                                                                    |
|                                                                                                                                                          |
========================================================================================================================================================='''


## = heading
# = subheading


##intro
#title
print("                                                       ,---,  ")
print("                                                    ,`--.' |  ")
print("    ,----..                                         |   :  :  ")
print("   /   /   \                    ,--,                '   '  ;  ")
print("  /   .     :            ,--, ,--.'|          ,----,|   |  |  ")
print(" .   /   ;.  \         ,'_ /| |  |,         .'   .`|'   :  ;  ")
print(".   ;   /  ` ;    .--. |  | : `--'_      .'   .'  .'|   |  '  ")
print(";   |  ; \ ; |  ,'_ /| :  . | ,' ,'|   ,---, '   ./ '   :  |  ")
print("|   :  | ; | '  |  ' | |  . . '  | |   ;   | .'  /  ;   |  ;  ")
print(".   |  ' ' ' :  |  | ' |  | | |  | :   `---' /  ;--,`---'. |  ")
print("'   ;  \; /  |  :  | : ;  ; | '  : |__   /  /  / .`| `--..`;  ")
print(" \   \  ',  . \ '  :  `--'   \|  | '.'|./__;     .' .--,_     ")
print("  ;   :      ; |:  ,      .-./;  :    ;;   |  .'    |    |`.  ")
print("   \   \ .~`--'  `--`----`    |  ,   / `---'        '----`,; ")
print('    `---`                      ---`-'+"                 "+'"---"  ')
print("")
print("Pokémon: Let's GO, Eevee! Quiz")
print("")

#instructions
print("Instructions:")
print("T = Text; type your answer")
print("MC = Multiple Choise; type a/b/c/d")
print("T/F = True or False; type t/f")
print("INT = Integer Answer; type the number")
print("Worded questions are not case-sensitive")
print("Points are revealed at the end!")
print("")

#start
input("Press Enter to begin")
print("")

#adding some personality
print("Let's GO!")
print("")


##questions
#q1
print("1. Where is the GO Park located?")
print("A. Pewter City")
print("B. Fuchsia City")
print("C. Pallet Town")
print("D. Cinnabar Island")
q1 = str(input("MC: "))
print("")

#q2
print("2. What Title do you earn by defeating Red?")
print("A. Pokémon Master")
print("B. Master Trainer")
print("C. Red Master")
print("D. Battle Master")
q2 = str(input("MC: "))
print("")

#q3
print("3. Where can you find wild Hitmonchan?")
print("A. Pokmeon Road")
print("B. Cerulean Cave")
print("C. Victory Road")
print("D. Route 18")
q3 = str(input("MC: "))
print("")

#q4
print("4. Who is the Fairy-type Trainer found at Vermilion City?")
q4 = str(input("T: "))
print("")

#q5
print("5. What is the cap for sending Pokémon to the Professor?")
q5 = int(input("INT: "))
print("")

#q6
print("6. That was the easy part! Are you ready to keep going?")
print("A. But it's hard already...")
print("B. Wynaut?")
print("C. GOTTA CATCH 'EM ALL!!")
print("D. No, but Let's GO!")
q6 = str(input("MC: "))
print("")

#q7
print("7. What percent of damage from a Fairy-type move affects a Poison-type Pokémon? (_%)")
q7 = int(input("INT: "))
print("")

#q8
print("8. How many Rare Candies are obtainable from one Poké Ball Plus session?")
q8 = int(input("INT: "))
print("")

#q9
print("9. You can access Cerulean Cave via Route 4.")
q9 = str(input("T/F: "))
print("")

#q10
print("10. What outfit does the Stone-selling Trainer wear?")
print("A. Slowpoke")
print("B. Juggler")
print("C. Ace Trainer")
print("D. Hiker")
q10 = str(input("MC: "))
print("")

#q11
print("11. What Pokédex number is Pidgeot?")
q11 = int(input("INT: "))
print("")

#q12
print("12. How much money can you sell Beach Glass for?")
q12 = int(input("INT: "))
print("")

#q13
print("13. You can ride on Kangaskhan.")
q13 = str(input("T/F: "))
print("")

#q14
print("14. How many hairstyles can you give your Partner Eevee?")
q14 = int(input("INT: "))
print("")

#q15
print("15. Which button does the Top Button of the Poké Ball Plus register as?")
q15 = str(input("T: "))
print("")

#q16
print("16. How many Pokémon are in the Let's GO Pokédex?")
q16 = int(input("INT: "))
print("")

#q17
print("17. What does Trainer Mina give you when defeated?")
print("A. Heart Scale")
print("B. Bottle Cap")
print("C. Nugget")
print("D. Pearl")
q17 = str(input("MC: "))
print("")

#q18
print("18. What are Bottle Caps used for?")
print("A. Hyper Training")
print("B. Move Reminder")
print("C. Trading")
print("D. Bragging Rights")
q18 = str(input("MC: "))
print("")

#q19
print("19. You can find Scyther in Let's GO, Eevee!.")
q19 = str(input("T/F: "))
print("")

#q20
print("20. What accent does the 'e' in 'Pok_mon' have?")
print("A. é")
print("B. è")
print("C. ë")
print("D. ê")
q20 = str(input("MC: "))
print("")

#notice
print("Please wait..")
print("")


##calculate score
#score variable
p = 0

#q1
if q1.lower() == "b":
    p+=1

#q2
if q2.lower() == "d":
    p+=1

#q3
if q3.lower() == "c":
    p+=1

#q4
if q4.lower() == "mina":
    p+=1

#q5
if q5 == 30:
    p+=1

#q6
if q6.lower() == "b" or q6.lower() == "c" or q6.lower() == "d":
    p+=1

#q7
if q7 == 50:
    p+=1

#q8
if q8 == 3:
    p+=1

#q9
if q9.lower() == "f":
    p+=1

#q10
if q10.lower() == "a":
    p+=1

#q11
if q11 == 18:
    p+=1

#q12
if q12 == 400:
    p+=1

#q13
if q13.lower() == "t":
    p+=1

#q14
if q14 == 8:
    p+=1

#q15
if q15.lower() == "x":
    p+=1

#q16
if q16 == 153:
    p+=1

#q17
if q17.lower() == "b":
    p+=1

#q18
if q18.lower() == "a":
    p+=1

#q19
if q19.lower() == "f":
    p+=1

#q20
if q20.lower() == "a":
    p+=1

#percentage variable
per = p * 5


##title calculation
#title variable
t = ""

#0
if p == 0:
    t = "a Youngster..."

#1 to 4
elif p >=0 and p < 5:
    t = "a Bug Catcher.."

#5 to 9
elif p >= 5 and p < 10:
    t = "a Hiker."

#10 to 14
elif p >= 10 and p < 15:
    t = "a Scientist!"

#15 to 19
elif p >= 15 and p < 20:
    t = "an Ace Trainer!!"

#20
elif p == 20:
    t = "a Pokémon Master!!!"


##results
print("You scored " + str(p) + " points (" + str(per) + "%)!")
print("That means you're " + t)
print("")
input("Press Enter to exit")
