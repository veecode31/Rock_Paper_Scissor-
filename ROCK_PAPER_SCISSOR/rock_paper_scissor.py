# print("...ROCK...")
# print("...PAPER...")
# print("...SCISSOR...")

# player1_choice = input("Please enter player 1's choice: ")
# player2_choice = input("Please enter player 2's choice: ")

# if player1_choice == player2_choice:
#     print("It's a tie!")
# elif (
#     (player1_choice == "rock" and player2_choice == "scissor")
#     or (player1_choice == "scissor" and player2_choice == "paper")
#     or (player1_choice == "paper" and player2_choice == "rock")
# ):
#     print("Player 1 wins!")
# elif (
#     (player2_choice == "rock" and player1_choice == "scissor")
#     or (player2_choice == "scissor" and player1_choice == "paper")
#     or (player2_choice == "paper" and player1_choice == "rock")
# ):
#     print("Player 2 wins!")
# else:
#     print("Invalid choice")

# ---------------- Modified code of ROCK, PAPER, SCISSOR ----------------------------------------------------------------
 
# print("...ROCK...")
# print("...PAPER...")
# print("...SCISSOR...")

# player1_choice = input("Please enter player 1's choice: ")
# player2_choice = input("Please enter player 2's choice: ")

# if player1_choice == "rock":
#     if player2_choice == "paper":
#         print("Player 2 wins")
#     elif player2_choice == "scissor":
#         print("Player 1 wins")
# if player1_choice == "paper":
#     if player2_choice == "rock":
#         print("Player 1 wins")
#     elif player2_choice == "scissor":
#         print("Player 2 wins")
# if player1_choice == "scissor":
#     if player2_choice == "rock":
#         print("Player 2 wins")
#     elif player2_choice == "paper":
#         print("Player 1 wins")
#     else:
#         print("Invalid choice")
# if player1_choice == player2_choice:
#     print("It's a tie!")



# ------------------------------------------------ AUTOMATED CODE -----------------------------------------------------------------------


import random

options = ["rock", "paper", "scissor"]

while True:
    print()
    print("...ROCK...")
    print("...PAPER...")
    print("...SCISSOR...")

    player1_choice = input("Please enter player 1's choice: ")
    player2_choice = random.choice(options)
    print(f"Player 2 said: {player2_choice}")

    if player1_choice == player2_choice:
        print("It's a tie!")
    elif (
        (player1_choice == "rock" and player2_choice == "scissor")
        or (player1_choice == "scissor" and player2_choice == "paper")
        or (player1_choice == "paper" and player2_choice == "rock")
    ):
        print("Player 1 wins!")
    elif (
        (player2_choice == "rock" and player1_choice == "scissor")
        or (player2_choice == "scissor" and player1_choice == "paper")
        or (player2_choice == "paper" and player1_choice == "rock")
    ):
        print("Player 2 wins!")
    else:
        print("Invalid choice")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        print("Thank you for playing!")
        break
