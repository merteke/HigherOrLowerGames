import random
import os
from art import logo,vs_logo
from my_data import peak_players,random_key


cls=lambda: os.system('cls')

print(f'{logo}\n WELCOME TO HIGHER OR LOWER GAME!\n')
higher=int()
score=0
your_answer=""
real_answer=""
answer_game=""
game1=int()
game2=int()
game1_name=""
game2_name=""


while True:
    print("Which game has higher peak players?")
    higher=0
    for i in range(1,3):
        all_games=peak_players
        game=random_key()
        
        if i == 1:
            game1_name=game
            game1=all_games[game]
            print(f'A){game}')
            higher=all_games[game]
            answer_game=game
            real_answer="A"
            all_games.pop(game)
            
            print(vs_logo)
        elif i == 2:
            game2_name=game
            game2=all_games[game]
            
            if all_games[game]>higher:
                higher=all_games[game] 
                real_answer="B"
                all_games.pop(game)
            print(f'B){game}')
    answer=input("Your answer:")
    if str.lower(answer) == str.lower(real_answer):
        cls()
        print(f"{game1_name}:{game1}   {game2_name}:{game2}")
        score+=1
        print(f"Your score:{score}")
        input("Press 'ENTER' for next!")
    else:
        cls()
        print(f"{game1_name}:{game1}   {game2_name}:{game2}")
        print(f'Wrong answer!\nScore:{score}')
        score=0
        play_again=input(f"Play again?(y/n):\n")
        if str.lower(play_again)=="n":
            break
        
    
        
    
        
    
    
    
