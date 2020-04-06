import sys,random

print('Rock, Paper, Scissors')

wins = 0
losses = 0
ties = 0
list = ['Rock', 'Paper', 'Scissors']
while True:
    print('%s wins, %s losses, %s ties' %(wins, losses, ties))
    while True:
        print("Enter your move: r(rock), s(scissor), p(paper) or q(quit)")
        player_move=input()
        if player_move == 'q':
            sys.exit()
        elif player_move == 'r':
            print("Rock versus ...")
            break
        elif player_move == 's':
            print("Scissor versus ...")
            break
        elif player_move == 'p':
            print("Paper versus ...")
            break
        else :
            print('Please, type s,r,q or p')

    random_choice = random.choice(list)
    print(random_choice)
    if (player_move == 'r' and random_choice == "Rock") or (player_move == 'p' and random_choice == "Paper") or (player_move == 's' and random_choice == "Scissor"):
        print("It's a tie")
        ties += 1
    elif (player_move == 'r' and random_choice == "Paper") or (player_move == 'p' and random_choice == "Scissor") or (player_move == 's' and random_choice == "Rock"):
        print('You lost')
        losses += 1
    elif (player_move == 'r' and random_choice == "Scissor") or (player_move == 'p' and random_choice == "Rock") or (player_move == 's' and random_choice == "Paper"):
        print('You won')
        wins += 1