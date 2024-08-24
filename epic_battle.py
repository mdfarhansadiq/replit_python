### ******* In the name of Allah *******###


import os, time


def charNameType():
	char_name = input("Name Your Legend: ")
	char_type = input("Character Type (Human, Elf, Wizard, Orc): ")
	return char_name, char_type


def charHealth():
	import random
	dice_1 = random.randint(1, 6)
	dice_2 = random.randint(1, 12)
	char_health = ((dice_1 * dice_2) / 2) + 10
	return char_health


def charStrength():
	import random
	dice_1 = random.randint(1, 6)
	dice_2 = random.randint(1, 12)
	char_strength = ((dice_1 * dice_2) / 2) + 12
	return char_strength

def charBattle(char_name_1, battle_health_1, char_name_2, battle_health_2, strength_diff, round_count):
 import random
 
 char_roll_1 = random.randint(1, 6)
 char_roll_2 = random.randint(1, 6)
 
 if char_roll_1 > char_roll_2:
   battle_health_2 -= strength_diff
   print(char_name_1, "wins the", round_count)
   print(char_name_2, "takes a hit, with", strength_diff)
   return battle_health_1, battle_health_2
 
 elif char_roll_1 < char_roll_2:
   battle_health_1 -= strength_diff
   print(char_name_2, "wins the", round_count)
   print(char_name_1, "takes a hit, with", strength_diff)
   return battle_health_1, battle_health_2
 
 else:
   print("The round is tied...try again")
   return battle_health_1, battle_health_2
		

print("⚔️ BATTLE TIME ⚔️")
char_name_1, char_type_1 = charNameType()
char_health_1 = charHealth()
char_strength_1 = charStrength()
print(char_name_1, char_type_1)
print("HEALTH:", char_health_1)
print("STRENGTH:", char_strength_1)
print("")
print("Who are they battling?")
print("")

char_name_2, char_type_2 = charNameType()
char_health_2 = charHealth()
char_strength_2 = charStrength()
print(char_name_2, char_type_2)
print("HEALTH:", char_health_2)
print("STRENGTH:", char_strength_2)
strength_diff = abs(char_strength_1 - char_strength_2)

time.sleep(10)
os.system("clear")

battle_health_1, battle_health_2 = char_health_1, char_health_2

round_count = 0

while True:
 print("⚔️ BATTLE TIME ⚔️")
 round_count += 1
 battle_h1, battle_h2 = charBattle(char_name_1, battle_health_1, char_name_2, battle_health_2, strength_diff, round_count)
 
 if battle_h1 > 0 and battle_h2 > 0:
   battle_health_1, battle_health_2 = battle_h1, battle_h2
   print("And they're both standing for the next round!")
   time.sleep(7)
   os.system("clear")
   continue
 else:
   if battle_h1 <= 0:
     print(char_name_2, char_type_2, "destroyed", char_name_1, char_type_1, "in", round_count, "rounds")
     break
   elif battle_h2 <= 0:
     print(char_name_1, char_type_1, "destroyed", char_name_2, char_type_2, "in", round_count, "rounds")
     break
 
   
		
