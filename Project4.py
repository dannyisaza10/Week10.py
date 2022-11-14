player_hand = 17
dealer_hand = 19

if (player_hand < dealer_hand) > 21:
    print("The player wins!")
elif (player_hand > dealer_hand) < 21:
    print("The player loses!")
else:
    print("Push")


player_hand = 19
dealer_hand = 18

if (player_hand < dealer_hand) < 21:
    print("The player wins!")
elif (player_hand > dealer_hand) < 21:
    print("The player loses!")
else:
    print("Push")


player_hand = 22
dealer_hand = 20

if (player_hand < dealer_hand) > 21:
    print("The player wins!")
elif (player_hand > dealer_hand) < 21:
    print("The player loses!")
else:
    print("Push")


user_response = input("Do you want to play again? Y/N ")

if user_response.upper() == 'Y':
    print("Lets play again.")
elif user_response.upper() == 'N':
    print("Quitting.")
else:
    print("Error")




