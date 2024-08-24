###******* In the name of Allah *******###


num_var = 100
num_of_attempt = 0
print("Let's play - Guess The Number")
while True:
  player_num = int(input("Enter a number: "))
  
  num_of_attempt += 1
  
  if player_num >= 0:
    if player_num == num_var:
      print("Congratulations! You are the winner.")
      break
    
    elif player_num < num_var:
      print("too low...")
      
    elif player_num > num_var:
      print("too high...")
  else:
    exit()
print("Number of Attempts:", num_of_attempt)
    
  
      