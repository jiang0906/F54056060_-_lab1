# 設系統出手為隨機數，因為randint括號內要為整數，所以先設一個List
import random
GameList = ['ROCK', 'PAPER', 'SCISSORS']
GameMove = GameList[random.randint(0,2)]

# 記錄各次數
win_count = 0
loss_count = 0
tie_count = 0

# 設置遊戲邏輯
print("Welcome to ROCK, PAPER, SCISSORS game!")
while(win_count == 0):
    UserMove = input('Enter your move: (r)ock (p)aper (s)cissors ')
    if (UserMove == 'r'):
        print("ROCK versus...")
    elif (UserMove == 'p'):
        print("PAPER versus...")
    elif (UserMove == 's'):
        print("SCISSORS versus...")
    else:
        print("Invaild.")
    print(GameMove)
    if (UserMove == "r" and GameMove == "ROCK"):
        print("It is a tie!")
        tie_count += 1
    elif (UserMove == "p" and GameMove == "PAPER"):
        print("It is a tie!")
        tie_count += 1
    elif (UserMove == "s" and GameMove == "SCISSORS"):
        print("It is a tie!")
        tie_count += 1
    elif (UserMove == "r" and GameMove == "PAPER"):
        print("You loss!")
        loss_count += 1
    elif (UserMove == "p" and GameMove == "SCISSORS"):
        print("You loss!")
        loss_count += 1
    elif (UserMove == "s" and GameMove == "ROCK"):
        print("You loss!")
        loss_count += 1
    else:
        print("You win!")
        print('You have', tie_count, 'ties and',loss_count, 'losses before your win.')
        break