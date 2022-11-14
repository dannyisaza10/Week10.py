print("Hello")
print(type(5.3))



my_list = ['Tyler', 'Adam', 'Abby', 'Michael', 'Joey']

print(sorted(my_list))

def blackjack_hand2(player_hand):
    player_hand = 17
    dealer_hand = 19
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")

blackjack_hand2(21)

print()

def greeting(name):
    print(f'Hello, {name}!')

greeting(input)
greeting('Tyler')

print()

def cheer():
    print('Go Bears!')

cheer()

print()


def cheer2(team_name):
    for i in range(3):
        print(f'Go {team_name}!')

cheer2('Patriots')

print()

cheer2('Bruins')
print()
def main():
    cheer2('Patriots')
    print()
    cheer2('Bruins')
    print()
    cheer2('Revs')

main()

def prompt_for_name():
    name = input("What is your name?")
    print(f"Hello, {name}")

def while_with_flag():
    prompt = "\nTell me something, and I'll "
    prompt += "repeat it back to you."
    prompt += "\nEnter 'quit' to end the program."
    active = True
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)

while_with_flag()

def blackjack_hand3(player_hand, dealer_hand):
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")

blackjack_hand3(21, 15)

def cheer3(team_name, times):
    for i in range(times):
        print(f'Go {team_name}!')

cheer3('Patriots', 5)


