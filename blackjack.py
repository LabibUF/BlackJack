# imports random number generator
from p1_random import P1Random

rng = P1Random()

# setting up variables
users_inputs = 1
game_number = 1
player_hand = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

# if a number other than 4 is entered then the game runs
while users_inputs != 4:
    print(f"START GAME #{game_number}")
    game_number += 1
    player_hand = 0

    # draw random card
    card_name = rng.next_int(13) + 1

    # transforming the card into a value and prints what the player hand is
    card_value = 0
    if card_name == 13:
        print("Your card is a KING!")
        card_value = 10
    elif card_name == 12:
        print("Your card is a QUEEN!")
        card_value = 10
    elif card_name == 11:
        print("Your card is a JACK!")
        card_value = 10
    elif card_name == 1:
        print("Your card is a ACE!")
        card_value = 1
    elif card_name >= 2 and card_name <= 10:
        print(f"Your card is a {card_name}!")
        card_value = card_name

    player_hand += card_value
    print("Your hand is:", player_hand)
    current_game = True

    # Loop was created so that the game can continue running using the selection menu
    while current_game:
        print("1. Get another card \n2. Hold hand \n3. Print statistics \n4. Exit")
        users_inputs = int(input("Choose an option: "))

        # When user enters 1 card is drawn and you can keep drawing till you lose or get Blackjack
        if users_inputs == 1:
            card_name = rng.next_int(13) + 1
            card_value = 0
            # transforming the card into a value
            card_value = 0
            if card_name == 13:
                print("Your card is a KING!")
                card_value = 10
            elif card_name == 12:
                print("Your card is a QUEEN!")
                card_value = 10
            elif card_name == 11:
                print("Your card is a JACK!")
            elif card_name == 1:
                print("Your card is a ACE!")
                card_value = 1
            elif card_name >= 2 and card_name <= 10:
                print(f"Your card is a {card_name}!")
                card_value = card_name

            player_hand += card_value
            print("Your hand is:", player_hand)

            if player_hand > 21:
                print("You exceeded 21! You lose.")
                current_game = False
                dealer_wins += 1


            if player_hand == 21:
                print("BLACKJACK! You win!")
                current_game = False
                player_wins += 1


        # if 2 is entered you hold your hand and see what the dealer's hand is and it is decided if you won or lost
        if users_inputs == 2:
            dealer_hand = rng.next_int(11) + 16
            print("Dealer's hand:", dealer_hand)
            print("Your hand is:", player_hand)

            if dealer_hand > 21:
                print("You win!")
                player_wins += 1

                current_game = False
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!")
                tie_games += 1

                current_game = False
            elif dealer_hand > player_hand and dealer_hand <= 21:
                print("Dealer wins!")
                dealer_wins += 1

                current_game = False
            elif player_hand > dealer_hand and player_hand <= 21:
                print("You Win!")
                player_wins += 1

                current_game = False

        # If 3 is entered the statistics of the game is printed
        if users_inputs == 3:
            print("Number of Player wins:", player_wins)
            print("Number of Dealer wins:", dealer_wins)
            print("Number of tie games:", tie_games)
            print("Total # of games played is:", (player_wins + dealer_wins + tie_games))
            percent = ((player_wins / (player_wins + dealer_wins + tie_games))*100)
            print("Percentage of Player wins:", "{:.1f}".format(percent), "%")

        # If another number not listed in the selection is entered it will say Invalid
        if users_inputs > 4 or users_inputs < 1:
            print("Invalid input! \nPlease enter an integer value between 1 and 4.")


        # If user enters 4 the game will end
        if users_inputs == 4:
            current_game = False
