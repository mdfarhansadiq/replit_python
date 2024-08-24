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


while True:
	char_name, char_type = charNameType()
	char_health = charHealth()
	char_strength = charStrength()

	print(char_name, char_type)
	print("Health:", char_health)
	print("Strength:", char_strength)

	time.sleep(5)
	os.system("clear")
	gen_char = input("Do you want to generate more?(y/n): ")
	if gen_char == "y":
		continue
	else:
		break
	