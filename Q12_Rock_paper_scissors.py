from operator import truediv
from random import randint

def win():
    print ('You win!🙂')

def lose():
    print ('You lose!😔')

def want_to_continue(ans):
    if ans=='y':
        return True
    else:
        return False
a=want_to_continue(input("want to play rock, paper,scissors,enter 'y, or 'n':\n"))


while a:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]

    if player_choice == computer_choice:
       print ('Draw!')
    elif player_choice == 'rock' and computer_choice == 'scissors':
        win()
    elif player_choice  == 'paper' and computer_choice == 'scissors':
        lose()
    elif player_choice  == 'scissors' and computer_choice== 'paper':
        win
    elif player_choice == 'scissors' and computer_choice== 'rock':
        lose()
    elif player_choice == 'paper' and  computer_choice == 'rock':
        win()
    elif player_choice == 'rock' and computer_choice == 'paper':
        lose()
#     aGain = input('Do you want to play again? (y or n)').strip()
# if again == 'n':
#     break
    a=want_to_continue(input('Do you want to play again? (y or n):\n').strip())
else:
    print('Okay,bye,Have a good day!')

# def want_to_continue(ans):
#     if ans=='y':
#         return True
#     else:
#         return False

