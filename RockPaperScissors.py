# 設系統出手為隨機數，因為randint括號內要為整數，所以先設一個List
import random
GameList = ['ROCK', 'PAPER', 'SCISSORS']
GameMove = GameList[random.randint(0,2)]

# 記錄各起始次數
win_count = 0
loss_count = 0
tie_count = 0

# 設置遊戲邏輯
print("Welcome to ROCK, PAPER, SCISSORS game!")
while(win_count == 0):
    UserMove = input('Enter your move: (r)ock (p)aper (s)cissors ')
    if (UserMove == 'r'):                   # 先設置玩家出手時會出現的...versus
        print("ROCK versus...")
    elif (UserMove == 'p'):
        print("PAPER versus...")
    elif (UserMove == 's'):
        print("SCISSORS versus...")
    else:                                   # 若有輸入非'r','p','s'時，給予Invalid之提示
        print("Invaild.")
    print(GameMove)
    if (UserMove == "r" and GameMove == "ROCK"):      # 輸贏之邏輯 以及 紀錄平手和敗場次數
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
    else:                                   # 勝利之後即結算，並終止遊戲
        print("You win!")
        print('You have', tie_count, 'ties and',loss_count, 'losses before your win.')
        break