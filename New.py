import os, platform
t = 0
a = [] # player resonses stored here
m = [['Where is the GO Park located?\nA. Pewter City\nB. Fuchsia City\nC. Pallet Town\nD. Cinnabar Island','MC'],['What Title do you earn by defeating Red?\nA. Pokémon Master\nB. Master Trainer\nC. Red Master\nD. Battle Master','MC'],['Where can you find wild Hitmonchan?\nA. Pokmeon Road\nB. Cerulean Cave\nC. Victory Road\nD. Route 18','MC'],['Who is the Fairy-type Trainer found at Vermilion City?','T'],['What is the cap for sending Pokémon to the Professor?','INT'],['That was the easy part! Are you ready to keep going?\nA. But it\'s hard already...\nB. Wynaut?\nC. GOTTA CATCH \'EM ALL!!\nD. No, but Let\'s GO!','MC'],['What percent of damage from a Fairy-type move affects a Poison-type Pokémon? (_%)','INT'],['How many Rare Candies are obtainable from one Poké Ball Plus session?','INT'],['You can access Cerulean Cave via Route 4.','T/F'],['What outfit does the Stone-selling Trainer wear?\nA. Slowpoke\nB. Juggler\nC. Ace Trainer\nD. Hiker','MC'],['What Pokédex number is Pidgeot?','INT'],['How much money can you sell Beach Glass for?','INT'],['You can ride on Kangaskhan.','T/F'],['How many hairstyles can you give your Partner Eevee?','INT'],['Which button does the Top Button of the Poké Ball Plus register as?','T'],['How many Pokémon are in the complete Let\'s GO Pokédex?','INT'],['What does Trainer Mina give you when defeated?\nA. Heart Scale\nB. Bottle Cap\nC. Nugget\nD. Pearl','MC'],['What are Bottle Caps used for?\nA. Hyper Training\nB. Move Reminder\nC. Trading\nD. Bragging Rights','MC'],['You can find Scyther in "Let\'s GO, Eevee!".','T/F'],['What accent does the \'e\' in \'Pok_mon\' have?\nA. é\nB. è\nC. ë\nD. ê','MC']] # questions stored here
s = [[' Youngster... you can do better than that!',10],[' Bug Catcher!',20],[' Hiker!',30],[' Rising Star!',50],[' Scientist!',70],['n Ace Trainer!!',95],[' Pokémon Master!!!',100]] # titles stored here
r = [['b'],['d'],['c'],['mina'],['30'],['b','c','d'],['50'],['3'],['f'],['a'],['18'],['400'],['t'],['8'],['x'],['153'],['b'],['a'],['f'],['a']] # correct answers stored here
p = [['darwin','clear'],['java','System.out.print("\\033[H\\033[2J");System.out.flush();'],['linux','clear'],['windows','cls']] # os commands stored here
for item in p:
	if platform.system().lower() == item[0]:
		x = item[1]
		cls = lambda: os.system(x)
try:
	cls()
except Exception:
	cls = lambda: print('')
try:
	import msvcrt
except Exception:
	try:
		os.system('python -m pip install getch')
	finally:
		cls()
	wait = lambda: getch.getch()
else:
	wait=lambda: msvcrt.getch()
def b(z):
	while True:
		cls()
		input(f'\nERROR: {z}')
if len(m)!=len(r):
	b(f'There are {len(m)} questions, but {len(r)} correct answers stored.')
print(f'''\n                                                      ,---,\n                                                    ,`--.' |\n    ,----..                                         |   :  :\n   /   /   \                    ,--,                '   '  ;\n  /   .     :            ,--, ,--.'|          ,----,|   |  |\n .   /   ;.  \         ,'_ /| |  |,         .'   .`|'   :  ;\n.   ;   /  ` ;    .--. |  | : `--'_      .'   .'  .'|   |  '\n;   |  ; \ ; |  ,'_ /| :  . | ,' ,'|   ,---, '   ./ '   :  |\n|   :  | ; | '  |  ' | |  . . '  | |   ;   | .'  /  ;   |  ;\n.   |  ' ' ' :  |  | ' |  | | |  | :   `---' /  ;--,`---'. |\n'   ;  \; /  |  :  | : ;  ; | '  : |__   /  /  / .`| `--..`;\n \   \  ',  . \ '  :  `--'   \|  | '.'|./__;     .' .--,_\n  ;   :      ; |:  ,      .-./;  :    ;;   |  .'    |    |`.\n   \   \ .~`--'  `--`----`    |  ,   / `---'        '----`,;\n    `---`                      ---`-                 ---"\n\n"Pokémon: Let's GO, Eevee! Quiz" by TurnipGuy30. Repo located at [https://github.com/TurnipGuy30/LGPE-Quiz].\n\nInstructions:\nT = Text; type your answer\nMC = Multiple Choise; type a/b/c/d\nT/F = True or False; type t/f\nINT = Integer Answer; type the number\n\nThere are {len(m)} questions\nWorded questions are not case-sensitive\nPoints are revealed at the end!\n\nPress any key to begin.''')
wait()
cls()
for i in range(len(m)):
	print(f'\nQ{i+1}. {m[i][0]}')
	a.append('')
	while a[i] == '':
		a[i] = input(f'{m[i][1]}: ').lower()
	cls()
print('\nPlease wait..')
p = 0
for i in range(len(m)):
	for j in range(len(r[i])):
		if a[i] == r[i][j]:
			p += 1
c = p * (100 / len(m))
for i in range(len(s)):
	if int(c) >= s[i][1]:
		t = s[i][0]
print('\nDone! Press any key to continue.')
wait()
cls()
input(f'\nYou scored {str(p)}/{len(m)} points ({str(c)}%)!\nThat means you\'re a{t}\n\nPress Enter to exit.')
