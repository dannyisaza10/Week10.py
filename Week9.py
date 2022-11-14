user_response = input("Do you want to play again? Y/N ")

if user_response.upper() == 'Y':
    print("Lets play again.")
elif user_response.upper() == 'N':
    print("Quitting.")
else:
    print("Error")