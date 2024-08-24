### ******* In the name of Allah *******###


import random


list_of_words = ['superb', 'virtual', 'machine', 'web', 'verifiable']

word_val = random.choice(list_of_words)


life_line = 6
letter_position = []


for i in range(len(word_val)):
  letter_position.append(0)
  
  
print("🌟Hangman🌟")

count_letter = 0

while True:
  
  if life_line == 0:
    print("You lost!")
    break
  
  if count_letter == (len(word_val)):
    print(f"You won with {life_line} chances.")
    break
  
  letter_val = input("Choose a letter: ")
  
  check_letter = False
  same_letter = True
  
  for letter in range(len(word_val)):
    if word_val[letter] == letter_val:
      if letter_position[letter] == 0:
        letter_position[letter] = 1
        check_letter = True
        same_letter = False
        count_letter += 1
        print("Correct!")
        break
      elif letter_position[letter] == 1:
        check_letter = True
        print("You have used that letter before!")
  
  if check_letter == True and same_letter == False:
    for i in range(len(letter_position)):
      if letter_position[i] == 1:
        print(word_val[i], end="")
      else:
        print("_", end="")
        
  if check_letter == False:
    life_line -= 1
    if life_line:
      print("Nope, not in there.\n {} left".format(life_line))
  print("")