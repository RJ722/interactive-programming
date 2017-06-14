# Rock-paper-scissors-lizard-Spock game
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    
    if name == "rock" :
        return '0'
    elif name == "spock":
        return '1'
    elif name == "paper":
        return '2'
    elif name == "lizard":
        return '3'
    elif name == "scissors":
        return '4'
    else:
        print "WRONG INPUT"
    


def number_to_name(number):
    
    if number == 0 :
        return "rock"
    elif number == 1:
        return "spock"
    if number == 2:
        return "paper"
    if number == 3:
        return "lizard"
    if number == 4:
        return "scissors"
    else:
        return "wrong input!"
    
    
   
def rpsls(player_choice): 
   
    
    # print a blank line to separate consecutive games
      print ""
    # print out the message for the player's choice
      print "Player chooses " + player_choice
    # convert the player's choice to player_number using the function name_to_number()
      player_number=name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
      comp_number=random.randrange(0, 4)
    # convert comp_number to comp_choice using the function number_to_name()
      comp_choice=number_to_name(comp_number)
    # print out the message for computer's choice
      print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
      result = int(comp_number) - int(player_number) % 5
    # use if/elif/else to determine winner, print winner message
      if (result == 1) or (result== 2):
            print "Computer wins"
      elif (result ==3)or (result ==4):

            print "Player wins!"
                else:
                    print "There is something wrong!"
        
            
    
# Takes input from user
user_input = input('Enter your name: ')
user_choice = input('Enter your choice:').lower()
# Print user's name and choice
print "Hey!" + user_input 
print "You choose "  + user_choice



rpsls(user_choice)

#Test functions
#rpsls("rock")
#rpsls("Spock")
#rpsls("paper")
#rpsls("lizard")
#rpsls("scissors")



