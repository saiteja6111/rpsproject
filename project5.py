
import random

value_1  = '''
 _   ____  _   _ _   _ 
/ | |  _ \| | | | \ | |
| | | |_) | | | |  \| |
| | |  _ <| |_| | |\  |
|_| |_| \_\\___/|_| \_|


'''

value_2  = '''

 ____    ____  _   _ _   _ ____  
|___ \  |  _ \| | | | \ | / ___| 
  __) | | |_) | | | |  \| \___ \ 
 / __/  |  _ <| |_| | |\  |___) |
|_____| |_| \_\\___/|_| \_|____/ 

'''

value_3 = '''

 _____   ____  _   _ _   _ ____  
|___ /  |  _ \| | | | \ | / ___| 
  |_ \  | |_) | | | |  \| \___ \ 
 ___) | |  _ <| |_| | |\  |___) |
|____/  |_| \_\\___/|_| \_|____/ 


'''

value_4 = '''

 _____ ___  _   _ ____    _  _   
|  ___/ _ \| | | |  _ \  | || |  
| |_ | | | | | | | |_) | | || |_ 
|  _|| |_| | |_| |  _ <  |__   _|
|_|   \___/ \___/|_| \_\    |_|  

'''


value_5 = '''

 ____ _____  __   __   
/ ___|_ _\ \/ /  / /_  
\___ \| | \  /  | '_ \ 
 ___) | | /  \  | (_) |
|____/___/_/\_\  \___/ 


'''

print('\tWELCOME TO HAND CRICKET🏏\n')

print('\tChoose 1️⃣ PLAYER or 2️⃣ PLAYERS\n')

players = int(input('Enter you Choice 1 or 2 :'))

