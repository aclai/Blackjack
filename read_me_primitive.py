#Python 3.7.5

import deck
import card
import gameplay_method

main_deck = deck.Deck()
print(len(main_deck))
main_deck.create_full_deck()
print(len(main_deck))

player_hand = deck.Deck()
print(player_hand)
dealer_hand = deck.Deck()

player_hand.move_random_card(main_deck)
dealer_hand.move_random_card(main_deck)
print(player_hand[0].card_eng_name)
print(dealer_hand[0].card_eng_name)
print(len(main_deck))

gameplay_method.player_turn(player_hand, main_deck)
print(player_hand)
for i in player_hand:
    print(i.card_eng_name)
	
gameplay_method.dealer_turn(player_hand, dealer_hand, main_deck)

for i in dealer_hand:
    print(i.card_eng_name)

outcome = gameplay_method.check_winner(player_hand, dealer_hand)
print(outcome)



	