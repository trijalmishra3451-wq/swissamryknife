import time
import random
cheatCodeActive = True
canRun = True
humanTurn = True

def ask():
    #Rock: 1, Paper:2, Sissors:3
    game = input("What game do you want to play: tic, tack, toe or RPS(rock, paper, sissors)")
    Game = game.lower()
    if Game == "rps":
        rpsR()
        print("true")
    else:
        setUp()
        ttt()
def setUp():
    #Starting board values
    print("This is the starting board")
    print("\n")
    row3 = ['|','1','|','2','|','3','|']
    row2 = ['|','4','|','5','|','6','|']
    row1 = ['|','7','|','8','|','9','|']
    #starting board
    print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
    print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
    print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
    #player_tokens
    print("\n")
    print("Player 1 is O")
    print("Player 2 is X")
def ttt():
    ties = 0
    player_1_win = False
    player_2_win = False
    row3 = ['|','1','|','2','|','3','|']
    row2 = ['|','4','|','5','|','6','|']
    row1 = ['|','7','|','8','|','9','|']
    player_token = "X"
    ties = 0
    play_turn = 1
    while ties < 3 and player_1_win == False and player_2_win == False:
        """
        addIndex = None
        Middle is used for vertical rows
        #Center is used for horozontal rows
        #This is to add a new value
        #Possible values for "addIndex" are 1, 3, 5.
        """
        if player_token == "X":
            player_token = "O"
        else:
            player_token = "X"
        print("\n")
        pick = input("Where do you want to place your token? ")
        pick_conver = pick.lower()
        #Row 3
        if pick_conver == "1" and row3[1] == "1":
            row3[1] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        elif pick_conver == "2" and row3[3] == "2":
            row3[3] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        elif pick_conver == "3" and row3[5] == "3":
            row3[5] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        #Row 2
        elif pick_conver == "4" and row2[1] == "4":
            row2[1] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        elif pick_conver == "5" and row2[3] == "5":
            row2[3] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        elif pick_conver == "6" and row2[5] == "6":
            row2[5] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        #Row 1
        elif pick_conver == "7" and row1[1] == "7":
            row1[1] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        elif pick_conver == "8" and row1[3] == "8":
            row1[3] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        elif pick_conver == "9" and row1[5] == "9":
            row1[5] = player_token
            #Updated board
            print(row3[0],row3[1],row3[2],row3[3],row3[4],row3[5],row3[6])
            print(row2[0],row2[1],row2[2],row2[3],row2[4],row2[5],row2[6])
            print(row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row1[6])
        # Horozantal win detection
        if row3.count("X")== 3 or row2.count("X") == 3 or row1.count("X") == 3:
            player_1_win = True
            print("H")
        elif row3.count("O")== 3 or row2.count("O")== 3 or row1.count("O") == 3:
            print("H")
            player_2_win = True
        #Diagonal win detection
        elif row3[1]== "X" and row2[3]== "X" and row1[5] == "X" or row3[5]== "X" and row2[3]== "X" and row1[1] == "X":
            player_1_win = True
            print("D")
            break
        elif row3[1]== "O" and row2[3]== "O" and row1[5] == "O" or row3[5]== "O" and row2[3]== "O" and row1[1] == "O":
            player_2_win = True
            print("D")
            break
        #Vertical win detection
        elif row3[1] == "X" and row2[1] == "X" and row1[1] == "X" or row3[3] == "X" and row2[3] == "X" and row1[3] == "X" or row3[5] == "X" and row2[5] == "X" and row1[5] == "X":
            player_1_win = True
            print("V")
            break
        elif row3[1] == "O" and row2[1]== "O" and row1[1] == "O" or row3[3] == "O" and row2[3] == "O" and row1[3] == "O" or row3[5] == "O" and row2[5] == "O" and row1[5] == "O":
            player_2_win = True
            print("V")
            break
        else:
            print("akgakegn")
    if player_1_win == True:
        print("Player 1 wins!")
    elif player_2_win == True:
        print("Player 2 wins!")
def rpsR():
    mode = input("Automatic or Manual rock, paper sissors: ")
    amount = int(input("How many tries: "))
    lmode = mode.lower()
    print("\n")
    if "auto" in lmode :
        tries = 1
        for tries in range(amount):
            human_Try = random.randint(1,3)
            clanker_Try = random.randint(1,3)
            rps(human_Try,clanker_Try,tries,lword)
    #This is for manual mode
    else:
        tries = 1
        for tries in range(amount):
            clanker_Try = random.randint(1,3)
            human_Choice = input("Rock, Paper, or Sissors? : ")
            choice = human_Choice.lower()
            #Encoder------------------------------------
            if choice == "rock" or "r":
                human_Choice = 1
            elif choice == "paper" or "p":
                human_Choice = 2
            else:
                human_Choice = 3
            #-------------------------------------------
            print("Choosing....")
            time.sleep(5)
            rps(human_Choice,clanker_Try,tries,lword)
            
def report(human,clanker):
    print("You picked",human)
    print("And I picked",clanker)
    print("\n")
#Rock, paper, sissors
def rps(human_Try,clanker_Try,tries,lword):
    #Decoder
    if human_Try == 1:
        human_Choice = "Rock"
    elif human_Try == 2:
        human_Choice = "Paper"
    else:
        human_Choice = "Sissors"
        
    if clanker_Try == 1:
        clanker_Choice = "Rock"
    elif clanker_Try == 2:
        clanker_Choice = "Paper"
    else:
        clanker_Choice = "Sissors"
    #---------------------------------------
    #---------------------------------------
    #Checks winning conditions in a MASSIVE and block
    if human_Try == 1 and clanker_Try == 3 or human_Try == 2 and clanker_Try == 1 or human_Try == 3 and clanker_Try == 2:
        print("You won round", tries + 1)
        print("\n")
        report(human_Choice,clanker_Choice)
        if cheatCodeActive == True:
            report(human_Try,clanker_Try)
    elif human_Try == clanker_Try:
        print("Tie in round", tries + 1)
        print("\n")
        report(human_Choice,clanker_Choice)
        if cheatCodeActive == True:
            report(human_Try,clanker_Try)
    else:
        print("You lost round", tries + 1)
        print("\n")
        report(human_Choice,clanker_Choice)
        if cheatCodeActive == True:
            report(human_Try,clanker_Try)
    
def check(ori,word):
    duration = len(word)
    lastChar = duration - 1
    isPalindrome = None
    #The checker wrap around
    for firstChar in range(duration):
        if word[firstChar] == word[lastChar]:
            print("Yes, charather ",firstChar+1," is correct and is '",word[firstChar],"'")
            lastChar = lastChar-1
            isPalindrome = True
        else:
            isPalindrome = False
            print("no",word[firstChar],word[lastChar])
            break
    if isPalindrome == True:
        print(ori,"is a palindrome")

#Inputs
canRun = True
cheatCodeActive = False
original = input("Want to play a game, or check if a word is a palindrome? ")
lword = original.lower()
if "game" in lword:
    if ",debug" in lword:
        cheatCodeActive = True
    ask()
else:
    check(original,lword)