if players == 1:
    name = input('Enter your name : ')
    print(f"\t PLAYER({name}) VS COMPUTER \n")
    print("\tLet's Toss choose EVEN or ODD")
    toss_player = input("type EVEN or ODD : ")
    toss_computer =  random.choice(['EVEN','ODD'])
    if toss_player != toss_computer:
        print('You loss the Toss! Computer Won')
        game_choice_computer = random.choice(['Bat', 'Bowl'])
        print(f'Computer chooses to {game_choice_computer} first!!!')
        if game_choice_computer.upper() == 'BOWL':
            print('Lets Begin! Match')
            print('You are Batsman , Computer is Bowler')
            Total_player = 0
            player_game = int(input('Enter Your hitting choice 1,2,3,4 or 6 : '))
            computer_game = random.choice([1,2,3,4,6])
            while Total_player == 0 or player_game != computer_game:
                if player_game == 1:
                    print(value_1)
                    Total_player +=1
                elif player_game == 2:
                    print(value_2)
                    Total_player += 2
                elif player_game == 3:
                    print(value_3)
                    Total_player += 3
                elif player_game == 4:
                    print(value_4)
                    Total_player += 4
                elif player_game == 6:
                    print(value_5)
                    Total_player += 6
                player_game = int(input('Enter Your Choice 1,2,3,4 or 6 : '))
                computer_game = random.choice([1,2,3,4,6])
            print('Out!')
            print(f'Your Score is {Total_player}')
            print(f'Lets Start second Innings......')
            print('Lets Begin! Match')
            print('You are Bowler, Computer is Batsman')
            Total_computer = 0
            player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
            computer_game2 = random.choice([1,2,3,4,6])
            while Total_computer == 0 or player_game2 != computer_game2:
                if computer_game2 == 1:
                    print(value_1)
                    Total_computer += 1
                elif computer_game2 == 2:
                    print(value_2)
                    Total_computer += 2
                elif computer_game2 == 3:
                    print(value_3)
                    Total_computer += 3
                elif computer_game2 == 4:
                    print(value_4)
                    Total_computer += 4
                elif computer_game2 == 6:
                    print(value_5)
                    Total_computer += 6
                player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
                computer_game2 = random.choice([1,2,3,4,6])
            print('Player is OUT!')
            print(f'Computer Score is {Total_computer}')
            if Total_player > Total_computer:
                print(f'Congratulations! {name} you won the match')
            else:
                print(f'You Lost the match!😩')   
        elif game_choice_computer.upper() == 'BAT':
            print("Let's Begin Match")
            print('You are Bowler, Computer is Batsman')
            Total_computer = 0
            player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
            computer_game2 = random.choice([1,2,3,4,6])
            while Total_computer == 0 or player_game2 != computer_game2:
                if computer_game2 == 1:
                    print(value_1)
                    Total_computer += 1
                elif computer_game2 == 2:
                    print(value_2)
                    Total_computer += 2
                elif computer_game2 == 3:
                    print(value_3)
                    Total_computer += 3
                elif computer_game2 == 4:
                    print(value_4)
                    Total_computer += 4
                elif computer_game2 == 6:
                    print(value_5)
                    Total_computer += 6
                player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
                computer_game2 = random.choice([1,2,3,4,6])
            print('Player is OUT!')
            print(f'Computer Score is {Total_computer}')
            print(f'Lets Start second Innings......')
            print('Lets Begin! Match')
            print('You are Batsman , Computer is Bowler')
            Total_player = 0
            player_game = int(input('Enter Your hitting choice 1,2,3,4 or 6 : '))
            computer_game = random.choice([1,2,3,4,6,])
            while Total_player == 0 or player_game != computer_game:
                if player_game == 1:
                    print(value_1)
                    Total_player +=1
                elif player_game == 2:
                    print(value_2)
                    Total_player += 2
                elif player_game == 3:
                    print(value_3)
                    Total_player += 3
                elif player_game == 4:
                    print(value_4)
                    Total_player += 4
                elif player_game == 6:
                    print(value_5)
                    Total_player += 6
                player_game = int(input('Enter Your Choice 1,2,3,4 or 6 : '))
                computer_game = random.choice([1,2,3,4,6])
            print('Out!')
            print(f'Your Score is {Total_player}')
            if Total_player > Total_computer:
                print(f'Congratulations! {name} you won the match')
            else:
                print(f'You Lost the match!😩')

    elif toss_player == toss_computer:
        print('You won the Toss!')
        game_choice_player = input('Enter your choice Bat or Bowl : ')
        if game_choice_player.upper() == 'BAT':
            print('You are Batsman , Computer is Bowler')
            print(f'Player Chooses to {game_choice_player} First !')
            print('Lets Begin! Match')
            Total_player = 0
            player_game = int(input('Enter Your hitting choice 1,2,3,4 or 6 : '))
            computer_game = random.choice([1,2,3,4,6])
            while Total_player == 0 or player_game != computer_game:
                if player_game == 1:
                    print(value_1)
                    Total_player +=1
                elif player_game == 2:
                    print(value_2)
                    Total_player += 2
                elif player_game == 3:
                    print(value_3)
                    Total_player += 3
                elif player_game == 4:
                    print(value_4)
                    Total_player += 4
                elif player_game == 6:
                    print(value_5)
                    Total_player += 6
                player_game = int(input('Enter Your Choice 1,2,3,4 or 6 : '))
                computer_game = random.choice([1,2,3,4,6])
            print('Out!')
            print(f'Your Score is {Total_player}')
            print(f'Lets Start second Innings......')
            print('Lets Begin! Match')
            print('You are Bowler, Computer is Batsman')
            Total_computer = 0
            player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
            computer_game2 = random.choice([1,2,3,4,6])
            while Total_computer == 0 or player_game2 != computer_game2:
                if computer_game2 == 1:
                    print(value_1)
                    Total_computer += 1
                elif computer_game2 == 2:
                    print(value_2)
                    Total_computer += 2
                elif computer_game2 == 3:
                    print(value_3)
                    Total_computer += 3
                elif computer_game2 == 4:
                    print(value_4)
                    Total_computer += 4
                elif computer_game2 == 6:
                    print(value_5)
                    Total_computer += 6
                player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
                computer_game2 = random.choice([1,2,3,4,6])
            print('Player is OUT!')
            print(f'Computer Score is {Total_computer}')
            if Total_player > Total_computer:
                print(f'Congratulations! {name} you won the match')
            else:
                print(f'You Lost the match!😩') 
        elif game_choice_player.upper() == 'BOWL':
            print("Let's Begin Match")
            print('You are Bowler, Computer is Batsman')
            Total_computer = 0
            player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
            computer_game2 = random.choice([1,2,3,4,6])
            while Total_computer == 0 or player_game2 != computer_game2:
                if computer_game2 == 1:
                    print(value_1)
                    Total_computer += 1
                elif computer_game2 == 2:
                    print(value_2)
                    Total_computer += 2
                elif computer_game2 == 3:
                    print(value_3)
                    Total_computer += 3
                elif computer_game2 == 4:
                    print(value_4)
                    Total_computer += 4
                elif computer_game2 == 6:
                    print(value_5)
                    Total_computer += 6
                player_game2 = int(input('Enter Your Bowling Choice 1,2,3,4 or 6 : '))
                computer_game2 = random.choice([1,2,3,4,6])
            print('Player is OUT!')
            print(f'Computer Score is {Total_computer}')
            print(f'Lets Start second Innings......')
            print('Lets Begin! Match')
            print('You are Batsman , Computer is Bowler')
            Total_player = 0
            player_game = int(input('Enter Your hitting choice 1,2,3,4 or 6 : '))
            computer_game = random.choice([1,2,3,4,6,])
            while Total_player == 0 or player_game != computer_game:
                if player_game == 1:
                    print(value_1)
                    Total_player +=1
                elif player_game == 2:
                    print(value_2)
                    Total_player += 2
                elif player_game == 3:
                    print(value_3)
                    Total_player += 3
                elif player_game == 4:
                    print(value_4)
                    Total_player += 4
                elif player_game == 6:
                    print(value_5)
                    Total_player += 6
                player_game = int(input('Enter Your Choice 1,2,3,4 or 6 : '))
                computer_game = random.choice([1,2,3,4,6])
            print('Out!')
            print(f'Your Score is {Total_player}')
            if Total_player > Total_computer:
                print(f'Congratulations! {name} you won the match')
            else:
                print(f'You Lost the match!😩')
        
            
            
        












