
def do_init():
    global player1_move
    global player2_move
    global player1_score
    global player2_score
    player1_score = 0
    player2_score = 0
    player1_move = "B"
    player2_move = "B"

def do_score():
    global player1_score
    global player2_score
    print("player 1: ", player1_score)
    print("player 2: ", player2_score)

def do_input():
    global player1_move
    global player2_move
    player1_move = input("Player 1 move (R, P, S): ")
    player2_move = input("Player 2 move (R, P, S): ")

def get_who_won(move1, move2):  

    if move1 == move2 :
        #print("Draw")
        return 0
    elif move1 == "R" and move2 == "P" :
        #print("player 2 wins")
        return 2
    elif move1 == "R" and move2 == "S" :
        #print("player 1 wins")
        return 1
    elif move1 == "S" and move2 == "P" :
        #print("player 1 wins")
        return 1
    elif move1 == "S" and move2 == "R" :
        #print("player 2 wins")
        return 2
    elif move1 == "P" and move2 == "R" :
        #print("player 1 wins")
        return 1
    elif move1 == "P" and move2 == "S" :
        #print("player 2 wins")
        return 2

def do_turn():
    global player1_move
    global player2_move
    global player1_score
    global player2_score

    result = get_who_won(player1_move, player2_move)
    if result == 1:
        player1_score += 1
    elif result == 2:
        player2_score += 1
    
def do_play():
    global player1_score
    global player2_score
    do_init()
    
    while player1_score < 3 and player2_score < 3 :
        do_input()
        do_turn()
        do_score()



